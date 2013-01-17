===========
reStinPeace
===========

Typing `reStructuredText <http://docutils.sourceforge.net/rst.html>`_  texts may sometimes be long and fastidious.
`reStinPeace <http://kib2.free.fr/reSTinPeace/>`_ was made to tackle this point by giving you some nice features for editing `reStructuredText <http://docutils.sourceforge.net/rst.html>`_  files.

It uses the Qt4 toolkit coupled with the Python langage to accomplish these tasks:

* some keyboard shortcuts to view/refresh/save/load your `reStructuredText <http://docutils.sourceforge.net/rst.html>`_  files;

* export your `reStructuredText <http://docutils.sourceforge.net/rst.html>`_ docs to HTML+CSS, LaTeX, OpenOffice and Lout. The OpenOffice one needs a special package rst2odt, made by Dave Kuhlman. type ``rst2odt`` in a search engine for this...

* indent/dedent parts of text easily with the respectives keys **F2** and **F3**, and some (I have to write it, really) help with the **F1** key;

* a browser view : thanks to QTextEdit widget, it supports some sort of CSS-like syntax, but it's also difficult to handle correctly; maybe I shoud use the new Webkit project ?

* an original way to synchronise the editor and browser views by moving the editor slidebar with the mouse cursor (not the mouse wheel for the moment). The synchronisation is made proportionnaly;

* you can change the browser font size with Ctrl-mouse wheel;

* a basic `reStructuredText <http://docutils.sourceforge.net/rst.html>`_  highlighter in the editor;

* finally, a brand new snippets engine witch lets you type i.e only 3 letters to obtain a nice `reStructuredText <http://docutils.sourceforge.net/rst.html>`_  title. Try-it yourself, type "tit" then press the **TAB** key.

`reStinPeace <http://kib2.free.fr/reSTinPeace/>`_ is in an early development stage. I've given some of my time for it, and I offer it for free. But if you really want to give something, please give some time to beautify our planet, or if you really want to go for money, then give it to free software associations how really needs it to survive.

For the first time in my life, I'm really proud of some parts of my program : not only because they work quite well, but because I'm the real conceptor of them.

Particulary the snippets engine took me a while to implement. All the implementations I saw before were based on calculus about fields indexes, and so on...Naturally, `reStinPeace <http://kib2.free.fr/reSTinPeace/>`_ has to calculate some things, but not a lot compared to the other implementations I saw. I get the idea while sleeping, so maybe I should sleep more to get new fresh. 
 

As you want more (like transformations on snippets), the calculus grows and you finally get lost in your code.


I can talk about it because it's in fact my 3rd or 4th snippets engine. I started with a project in wxPython called ``WxSnip``, build a basic editor based on it. Then I switched to commercial ones : InType, eTextEditor...all TextMate clones ! But as they advance, their developpement seems to go slower now. I've decided to implement my own text editor, with full snippets support, line numbers, custom syntax highlighting and maybe some folding...but it's just another story starting.


reStinPeace was first developped on Windows XP, I recently switched to Ubuntu's Gutsy distribution so major improvements have been made on Linux based system where bugs have been found. Now, it works very well on my machine, please let me now if Mac users can test it.

Limitations
-----------

- snippets can't be chained (you can't use snippets inside snippets). Believe it or not : it's not as easy as it seems. TextMate, InType or eTextEditor don't have that feature too. I'll try to do my best for it, but I just can't promise anything.

- snippets definitions can't be nested. It's a parser problem, but if you already worked with regular expressions before, you should know the common problems with nested structures. Maybe one day I'll rewrite the parser, but this one is so nice (one magic line of Python code !).

See you, and have a good time with reStinPeace !

*Don't forget to write me if you see a bug or a missing feature* at  kib2@free.fr


 

 




