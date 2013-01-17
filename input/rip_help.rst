===========================
Help file for reStInPeace :
===========================
.. contents::

Things to be aware of with reStInPeace:
=======================================

reStInPeace needs :
-------------------

- version 2.5.1 of Python or better (ElementTree is now included in the Python distribution). 

- a recent version of docutils (the svn one is recommended).

- the "DejaVu Sans Mono" fonts, there are nice and free. You'll find them here : `DejaVu fonts <http://dejavu.sourceforge.net/wiki/index.php/Download>`_ . 

- If you want to use the OdtWriter translator for OpenOffice, go to http://www.rexx.com/~dkuhlman/odtwriter.html to have an idea of it and get the files from Dave Kuhlman here : http://www.rexx.com/~dkuhlman/odtwriter-1.1a.tar.gz. 

- There's a Lout decoder, but it's an old one...maybe someone could be intersted in writing a new fresh one ?

- Beware that all your reSt files are UTF-8 encoded.


Shortcuts
=========
 
- **F1** Show the help dialog. 
- **F2** Indent selected text. 
- **F3** Unindent selected text.
- **F4** Choose editor's fonts.
- **F5** Basic grid table creator.
- **Ctrl+R** Refresh the browser view 
- **Ctrl+S** Open a file 
- **Ctrl+S** Save the current file 
- **Ctrl+Alt+S** Save As...the current file 
- **Ctrl+Alt+P** Preferences dialog (really ugly for the moment, sorry) 
- **Ctrl+Alt+V** View in default browser (you first need to save your file before) 
- **Ctrl+Alt+C** Show the conversion dialog 
- **Ctrl+Alt+Q** Quit
 
Snippets:
=========

Typing one of those texts followed by the Tab key will get you in Snippets mode. Once a snippet is activated, use Tab to go to the next field until the snippet end.

- tit --> title of your document 
- t1 --> header level 1 
- t2 --> header level 2 
- t3 --> header level 3 
- link --> A link without reference 
- lit --> A litteral text 
- con --> Contents 
- bold --> A bolded text 
- ita --> Italic text 
- inter --> Interpreted text 
- im --> To include an image 
- ref --> Reference 
- pref --> Phrase Reference 
- ano --> Anonymous Target 
- sr --> Substitution Reference 
- iit --> Inline Internal Target 
- sc --> Source code 
- rip --> reStinPeace 
- rest --> reStructuredText

Write your own snippets:
========================

Snippets are templates that expands text and automates a lot of what could otherwise be repetitive typing. To insert a snippet, write the 'trigger' word and press the Tab key.

Appart from text, snippets may take 3 placeholders types :
 
- ``${number:default_value}``  is a master placeholder. Once in it, you can choose the default value by pressing Tab or write the one you want, followed by Tab to go to the next one.
 
- ``$number`` is a slave placeholder. It's value is the same as its numbered father.

- ```$0`` is a special placeholder. It has no value, it is the cursor position when the snippet ends.
 
- ``${number/regexp/python code}}`` is a trafo placeholder, and is an hard beast ! First, you specify wich placeholder is the father by giving it a reference number. Then, you'll have to giev a Python regexp that matches something inside the father's contents. If that catches, you can transform the father's contents with whatever Python code you want. You can use special variables inside :

    - PAT : is the pattern matched against the father's contents. 
    - EXP : is the whole father's contents.

.. Attention:: this is not safe has you can make whatever you want inside those fields ! I just used the Python's eval functionality.

customizing reStinPeace: 
=========================

For the moment, reStinPeace has poor support for customisation.
You can change the editor's fonts by pressing F4, and edit the two CSS files default.css (in the application's directory), and browser.css wich is not a real CSS files but Qt4 sort of.

.. Attention:: These files are not real CSS ! For their complete description, please consult the Qt4 docs here :`CSS Propreties <http://doc.trolltech.com/4.3/richtext-html-subset.html>`_ at the bottom of the page.

Bugs/Suggestions:
=================

If you find a bug or have some suggestions to improve reStInPeace, please mail me at kib2@free.fr and give a good description of what you did. 
