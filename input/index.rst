===========
reStInPeace
===========

reStInPeace_ is a little apllication to manage your documents in reStructuredText_ format.

The project has been started in August 2007 as I missed a simple editor from wich I can type and view my output in HTML easily.

It is written in Python_ using the PyQt4_ toolkit.

.. contents::

Licence:
========

reStInPeace_ is under the Gnu GPL 2.0 Licence.

Requirements:
=============

- Python_ > 2.5;

- RiveBank's PyQt4_ toolkit;

- Docutils_ package (SVN version recommanded)

- the DejaVu_ fonts ;

- Pygments_ package for source code colorisation;

- [Optional] The Psyco_ module to speed up some parts of the code;  

Features:
=========

- open/save files your in ``reStructuredText`` format;

- view them inside a pseudo-browser while you type; in this case, you'll have to refresh the view after typing. I've tried the dynamic highlighting witrh poor results.

- sourcecode colorisation inside ``reSTructuredText`` thanks to the Pygments team;

- convert your ``reSTructuredText`` docs in LaTeX, HTML, Lout, OpenOffice with your personnal stylesheets. For the moment, you can't choose them, but it's a planned feature.

- powerfull snippets engine, very TextMate-like ;

- make ``reStructuredText`` grid-tables easily;

Limitations:
============

reStInPeace_ is rather ``strict`` :

- Your reStructuredText_ documents should be UTF-8 encoded.

- They must have a '.txt' or '.rst' extension. I know, the Docutils site tells us to use '.txt', but I find it good to see directly my reSt docs.

- If you use the OpenOffice output, be aware that it does not handle the colorisation the same as the HTML one.

To be done:
===========

- handle several stylesheets;

- chained and nested snippets. For this to work, I've to implement a custom parser, not regexp based;

- better reSt highlighter and (sort-of) CSS stylesheet for the viewer;

Download:
=========

reStInPeace_ is in beta stage, so please don't complain about a missing feature yet. 

No more direct download, the latest sources can be found here with their version number :

`reSTinPeace betas <http://kib2.free.fr/reSTinPeace/betas/>`_

Usage:
======

Launch the programm by typing this line inside the application's directory::

   python reStInPeace.py

+ Type/Load your text in the left part (editor), press the Refresh button to have a view of it on the right side (browser). Save it.

+ Press the conversion dialog button, choose your format, press Process then OK. The output file should be inside the output directory of your application.

+ If you want a real view of your document ie inside FireFox, press the 'See in my default browser' button. 

Thanks and links:
=================

- The Docutils_ team for reSt;

- The new project rst2a_ for their beautifull project and from wich I borrowed their stylesheet (yes, sometimes I'm just cheating, I don't like Web programming very much);

- The Pandoc_ project is young, but very interesting: it lets you convert from one markup format to another; it is implemented in Haskell langage.

- Interpol_'s music has good inspiration influence, I don't know why...maybe I find myself in the past when I'm listening to them :)

Sometimes, I post some news about ideas and development on my 'sort-of' static blog_ engine.  

Screenshots:
============

v0.8
####

The 0.8 beta version, with a new Table creator dialog, using the **F5** key.

The Table dialog in action

.. image:: http://kib2.free.fr/reSTinPeace/RIP2_small.png
    :scale: 100
    :alt: v0.8 screen
    :align: center
    :target: http://kib2.free.fr/reSTinPeace/RIP2.png

The result in the editor and view:

.. image:: http://kib2.free.fr/reSTinPeace/RIP3_small.png
    :scale: 100
    :alt: v0.8 screen
    :align: center
    :target: http://kib2.free.fr/reSTinPeace/RIP3.png

v0.7
####

.. image:: http://kib2.free.fr/reSTinPeace/RIP1_small.png
    :scale: 100
    :alt: v0.7 screen
    :align: center
    :target: http://kib2.free.fr/reSTinPeace/RIP1.png

The older 0.5 version had a very basic snippets support, but it takes me time to get these images so it will stay for some time.
   
v0.5
####

.. image:: http://kib2.free.fr/reSTinPeace/RIPsnippets.gif
   :scale: 100
   :alt: RIPsnippets.gif
   :align: center

ChangeLog:
==========

28.10.2007
##########

- Added a 'French' translation, but I really don't know if it's good enough. It's working on my machine, I'm waiting for your replies;

- Chained snippets are done, but there's some limitations :

  + If there's already a character before the cursor, the snippet won't expand::

      You can i.e chain a title with a bolded characters like this : 
      type 'tit' followed by Tab. Once in the field, type 'bold' 
      followed by Tab. Type your title, then Tab : you're done :)

  + You won't get dynamic updating inside the view.   

- Basic grid tables editing via F5 key highlighting; ``basic`` because rows or columns can't be spaned for the moment.

- Added tables highlighting;

21.10.2007
##########

-   Editor fonts can be choosen by hitinf F4 or via the really ugly Preferences dialog.
-   Added a QSplitter widget between the editor and browser views. Those how don't have a widescreen will certainly appreciate it.
-    The docs (accessible via F1) have been updated, they're now read from a rest file.
-    Fixed a bug inside saveFile();
-    Fixed some translations typos;

16.10.2007
##########

- Snippets have been rewritten from scatch.
- The new engine is more powerfull and has some little tranformations features (not enough time for it yet).
- Snippets are now separated from code, they've got their xml file format inside a Snippets directory. They are read with ElementTree.
- browser.css is getting better, but not perfect :)
- Added 3 shortcuts :

  - F1 : Help
  - F2 : Indent region (taken from the Sandbox project)
  - F3 : Unindent region (idem)

- Added a Save button and shortcut(Ctrl-S);
- Saving mechanism has been reviewed;

Known bugs in the latest version |vnum|:
========================================

Symptom:
########

1. Write a new file; save it via Save button. The file is saved as a blank one;

Status:
#######

1. Not corrected yet (don't want to upload just for this), but you can do it just by searching for  ``actionEnregistrer`` and replace it by ``actionSave`` in the file ``reStInPeace.py``.

.. _Python : http://www.python.org/
.. _Docutils : http://docutils.sourceforge.net/
.. _reStructuredText : http://docutils.sourceforge.net/rst.html
.. _PyQt4 : http://www.riverbankcomputing.co.uk/pyqt/download.php
.. _InType : http://intype.info/home/index.php
.. _InType : http://intype.info/home/index.php
.. _DejaVu : http://dejavu.sourceforge.net/wiki/index.php/Download
.. _PyQt4 : http://www.riverbankcomputing.co.uk/pyqt/download.php
.. _Pygments : http://pygments.org/
.. _reStInPeace : http://kib2.free.fr/reSTinPeace/
.. _rst2a : http://rst2a.com
.. _Pandoc : http://johnmacfarlane.net/pandoc/
.. _Psyco : http://psyco.sourceforge.net/
.. _blog : http://kib2.free.fr/Articles/index.html
.. _Interpol : http://www.interpolnyc.com/

.. |vnum| replace:: 0.7
