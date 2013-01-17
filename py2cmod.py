# py2cmod - Generate C extension module skeleton from a Python module
# while aiming to keep the same interface and not break existing code

import sys, os.path, imp, types, getopt
version='0.1.2'
templates = {}

class CModule:
    '''Handles the conversion of a Python module object to a C extension module'''
    def __init__(self, name, obj, outfile):
        '''__init__(self, name, obj, outfile):
        name     -> The name of the module
        obj        -> The module object
        outfile    -> A file-like object to receive the C source code'''
        self._name = name
        self._obj = obj
        self._outfile = outfile

    def process(self):
        '''Generate the C source code, and process the module's members'''
        classes = []
        functions = []
        constants = []

        # output a copyright notice
        copyright_vars = {}
        self._outfile.write(templates['copyright'] % copyright_vars)

        # output the module header
        module_head_vars = {}
        self._outfile.write(templates['module_head'] % module_head_vars)
        
        # loop over each attribute of the module and append each
        # attribute to the relevant list
        module = self._obj
        for objname in dir(module):
            obj = getattr(module, objname)
            if type(obj) == types.FunctionType:
                functions.append((objname, obj))
                continue
            elif type(obj) == types.ClassType:
                classes.append((objname, obj))
                continue
            elif type(obj) == types.IntType or type(obj) == types.LongType:
                constants.append((objname, obj))
                continue
            elif type(obj) == types.StringType:
                constants.append((objname, obj))
                continue

        self._func_decls = []
        self._const_decls = []        
        # for each class, create a CClass object, and process the class    
        for c in classes:
            t = CClass(c[0], c[1], self._outfile, self)
            t.process()

        # for each function, create a CFunction object, process the function,
        # and collect the function declaration
        for f in functions:
            func = CFunction(f[0], f[1], self._outfile, self)
            func.process()

        # for each function, create a CConstant object, process the constant,
        # and collect the constant declaration
        for c in constants:
            const = CConstant(c[0], c[1], self._outfile, self)
            const.process()

        # write the module tail, which includes the function
        # declarations and constant declarations that have been
        # collected previously
        module_tail_vars = {'abbrev': self._name, 'methodlist': ''.join(self._func_decls),
                            'name': self._name, 'constlist': ''.join(self._const_decls)}
        self._outfile.write(templates['module_tail'] % module_tail_vars)
            

class CClass:
    '''Handles the conversion of a class object into the C source code'''
    def __init__(self, name, obj, outfile, module):
        '''__init__(self, name, obj, outfile, module):
        name     -> The name of the class
        obj        -> The class object
        outfile    -> A file-like object to receive the C source code
        module  -> The parent module'''
        self._name = name
        self._obj = obj
        self._outfile = outfile
        self._module = module

    def process(self):
        '''Generate the C source code, and process the classes members'''

        # TODO: Scan for variables declared in the class, but before
        # the __init__ method, and output them as PyObject *'s in the
        # object declaration

        # output the object header
        object_head_vars = {'object_def': '', 'type_abbrev': self._name}
        self._outfile.write(templates['object_head'] % object_head_vars)
        
        self._method_decls = []
        self._func_decls = []
        
        m = CMethod('', None, self._outfile, self._module, self, 'object_new')
        m.process()
        del self._method_decls[-1]
        f = CFunction(self._name, None, self._outfile, self._module)
        f.process()
        del self._func_decls

        for m in templates.keys():
            if m.startswith('object_tp') and not m.startswith('object_tp_as'):
                tp_meth = CMethod(m, None, self._outfile, self._module, self, m)
                tp_meth.process()
                del self._method_decls[-1]

        methods = []
        # loop over the classes members and add them to the
        # appropriate list
        for m in dir(self._obj):
                obj = getattr(self._obj, m)
                if type(obj) == types.MethodType and m not in ('__init__', '__getattr__', '__setattr__', '__del__'):
                    methods.append((m, obj))

        # for each method, create a CMethod object, process the
        # method, and collect the method declaration
        for m in methods:
            meth = CMethod(m[0], m[1], self._outfile, self._module, self)
            meth.process()

        # output the objects method list
        object_mlist_vars = {'type_abbrev': self._name, 'method_list': ''.join(self._method_decls)}
        self._outfile.write(templates['object_mlist'] % object_mlist_vars)

        # get the objects docstring, or an empty string if none
        try:
            doc = self._obj.__doc__
        except:
            doc = None
        if not doc:
            doc = ''

        # output the object tail, with NULL values for all of the slots
        object_tail_vars = {'type_abbrev': self._name, 'type_doc': doc,
                            'tp_dealloc': '0', 'tp_print': '0', 'tp_getattr': '0',
                            'tp_setattr': '0', 'tp_compare': '0', 'tp_repr': '0',
                            'tp_as_number': '0', 'tp_as_mapping': '0',
                            'tp_as_sequence': '0', 'tp_hash': '0', 'tp_call': '0',
                            'tp_str': '0'}
        self._outfile.write(templates['object_tail'] % object_tail_vars)

class CMethod:
    '''Handles the generation of C source code for a Python method'''
    def __init__(self, name, obj, outfile, module, cclass, template='object_method', opt_keys=None):
        '''__init__(self, name, obj, outfile, module, cclass, template, opt_keys):
        name     -> The name of the method
        obj        -> The method object
        outfile    -> A file-like object to receive the C source code
        module   -> The parent module
        cclass    -> The parent class
        template -> The template to use
        opt_keys -> Optional keys to use in variable substitution in the template'''
        self._name = name
        self._obj = obj
        self._outfile = outfile
        self._module = module
        self._class = cclass
        self._template = template
        self._opt_keys = opt_keys

    def process(self):
        '''Generate the C source code'''
        # get the methods docstring, or an empty string if none
        try:
            doc = self._obj.__doc__
        except:
            doc = None
        if not doc:
                doc = ''

        # Attempt to generate the appropriate function signature
        try:
            # ignore the /first/ argument, as that is self
            arg_count = self._obj.func_code.co_argcount - 1
            method_sig = 'O' * arg_count
            param_vars = ''.join(['PyObject *arg%d;' % (x, ) for x in range(arg_count)])
            parse_params = ''.join([', &arg%d' % (x, ) for x in range(arg_count)])
        except AttributeError:
            # Not really a function object
            method_sig = ''
            param_vars = ''
            parse_params = ''

        # output the method skeleton and docstring
        object_method_vars = {'type_abbrev': self._class._name, 'method': self._name,
                              'method_doc': doc, 'abbrev': self._module._name,
                              'method_sig': method_sig, 'param_vars': param_vars, 'parse_params': parse_params}
        if self._opt_keys:
            object_method_vars.update(self._opt_keys)
        self._outfile.write(templates[self._template] % object_method_vars)

        # return the method declaration
        self._class._method_decls.append(templates['method_list'] % object_method_vars)

class CFunction:
    '''Handles the generation of C source code for Python functions'''
    def __init__(self, name, obj, outfile, module):
        '''__init__(self, name, obj, outfile, module):
        name     -> The name of the function
        obj        -> The function object
        outfile    -> A file-like object to receive the C source code
        module   -> The parent module'''
        self._name = name
        self._obj = obj
        self._outfile = outfile
        self._module = module

    def process(self):
        '''Generate the C source code'''
        # retrieve the functions docstring, or an empty string if none
        try:
            doc = self._obj.__doc__
        except:
            doc = None
        if not doc:
            doc = ''

        # Attempt to generate the appropriate function signature
        try:
            arg_count = self._obj.func_code.co_argcount
            method_sig = 'O' * arg_count
            param_vars = ''.join(['PyObject *arg%d;' % (x, ) for x in range(arg_count)])
            parse_params = ''.join([', &arg%d' % (x, ) for x in range(arg_count)])
        except AttributeError:
            # Not really a function object
            method_sig = ''
            param_vars = ''
            parse_params = ''

        # output the method skeleton and docstring
        module_method_vars = {'abbrev': self._module._name, 'method': self._name,
                              'method_doc': doc, 'param_vars': param_vars, 'method_sig': method_sig, 'parse_params': parse_params}
        self._outfile.write(templates['module_method'] % module_method_vars)

        # return the method declaration
        self._module._func_decls.append(templates['method_list'] % module_method_vars)

class CConstant:
    '''Handles the generation of C source code for a module-level constant'''
    def __init__(self, name, obj, outfile, module):
        '''__init__(self, name, obj, outfile, module):
        name     -> The name of the constant
        obj        -> The constant object
        outfile    -> A file-like object to receive the C source code
        module   -> The parent module'''
        self._name = name
        self._obj = obj
        self._outfile = outfile
        self._module = module

    def process(self):
        '''Generate the C source code'''

        # return the constant declaration
        constant_vars = {'const_name': self._name, 'value': self._obj}
        if type(self._obj) == types.StringType:
            t = templates['constant_str']
        else:
            t = templates['constant_int']
        self._module._const_decls.append(t % constant_vars)

def useage():
    print '''Useage: python %s [-h] [-o filemodule.c] file.py [file2.py ...]

    -h: Display this help information
    -o: Set the output file name.  Only valid if only
        one file is mentioned on the command line.''' % (sys.argv[0], )

def copyright():
    print '''py2cmod %s, Copyright (C) 2001 Mark Rowe
py2cmod comes with ABSOLUTELY NO WARRANTY.
This is free software, and you are welcome to redistribute it
under certain conditions.  Read COPYING for details.
''' % (version, )


def main():
    try:
        opts, args = getopt.getopt(sys.argv[1:], "ho:", ["help", "output="])
    except getopt.GetoptError:
        sys.exit(2)
    output = None
    for o, a in opts:
        if o in ('-h', '--help'):
            useage()
            return
        if o in ('-o', '--output'):
            output = a

    if len(args) == 0:    
        useage()
        return
    elif len(args) > 1 and output:
        useage()
        return
    
    copyright()
    initTemplates()
    for file in args:
        print 'Processing %s...' % (file, ),
        process(file, output)

        print 'Done'

def initTemplates(template_dir='templates'):
    '''Initialize the global templates dictionary with the files
    located in template_dir'''
    global templates
    directory = os.path.join(os.getcwd(), template_dir)
    # add every file in the directory to the templates dict
    for file in os.listdir(directory):
        if not os.path.isdir(file):
            templates[file] = open(os.path.join(directory, file), 'r').read()
    

def process(file, outfile=None):
    '''Generate the C extension module from the Python module'''
    # imp.load_source wants a file object of the source file
    try:
        fp = open(file, 'r')
    except IOError:
        print 'Error opening file'
        return

    # imp.load_source wants the module name, which is taken as
    # the filename minus the extension
    modname = os.path.splitext(file)[0]
    try:
        module = imp.load_source(modname, file, fp)
    except ImportError:
        print 'Unable to load module'
        return

    fp.close()

    # open the output file
    if outfile:
        fp = open(outfile, 'w')
    else:
        fp = open('%s.c' % (modname, ), 'w')

    # create a module object with the relevant data, and process it
    m = CModule(modname, module, fp)
    m.process()
    

if __name__ == '__main__':
    main()
