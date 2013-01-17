'''This module manages plugins and macro code. The difference is that
macros are loaded dynamically and plugins are loaded from files. Macros tend
to be shorter snippets executed once while plugins are loaded into memory and
interact with the core.'''

import sys, traceback

class PluginManager(object):
  def __init__(self, window):
    self.window = window
  
  def LoadPlugin(self, pluginName):
    '''Load a Python plugin. It needs to be on the path (ie: in the plugins dir)
    A plugin is simply a module with a setup function. Variables are set in the module
    for the view, config, eventBus, actions list and pluginManager before setup
    is called'''
    try:
      plugin = self.MyImport(pluginName)
      print "-" * 40 + "\n\nLoaded %s successfuly" % pluginName
    except:
      traceback.print_exc()
      print "-" * 40 + "\n\nError Loading %s" % pluginName
      return
    plugin.window = self.window
    plugin.editor = self.window.editor
    plugin.pluginManager = self
    #plugin.config = self.pallavi.config
    #plugin.eventBus = self.pallavi.eventBus
    #plugin.actions = self.pallavi.actions
    plugin.setup()
    #setattr(self.editor,method.__name__,method) 
    
  def LoadPlugins(self, pluginList):
    '''Load a list of plugins. The list should be of names of python modules in
    the path (normally the plugins dir).'''
    for plugin in pluginList:
      self.LoadPlugin(plugin)

  def LoadDefaultPlugins(self, pluginList):
    '''Load a list of plugins. The list should be names of python modules in the
    pallavi.plugins directory. For example, to load the plugin
    pallavi.plugins.Default_Keybinding, the list should contain 'Default_Keybinding';
    the prefix will be prepended automatically.'''
    newlist = []
    for plugin in pluginList:
      newlist.append("pallavi.plugins." + plugin)
    self.LoadPlugins(newlist)
      
  def MyImport(self, name):
    '''Borrowed from python tutorial, does basic importing, I believe'''
    #name = "plugins/" + name
    mod = __import__("plugins/" + name)
    components = name.split('.')
    for comp in components[1:]:
      mod = getattr(mod, comp)
      print "module=", mod
    return mod
    
pm = PluginManager(None)
pm.MyImport("essai")
