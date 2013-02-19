#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Copyright (C) 2007 Christophe Kibleur <kib2@free.fr>
#
# This file is part of reSTinPeace (http://kib2.free.fr).
#
# reSTinPeace is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
#
# reSTinPeace is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# CHANGELOG:[ 2 latest versions only]

# 24.10.2007    -   It is now possible to chain your snippets, 
#                   with one limitation :
#                   - the trigger should be alone
#               -   Try to use the psyco module for better performances. 
#               -   Corrected a little bug inside saveFile. This was a
#                   old named method actionEnregistrer() to be replaced
#                   by actionSave.

# 21.10.2007 :
#               -   Editor fonts can be choosen by hitinf F4 or via
#                   the really ugly Preferences dialog. 
#               -   Added a QSplitter widget between the editor and browser 
#                   views. Those how don't have a widescreen will certainly 
#                   appreciate it.
#               -    The docs (accessible via F1) have been updated, they're
#                   now read from a rest file.
#               -    Fixed a bug inside saveFile();
#               -    Fixed some translations typos;

# 16.10.2007 :  - Snippets have been rewritten from scatch.
#                 The new engine is more powerfull and has some
#                 little tranformations features (not enough time for it yet).
#               - Snippets are now separated from code, they've got their
#                 xml file format inside a Snippets directory. They are read 
#                 with ElementTree.
#               - browser.css is getting better, but not perfect :)
#               - Added 3 shortcuts :
#                   F1 : Help
#                   F2 : Indent region (taken from the Sandbox project)
#                   F3 : Unindent region (idem)
#               - Added a Save button and shortcut(Ctrl-S);
#               - Saving mechanism has been reviewed;

# TODO:
#   - Preserve indentation in snippets

#   - Highlighter dialog;
#   - highlighter and conversion parts needs to be rewritten ;

# IDEAS TO IMPLEMENT:
#   - Review the snippet parser to get nested ones (hard work);
#   - Line numbers (already done in another secret projet);
#   - tables editing facilities;
#   - folding ?

__version__ = "0.8 beta"
__author__ = "Christophe Kibleur"

# build-in modules
import os, sys
import urllib
import string
import re
import xml.etree.cElementTree as ET
from docutils import core

# PyQt specific
from PyQt4 import QtGui, QtCore

# personnal packages
from ui_restester import Ui_MainWindow
from ui_converter import Ui_Converter
from ui_about import Ui_About
from ui_preferences import Ui_preferences
from ui_arraydialog import Ui_ArrayDialog

import highlighter
import RegisterPygment
from SnipEngine import *


def readSnippetsDefs(file):

    """Reads an XML file containing the snippets and
    returns a dictionnary like whose keys are the triggers
    to type, and the values are a 2-uplet(description',snippet).
    """
    templates = {}
    doc = ET.parse(str(file))
    entries = doc.findall("entry")
    for entry in entries:
        templates[entry.find("trigger").text] = (entry.find("description").text, entry.find("snippet").text)
    return templates


# globals
APPLIREP = os.getcwd()
INREP = os.path.join(APPLIREP, "input")
OUTREP = os.path.join(APPLIREP, "output")
SNIPREP = os.path.join(APPLIREP, "Snippets")

# Snippets
DICSNIP = readSnippetsDefs(SNIPREP + "/rest_snippets.xml")

# A QTextBrowser abble to download
# images and put them inside input directory
class imageBrowser(QtGui.QTextBrowser):
    def loadResource(self, type, name):
        url = unicode(name.toString())
        ret = QtCore.QVariant()
        if url.startswith('http://'):
            fname = url.split("/")[-1]
            dn = os.path.expanduser(INREP)
            if not os.path.isdir(dn):
                os.mkdir(dn)
            #fn = dn + "/" + fname
            fn = os.path.join(dn, fname)
            if not os.path.isfile(fn):
                urllib.urlretrieve(url, fn)
            ret = QtGui.QTextBrowser.loadResource(self, type, QtCore.QUrl.fromLocalFile(QtCore.QString(fn)))
        else:
            ret = QtGui.QTextBrowser.loadResource(self, type, name)
        return ret


class MonAppli(QtGui.QMainWindow, Ui_MainWindow):

    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)

        # Configure the user interface.
        self.setupUi(self)

        # Snippets special Variables
            # snippet
        self.insideSnippet = False
        self.start_snip = 0
            # Field courant
        self.snippets = []
        self.field = None
        self.field_start = 0
        self.field_long = 0
        self.oldsnip = None

        # Editor
            # Editor tabs = 4 chars
        self.tab_long = 4
        self.setTabEditorWidth(self.tab_long)
            # Coloration syntaxique
        self.highlighter = highlighter.Highlighter(self.editor)
        self.highlighter.modeRest()

        # Browser (viewer)
            # Set permissions to open external links
            # by clicking on them
        self.viewer.openExternalLinks = True
        self.viewer.setOpenExternalLinks(True)

            # Big Hack not to have to create a particluar
            # classe for the browser.
            # TODO : clean derivation
        self.viewer.loadResource = imageBrowser().loadResource

        ## Special attributes :
            # name of the current edited file
        self.fileName = "Noname.rst"
            # absolute path
        self.filePath = INREP
            # boolean to know if file has been saved or not
        self.isSaved = False
            # default directory
        self.default_dir = INREP # or APPLIREP (up to you)

        ## Conversion Dialog
        self.ConvDialog = QtGui.QDialog(self)
        ui = Ui_Converter()
        ui.setupUi(self.ConvDialog)
        self.converterdial = ui

        ## SIGNALS/SLOTS
            # we need to know if source as changed
        self.connect(self.editor, QtCore.SIGNAL("textChanged()"), self.needSave)

        ## ScrollBars editor-viewer
            # scrollbar editor
        self.esb = self.editor.verticalScrollBar()
            # scrollbar viewer
        self.vsb = self.viewer.verticalScrollBar()
            # connexions scrollbar editor --> synchronise view in browser
        self.connect(self.esb, QtCore.SIGNAL("valueChanged(int) "), self.actualiseBSlider)
            # connexions scrollbar viewer --> synchronise view in editor 
        self.connect(self.vsb, QtCore.SIGNAL("valueChanged(int) "), self.actualiseESlider)

        ## MENU ACTIONS
        self.createActions()

        ## BUTTONS
        self.actionSave.setEnabled(self.isSaved)

        ## APPLY SAVED APP SETTINGS
        self.readSettings()

        ## KEYBOARD SHORTCUTS
        keyTab = QtGui.QShortcut(QtGui.QKeySequence(self.tr("Tab")), self)
        self.connect(keyTab, QtCore.SIGNAL("activated()"), self.whatToDoOnTab)

        QtGui.QShortcut(QtGui.QKeySequence("F1"), self, self.showHelp)
        QtGui.QShortcut(QtGui.QKeySequence("F2"), self, self.indentRegion)
        QtGui.QShortcut(QtGui.QKeySequence("F3"), self, self.unindentRegion)
        QtGui.QShortcut(QtGui.QKeySequence("F4"), self, self.chooseFont)
        QtGui.QShortcut(QtGui.QKeySequence("F5"), self, self.tableCreate)
        QtGui.QShortcut(QtGui.QKeySequence("F6"), self, self.columnMode)


        self.connect(self.editor, QtCore.SIGNAL("textChanged()"), self.updateChilds)

        ## STATUSBAR
        self.statusBar().showMessage("Welcome to reStInPeace, press F1 for Help.")

    ## ------------------------------------------
    ##                  Snippets
    ## 
    ## Methods used by the editor :
    ## 
    ## - insertSnippet
    ## - whatToDoOnTab
    ## - nextField
    ## - endSnip
    ## - updateChilds
    ## ------------------------------------------
    def columnMode(self):
        deb = self.editor.textCursor()
        selection = deb.selectedText()
        lines = unicode(selection).split()
        print lines

        for i in lines :
            c = self.editor.textCursor()
            # on se positionne au debut
            c.movePosition(QtGui.QTextCursor.Down)
            c.insertText(i)
            c.movePosition(QtGui.QTextCursor.Left, len(i))
            self.editor.setTextCursor(c)

        # on repositionne alors le curseur
        self.editor.setTextCursor(deb)
    def insertSnippet(self):
        """ Called from whatToDoOnTab's method
        
        Takes the word before the cursor thanks to wordLeftExtend's
        method and tries to find the word in the snippet dictionary
        DICSNIP.
        
        If so, the snippet is added to the stack and expanded, returning True.
        """
        # r�cup�re le curseur et sa position
        tc = self.editor.textCursor()
        p = tc.position()

        # recup�re le mot le plus � gauche de celui-ci
        word = self.wordLeftExtend(tc)

        # position de depart du snippet
        # [Si on tape en (0,0) le mot 'link', le curseur
        # est alors en pos (4,0). Il faut alors corriger
        # ceci en enlevant la longeur du raccourci tap�.]


        # On essaye de r�cup�rer dans le dico des snippets
        # celui qui correspond au raccourci tap�.
        try:
            # le mot est dans le dico
            tpl = DICSNIP[word][1]
            helptpl = DICSNIP[word][0]
            self.snippet = Snippet(unicode(tpl))
            self.snippet.help = helptpl
            self.snippet.start = p - len(word)
            ##
            self.snippets.append(self.snippet)

            self.snippet.fielditer = self.snippet.fieldIter()
            rendu = self.snippet.expanded()
            self.snippet.long = len(rendu)

            #tc.beginEditBlock()
            self.editor.blockSignals(True)
            tc.insertText(rendu)
            self.editor.blockSignals(False)
            #tc.endEditBlock()

            return True
        except :
            # word is not in DICSNIP
            self.removeSelection()
            return False

    def whatToDoOnTab(self):
        """ Slot called when 'Tab' is pressed.

           - Tries to expand the word before the cursor;
           
           - if return value is True in insertSnippet's method:
                - the snipped has been added to the stack and is expanded,
                  we then go to the next snippet's field, if any.
             
           - if return value is False in insertSnippet's method:
                - if there are already snippets in stack, pass to the next one.
                - if there are no snippet in stack : stop and insert a tab char.
        """
        expanded = self.insertSnippet() # boolean

        if expanded : # if a snippet has been entered previously
            self.nextField()
        else : # the word entered wasn't a shortcut
            if len(self.snippets) > 0:
                self.nextField()
            else:
                self.statusBar().showMessage('insert spaces as no more snippet in stack %s' % (self.snippets))
                self.editor.textCursor().insertText(" "*self.tab_long)

    def nextField(self):

        try: # to go to next field
            self.field = self.snippet.fielditer.next()
            self.snippet.current_field = self.field

            self.field.start = self.snippet.getFieldPos(self.field)
            self.field.long = self.field.getLengh()
            self.statusBar().showMessage('Field=%s--Snippet=%s--Start=%s--Long=%s' % (self.field.code, self.snippet, self.field.start, self.field.long))
            self.selectFromTo(self.snippet.start + self.field.start, self.field.long)

            if self.field.isEnd:
                self.endSnip()
        except :
            self.statusBar().showMessage('ds nextField %s %s' % (self.snippet, self.snippet.current_field))


    def endSnip(self):
        self.removeSelection()
        if len(self.snippets) < 1:
            self.snippets = []
            return

        oldval = self.snippet.expanded()
        self.snippets.pop() # the old snippet
        self.snippet = self.snippets[-1] # new snippet= last entry
        self.field = self.snippet.current_field
        self.updateChilds(given=oldval)
        self.whatToDoOnTab()

    def updateChilds(self, given=None):
        """ Slot called when textarea is modified.
        """
        if len(self.snippets) > 0:
            ## curseur
            c = self.editor.textCursor()
            cursor_pos = c.position()

            ## variables utiles
            # pos de depart du snippet
            debut_snip = self.snippet.start
            old_long = self.snippet.long
            # le champ
            f = self.snippet.current_field

            # le nbr d'esclaves
            nslaves = len(f.slaves)
            # la valeur de l'ancien champ (si existence)
            old_field_val = f.content
            # l'ancien champ
            self.oldfield = f

            ## Capture le texte du champ actuel
            # l'affiche dans la statusbar
            newpos = c.selectionStart()
            #c.setPosition(debutsnip+st, QtGui.QTextCursor.MoveAnchor)
            c.setPosition(self.field.start + self.snippet.start, QtGui.QTextCursor.MoveAnchor)
            c.setPosition(cursor_pos, QtGui.QTextCursor.KeepAnchor)
            if not given :
                self.exp = c.selectedText()
            else:
                self.exp = given
            self.statusBar().showMessage("Field %s replaced by '%s'" % (f.code, unicode(self.exp)))

            ## Selectionne et remplace le snippet

            # update du champ avec la valeur calculee
            f.content = unicode(self.exp)

            # nouveau contenu du snippet
            cont = self.snippet.expanded()

            # self.snip_long est l'ancienne longueur
            offset = len(f.content) - len(old_field_val)
            self.selectFromTo(self.snippet.start, self.snippet.long + offset)
            #time.sleep(1)

            # on update la longueur du snippet
            self.snippet.long = len(cont)

            # On doit faire attention a bloquer
            # l'emission du signal
            self.editor.blockSignals(True)
            self.editor.textCursor().insertText(cont)
            self.editor.blockSignals(False)

            # Should I prefer this one-liner ?
            #self.selectFromTo(self.start_snip+f.start+len(self.exp), 0)

            c = self.editor.textCursor()
            c.setPosition(self.field.start + self.snippet.start + len(self.exp))
            self.editor.setTextCursor(c)

    ## ------------------------------------------
    ## Editor's functions
    ## ------------------------------------------
    # Find the word before the cursor and select it
    def wordLeftExtend(self, my_cursor):
        """ Recup�re le mot le plus � gauche
            d'un curseur donn� et le s�lectionne.
        """
        oldpos = my_cursor.position()

        # manips curseur
        my_cursor.select(QtGui.QTextCursor.WordUnderCursor)
        #self.editor.setTextCursor(my_cursor)

        newpos = my_cursor.selectionStart()

        my_cursor.setPosition(newpos, QtGui.QTextCursor.MoveAnchor)
        my_cursor.setPosition(oldpos, QtGui.QTextCursor.KeepAnchor)
        self.editor.setTextCursor(my_cursor)
        return str(my_cursor.selectedText())

    def showCursorPos(self):
        tc = self.editor.textCursor()
        self.statusBar().showMessage("Position: %s" % (tc.position()))

    # selectionne le texte de pos � pos + nbr_car
    def selectFromTo(self, pos, nbr_car) :
        """ Selectionne la partie de texte comprise
            entre pos et pos + nbr_car
        """
        #print "Je dois Selectionner de ", pos," a ",lon
        c = self.editor.textCursor()
        # on se positionne au debut
        c.setPosition(pos)
        # on va vers la droite de nbr_car caract�res
        c.movePosition(QtGui.QTextCursor.Right, QtGui.QTextCursor.KeepAnchor, nbr_car)
        # on repositionne alors le curseur
        self.editor.setTextCursor(c)

    # enleve toute selection
    def removeSelection(self):
        """ Enleve la selection et deplace le
            curseur � la fin de celle-ci.
        """
        p = self.editor.textCursor().position()
        self.selectFromTo(p, 0)

    ## ------------------------------------------
    ## Nombre de caract�res maximum sur une ligne
    ## ------------------------------------------
    def setTabEditorWidth(self, tw):
        e = self.editor
        e.setTabStopWidth(e.fontMetrics().width("x") * tw)

    ## Sliders verticaux
    def actualiseBSlider(self, val_ed):
        # Essaye d'actualiser le scrolling du Browser
        # de fa�on proportionnelle � celui de l'
        # �diteur.
        #
        # val est la valeur du slider de l'editeur
        val_view = self.vsb.sliderPosition()

        max_ed = self.esb.maximum()
        max_view = self.vsb.maximum()

        prop_ed = float(val_ed) / float(max_ed)
        prop_view = float(val_view) / float(max_view)

        if not (prop_ed - 0.01 <= prop_view <= prop_ed + 0.01):
            self.vsb.setSliderPosition(prop_ed * max_view)

    def actualiseESlider(self, val_view):
        val_ed = self.esb.sliderPosition()

        max_ed = self.esb.maximum()
        max_view = self.vsb.maximum()

        prop_ed = float(val_ed) / float(max_ed)
        prop_view = float(val_view) / float(max_view)

        if not (prop_view - 0.01 <= prop_ed <= prop_view + 0.01):
            self.esb.setSliderPosition(prop_view * max_ed)

    def newFile(self, path=""):
        """ Create a new reSTructuredText file UTF-8 encoded
        """
        if self.isSaved :
            self.editor.clear()
            self.fileName = "Noname.rst"
            self.filePath = INREP
            self.isSaved = False
            self.toBrowser()
            self.actionSave.setEnabled(self.isSaved)
            self.actionSaveAs.setEnabled(self.isSaved)
        else:
            self.Attention("Your document has not yet been saved, please save it before !")
            #self.saveFile()

    def openFile(self, path=""):
        """ Open a reSTructuredText file UTF-8 encoded
        """

        fileName = QtCore.QString(path)

        if fileName.isEmpty():
            fileName = QtGui.QFileDialog.getOpenFileName(self, self.tr("Open the file"), self.default_dir, "reST Files (*.rst *.txt )")
        codec = QtCore.QTextCodec.codecForName("UTF-8")
        if not fileName.isEmpty():
            # le nom du fichier brut
            self.fileName = str(QtCore.QFileInfo(fileName).fileName())
            self.filePath = str(QtCore.QFileInfo(fileName).path())
            self.editor.clear()
            # update de la statusbar
            self.statusBar().showMessage('File %s has been loaded correctly.' % (self.fileName))

            inFile = QtCore.QFile(fileName)
            #print inFile.fileName()
            if inFile.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text):
                data = QtCore.QTextStream(inFile)
                data.setAutoDetectUnicode(True)
                data.setCodec(codec)
                self.decodedStr = data.readAll()
                self.editor.setPlainText(self.decodedStr)
        self.isSaved = True
        self.toBrowser()
        self.actionSave.setEnabled(self.isSaved)
        self.actionSaveAs.setEnabled(self.isSaved)

    def saveFileAs(self):
        """ Save actual file in default dir
        """

        fileName = QtGui.QFileDialog.getSaveFileName(self, self.tr("Save the file as..."), self.filePath, "reST Files (*.rst *.txt )")
        if not fileName.isEmpty():
            outFile = QtCore.QFile(fileName)
            if not outFile.open(QtCore.QFile.WriteOnly):
                print "A problem has occured with your file..."
                return
            out = QtCore.QTextStream(outFile)
            out.setCodec("UTF-8")
            out << self.editor.toPlainText()
            # update de self.filename :
            self.fileName = QtCore.QFileInfo(outFile).fileName()
            # update de la statusbar
            self.statusBar().showMessage('File %s has been saved correctly.' % (self.fileName))

            # flag de sauvegarde
            self.isSaved = True
            self.actionSave.setEnabled(self.isSaved)

    # Why reinvent the wheel ? It has been taken and adapted from M.Summerfield's demo
    def saveFile(self):
        fp = self.filePath + '/'
        if self.fileName == "Noname.rst":
            self.saveFileAs()
            return
        if QtCore.QFile.exists(self.fileName):
            backup = self.fileName + '.rst_old'
            ok = True
            if QtCore.QFile.exists(fp + backup):
                ok = QtCore.QFile.remove(fp + backup)
                if not ok:
                    QtGui.QMessageBox.information(self, "reSTinPeace - Save Warning",
                            "Failed to remove the old backup %s")
            if ok:
                # Must use copy rather than rename to preserve file
                # permissions; could use rename on Windows though
                if not QtCore.QFile.copy(fp + self.fileName, fp + backup):
                    QtGui.QMessageBox.information(self, "reSTinPeace - Save Warning",
                            "Failed to save a backup %s")

        try:
            try:
                fh = QtCore.QFile(fp + self.fileName)
                if not fh.open(QtCore.QIODevice.WriteOnly):
                    raise IOError, unicode(fh.errorString())
                stream = QtCore.QTextStream(fh)
                stream.setCodec("UTF-8")
                stream << self.editor.toPlainText()
                self.editor.document().setModified(False)
                self.setWindowModified(False)
                self.setWindowTitle("reSTinPeace - %s[*]" % \
                        QtCore.QFileInfo(fp + self.fileName).fileName())
                self.statusBar().showMessage("Saved %s" % self.fileName,
                        5000)
                self.isSaved = True
            except (IOError, OSError), e:
                QtGui.QMessageBox.warning(self, "reSTinPeace - Save Error",
                        "Failed to save %s: %s" % (fp + self.fileName, e))
        finally:
            if fh is not None:
                fh.close()
        return True

    def toBrowser(self):
        """ Transforme le texte de l'editeur en HTML
            pour le voir dans la partie browser.
        """
        self.viewer.document().setDefaultStyleSheet(open(os.getcwd() + "/browser.css", "r").read())
        sortie = core.publish_string(unicode(self.editor.document().toPlainText()).encode("utf-8"),
                writer_name='html',
                settings_overrides={'input_encoding': 'utf-8',
                                    'output_encoding': 'latin-1',
                                    'language': 'en',
                                    },
                            )
        self.viewer.setSearchPaths([os.path.expanduser(self.filePath)])
        self.viewer.setHtml(sortie)

    def showConverterDialog(self):
        """ Affiche le dialogue de conversion
        """
        self.ConvDialog.show()
        self.connect(self.converterdial.but_process, QtCore.SIGNAL("clicked()"), self.processOutput)

    def processOutput(self):
        """ Transforme l'entree au format demand�
        """

        dic_formats = {'(X)HTML': ('to_html', 'css'),
                        'LaTeX' : ('to_tex', 'sty'),
                        'OpenOffice' : ('to_odt', 'odt'),
                        'Lout' : ('to_lout', 'lout'),
                        }
        dial = self.converterdial
        format = dic_formats[str(dial.combo_out.currentText())][0]

        opt = ''
        if format == 'to_odt' :
            opt = ' --add-syntax-highlighting '

        Tstylesheet = OUTREP + "/default." + dic_formats[str(dial.combo_out.currentText())][1]
        extension = "." + format[3:]
        format += ".py"

        cmd = string.Template('python ${to_format} %s --stylesheet-path=${stylesheet} --language=en "${restfile}" "${outfile}"' % (opt))


        out_file = OUTREP + "/" + self.fileName[:-4] + extension

        # raccourci pour la commande lanc�e
        text_cmd = cmd.substitute(to_format=format,
                                  stylesheet=Tstylesheet,
                                  restfile=self.filePath + "/" + self.fileName,
                                  outfile=out_file)

        if format == 'to_lout.py' :
            cmd = string.Template('python ${to_format} %s --language=fr "${restfile}" "${outfile}"' % (opt))
            text_cmd = cmd.substitute(to_format=format,
                                  restfile=self.filePath + "/" + self.fileName,
                                  outfile=out_file)
        # debbuging :
        print text_cmd

        # lance la commande syst�me
        try:
            os.popen2(text_cmd)
            self.statusBar().showMessage('Command :  "%s"' % (text_cmd))
        except:
            self.statusBar().showMessage('Command failed')

        # update de la statusbar
        self.statusBar().showMessage('Command :  "%s"' % (text_cmd))

        # Ouvre t-on le document le document dans
        # le navigateur par d�faut ?
        # self.askIfShowInDefaultBrowser(html_file)

    def showInWB(self):
        html_file_name = OUTREP + "/" + self.fileName[:-4] + '.html'
        if os.path.isfile(html_file_name) :
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(html_file_name))
        else :
            self.Attention("You don't have converted your document to HTML yet.")
        return

    def Attention(self, mess):
        message = QtGui.QMessageBox(self)
        message.setText(mess)
        message.setWindowTitle('Attention')
        message.setIcon(QtGui.QMessageBox.Warning)
        message.addButton('Ok', QtGui.QMessageBox.AcceptRole)
        message.exec_()

    def askIfShowInDefaultBrowser(self, name):
        """ Demande � l'utilisateur s'il veut visualiser
            la sortie dans son navigateur par d�faut.
        """
        reply = QtGui.QMessageBox.question(self, 'Message',
            "Do you want to view your document in your default browser ?", QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.Yes:
            QtGui.QDesktopServices.openUrl(QtCore.QUrl.fromLocalFile(name))
        else:
            return

    def closeEvent(self, event):
        if self.isSaved or self.editor.toPlainText() == "":
            self.writeSettings()
            message = QtGui.QMessageBox(self)
            message.setText('Are you sure you want to quit reStInPeace ?')
            message.setWindowTitle('reSTinPeace')
            message.setIcon(QtGui.QMessageBox.Question)
            message.addButton('Yes', QtGui.QMessageBox.AcceptRole)
            message.addButton('No', QtGui.QMessageBox.RejectRole)
            message.exec_()
        else:
            self.Attention("Your document has not yet been saved, please save it before !")

    def needSave(self):
        self.isSaved = False
        self.actionSave.setEnabled(True)
        self.actionSaveAs.setEnabled(True)
        self.setWindowTitle("reSTinPeace %s -- File :%s* -- Directory: %s " \
                            % (__version__,
                            self.fileName,
                            self.filePath,
                            ))

    def showPrefs(self):
        """ Preferences dialog
        """
        Dialog = QtGui.QDialog(self)
        ui = Ui_preferences()
        ui.setupUi(Dialog)
        Dialog.show()
        self.connect(ui.editorFontButton, QtCore.SIGNAL('clicked()'), self.chooseFont)

    def showAbout(self):
        """ Dialogue a propos
        """
        Dialog = QtGui.QDialog(self)
        ui = Ui_About()
        ui.setupUi(Dialog)
        Dialog.show()

    ## Application Settings
    def readSettings(self):
        # lire les settings
        settings = QtCore.QSettings("Kib", "reSTinPeace")
        pos = settings.value("pos", QtCore.QVariant(QtCore.QPoint(200, 200))).toPoint()
        size = settings.value("size", QtCore.QVariant(QtCore.QSize(600, 400))).toSize()
        #textSize = settings.value("pointSize", 12).toInt()

        # applique les settings
        self.resize(size)
        self.move(pos)

    def writeSettings(self):
        # ecrire les settings
        settings = QtCore.QSettings("Kib", "reSTinPeace")
        settings.setValue("pos", QtCore.QVariant(self.pos()))
        settings.setValue("size", QtCore.QVariant(self.size()))

    def afficheMessage(self, mess):
        self.statusBar().showMessage(mess)

    def createActions(self):
        # actions du menu et raccourcis clavier

        # Ouvrir un fichier
        self.actionOpen.setShortcut(self.tr("Ctrl+O"))
        QtCore.QObject.connect(self.actionOpen,
            QtCore.SIGNAL("triggered()"),
            self.openFile)

        # Nouveau fichier
        self.actionNew.setShortcut(self.tr("Ctrl+N"))
        QtCore.QObject.connect(self.actionNew,
            QtCore.SIGNAL("triggered()"),
            self.newFile)

        # Enregistrer fichier
        self.actionSaveAs.setShortcut(self.tr("Ctrl+Alt+S"))
        QtCore.QObject.connect(self.actionSaveAs,
            QtCore.SIGNAL("triggered()"),
            self.saveFileAs)

        # Enregistrer sous fichier
        self.actionSave.setShortcut(self.tr("Ctrl+S"))
        QtCore.QObject.connect(self.actionSave,
            QtCore.SIGNAL("triggered()"),
            self.saveFile)

        # Rafraichir le browser
        self.actionRefresh.setShortcut(self.tr("Ctrl+R"))
        QtCore.QObject.connect(self.actionRefresh,
            QtCore.SIGNAL("triggered()"),
            self.toBrowser)

        # Dialogue de pr�f�rences
        self.actionSettings.setShortcut(self.tr("Ctrl+Alt+P"))
        QtCore.QObject.connect(self.actionSettings,
            QtCore.SIGNAL("triggered()"),
            self.showPrefs)

        # Dialogue a propos
        QtCore.QObject.connect(self.actionAbout,
            QtCore.SIGNAL("triggered()"),
            self.showAbout)

        # Dialogue a propos
        QtCore.QObject.connect(self.actionHelp,
            QtCore.SIGNAL("triggered()"),
            self.showHelp)

        # Voir dans le navigateur par defaut
        self.actionSeeInDefaultBrowser.setShortcut(self.tr("Ctrl+Alt+V"))
        QtCore.QObject.connect(self.actionSeeInDefaultBrowser,
            QtCore.SIGNAL("triggered()"),
            self.showInWB)

        # Appelle le dialogue de conversion en HTML, LaTeX, etc.
        self.actionConversionDialog.setShortcut(self.tr("Ctrl+Alt+C"))
        QtCore.QObject.connect(self.actionConversionDialog,
            QtCore.SIGNAL("triggered()"),
            self.showConverterDialog)

        # Quitter l'application
        self.actionQuit.setShortcut(self.tr("Ctrl+Alt+Q"))
        QtCore.QObject.connect(self.actionQuit,
            QtCore.SIGNAL("triggered()"),
            QtGui.qApp, QtCore.SLOT('quit()'))

    def chooseFont(self):
        font, ok = QtGui.QFontDialog.getFont(self.editor.font())
        if ok:
            self.editor.setFont(font)


    # Internationalisation taken from PyQt4 demo
    def findQmFiles(self):
        trans_dir = QtCore.QDir(APPLIREP + "/translations")
        fileNames = trans_dir.entryList(QtCore.QStringList("*.qm"), QtCore.QDir.Files, QtCore.QDir.Name)

        for i in fileNames:
            fileNames.replaceInStrings(i, trans_dir.filePath(i))

        return fileNames

    def languageName(self):
        files = self.findQmFiles()
        translator = QtCore.QTranslator()
        translator.load(files[0])

        QtGui.qApp.installTranslator(translator)
        translator.translate("MonAppli", "en_US")
        return

    def showHelp(self):
        """Shows a Help dialog that can be closed by 'Esc' key.
        """
        h = HelpForm(parent=self)
        h.show()


    def addEditorMethod(self, methodname):
        #self.editor.methodname = methodname
        setattr(self.editor, method.__name__, method)

    ## This part of code has been taken and adapted 
    ## from Sanbox thanks to Mark Summerfield for the GPL 2.0 licence.

    def indentRegion(self):
        self._walkTheLines(True, " " * self.tab_long)

    def unindentRegion(self):
        self._walkTheLines(False, " " * self.tab_long)

    def _walkTheLines(self, insert, text):
        userCursor = self.editor.textCursor()
        userCursor.beginEditBlock()
        start = userCursor.position()
        end = userCursor.anchor()
        if start > end:
            start, end = end, start
        block = self.editor.document().findBlock(start)
        while block.isValid():
            cursor = QtGui.QTextCursor(block)
            cursor.movePosition(QtGui.QTextCursor.StartOfBlock)
            if insert:
                cursor.insertText(text)
            else:
                cursor.movePosition(QtGui.QTextCursor.NextCharacter,
                        QtGui.QTextCursor.KeepAnchor, len(text))
                if cursor.selectedText() == text:
                    cursor.removeSelectedText()
            block = block.next()
            if block.position() > end:
                break
        userCursor.endEditBlock()


    def tableCreate(self):
        """ This function creates a QTableWidgetItem out of a 2-dimension nested list which contains numbers, and then uses it to "paint" the someTbl object, which is a QTableWidget """
        dial = QtGui.QDialog(self)
        dial.setWindowTitle("Table creator")
        self.tabledialog = dial
        self.tbl_dial = Ui_ArrayDialog()
        self.tbl_dial.setupUi(dial)


        #ArrayDialog.show()
        tbl = self.tbl_dial.tableWidget
        col = self.tbl_dial.spinBoxColumns
        lin = self.tbl_dial.spinBoxRows
        but = self.tbl_dial.okButton

        # Connexions
        self.connect(col, QtCore.SIGNAL("valueChanged(int)"), self.actualiseTable)
        self.connect(lin, QtCore.SIGNAL("valueChanged(int)"), self.actualiseTable)
        #dial.connect(but, QtCore.SIGNAL("cliked()"), self.insertRestTable)
        QtCore.QObject.connect(but, QtCore.SIGNAL("clicked()"), self.insertRestTable)
        tbl.setColumnCount(col.value())
        tbl.setRowCount(lin.value())

        dial.show()

    def actualiseTable(self, int_number):
        tbl = self.tbl_dial.tableWidget
        col = self.tbl_dial.spinBoxColumns
        lin = self.tbl_dial.spinBoxRows

        tbl.setColumnCount(col.value())
        tbl.setRowCount(lin.value())

    def insertRestTable(self):
        lines = self.tbl_dial.tableWidget.rowCount()
        cols = self.tbl_dial.tableWidget.columnCount()
        mylist = []
        for col in range(cols) :
            poorlist = []
            for line in range(lines) :
                try :
                    text = self.tbl_dial.tableWidget.item(line, col).text()
                except:
                    text = ''
                truc = unicode(text)
                poorlist.append(truc)
            mylist.append(poorlist)
        self.traiteListe(mylist)
        self.tabledialog.close()

    def traiteListe(self, laliste):
        # see new changes in Python 2.5 max function
        # http://www.onlamp.com/pub/a/python/2006/10/26/python-25.html?page=3
        output = []

        def myord(astr):
            return len(astr)

        nbr_lines = len(laliste[0])
        for lin in range(nbr_lines):
            textcell, deco = [], []

            for col in laliste:
                largeur = len(max(col, key=myord))
                spaces = largeur - len(col[lin])
                if lin == 1:
                    deco.append('+' + (largeur + 2) * '=')
                else:
                    deco.append('+' + (largeur + 2) * '-')
                textcell.append("| " + col[lin] + (spaces + 1) * " ")
            deco.append("+")
            textcell.append("|")
            #print "".join(deco)
            #print "".join(koala)
            output.append("".join(deco))
            output.append("".join(textcell))
        output.append(output[0])

        c = self.editor.textCursor()
        c.insertText("\n".join(output))
        self.toBrowser()

class HelpForm(QtGui.QDialog):

    def __init__(self, parent=None):
        super(HelpForm, self).__init__(parent)
        #self.setAttribute(Qt.WA_GroupLeader)
        #self.setAttribute(Qt.WA_DeleteOnClose)
        browser = QtGui.QTextBrowser()
        browser.setOpenExternalLinks(True)
        browser.document().setDefaultStyleSheet(open(os.getcwd() + "/browser.css", "r").read())
        myhelp = open(APPLIREP + "/input/rip_help.rst", 'r').read()
        sortie = core.publish_string(myhelp,
                writer_name='html',
                settings_overrides={'input_encoding': 'utf-8',
                                    'output_encoding': 'latin-1',
                                    'language': 'fr',
                                    },
                            )
        #browser.setSearchPaths([os.path.expanduser(self.filePath)])
        browser.setHtml(self.tr(sortie))

        layout = QtGui.QVBoxLayout()
        layout.setMargin(0)
        layout.addWidget(browser)
        self.setLayout(layout)
        self.resize(600, 500)
        QtGui.QShortcut(QtGui.QKeySequence("Escape"), self, self.close)
        self.setWindowTitle("reStInPeace - Help")

def main():
    app = QtGui.QApplication(sys.argv)
    ## Change le look de l'appli
    QtGui.QApplication.setStyle(QtGui.QStyleFactory.create("Cleanlooks"))
    ## et la palette correspondante
    QtGui.QApplication.setPalette(QtGui.QApplication.style().standardPalette())

    ## Translation process
    locale = QtCore.QLocale.system().name()
    qtTranslator = QtCore.QTranslator()
    if qtTranslator.load("qt_" + locale):
        app.installTranslator(qtTranslator)
    appTranslator = QtCore.QTranslator()
    if appTranslator.load("reStInPeace_" + locale):
        app.installTranslator(appTranslator)

    window = MonAppli()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()

