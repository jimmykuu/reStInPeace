# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/kib/Public/reStInPeace/reStInPeace0.9/ui_files/ui_restester.ui'
#
# Created: Wed Oct 24 20:38:07 2007
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,800,673).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/new/prefix1/icones/crayon.svg"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.vboxlayout = QtGui.QVBoxLayout(self.centralwidget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setObjectName("hboxlayout")

        self.label = QtGui.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.hboxlayout.addWidget(self.label)

        self.label_2 = QtGui.QLabel(self.centralwidget)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.hboxlayout.addWidget(self.label_2)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.editor = QtGui.QTextEdit(self.centralwidget)

        palette = QtGui.QPalette()

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(255,255,255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(0,0,0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive,QtGui.QPalette.Base,brush)

        brush = QtGui.QBrush(QtGui.QColor(113,113,113))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Text,brush)

        brush = QtGui.QBrush(QtGui.QColor(226,226,226))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled,QtGui.QPalette.Base,brush)
        self.editor.setPalette(palette)

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        self.editor.setFont(font)
        self.editor.setAcceptRichText(False)
        self.editor.setObjectName("editor")
        self.hboxlayout1.addWidget(self.editor)

        self.viewer = QtGui.QTextBrowser(self.centralwidget)

        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        self.viewer.setFont(font)
        self.viewer.setObjectName("viewer")
        self.hboxlayout1.addWidget(self.viewer)
        self.vboxlayout.addLayout(self.hboxlayout1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,800,21))
        self.menubar.setObjectName("menubar")

        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")

        self.menuA_propos = QtGui.QMenu(self.menubar)
        self.menuA_propos.setObjectName("menuA_propos")

        self.menuTransform = QtGui.QMenu(self.menubar)
        self.menuTransform.setObjectName("menuTransform")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(self.toolBar)

        self.actionNouveau = QtGui.QAction(MainWindow)
        self.actionNouveau.setIcon(QtGui.QIcon(":/new/prefix1/icones/Nouveau.svg"))
        self.actionNouveau.setObjectName("actionNouveau")

        self.actionOuvrir = QtGui.QAction(MainWindow)
        self.actionOuvrir.setIcon(QtGui.QIcon(":/new/prefix1/icones/Ouvrir.svg"))
        self.actionOuvrir.setObjectName("actionOuvrir")

        self.actionEnregistrer = QtGui.QAction(MainWindow)
        self.actionEnregistrer.setIcon(QtGui.QIcon(":/new/prefix1/icones/Enregistrer.svg"))
        self.actionEnregistrer.setObjectName("actionEnregistrer")

        self.actionQuitter = QtGui.QAction(MainWindow)
        self.actionQuitter.setIcon(QtGui.QIcon(":/new/prefix1/icones/Quitter.svg"))
        self.actionQuitter.setObjectName("actionQuitter")

        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setIcon(QtGui.QIcon(":/new/prefix1/icones/APropos.svg"))
        self.actionHelp.setObjectName("actionHelp")

        self.actionHTML = QtGui.QAction(MainWindow)
        self.actionHTML.setObjectName("actionHTML")

        self.actionLaTeX = QtGui.QAction(MainWindow)
        self.actionLaTeX.setObjectName("actionLaTeX")

        self.actionDialogue_de_conversion = QtGui.QAction(MainWindow)
        self.actionDialogue_de_conversion.setIcon(QtGui.QIcon(":/new/prefix1/icones/ConversionDialog.svg"))
        self.actionDialogue_de_conversion.setObjectName("actionDialogue_de_conversion")

        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setIcon(QtGui.QIcon(":/new/prefix1/icones/Settings.svg"))
        self.actionSettings.setObjectName("actionSettings")

        self.actionRafraichir = QtGui.QAction(MainWindow)
        self.actionRafraichir.setIcon(QtGui.QIcon(":/new/prefix1/icones/reload.svg"))
        self.actionRafraichir.setObjectName("actionRafraichir")

        self.actionVoirDansNavigateur = QtGui.QAction(MainWindow)
        self.actionVoirDansNavigateur.setIcon(QtGui.QIcon(":/new/prefix1/icones/Navigateur.svg"))
        self.actionVoirDansNavigateur.setObjectName("actionVoirDansNavigateur")
        self.menuFichier.addAction(self.actionNouveau)
        self.menuFichier.addAction(self.actionOuvrir)
        self.menuFichier.addAction(self.actionEnregistrer)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuitter)
        self.menuA_propos.addSeparator()
        self.menuA_propos.addAction(self.actionHelp)
        self.menuTransform.addAction(self.actionDialogue_de_conversion)
        self.menuTransform.addAction(self.actionSettings)
        self.menuTransform.addAction(self.actionRafraichir)
        self.menuTransform.addAction(self.actionVoirDansNavigateur)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuA_propos.menuAction())
        self.toolBar.addAction(self.actionOuvrir)
        self.toolBar.addAction(self.actionNouveau)
        self.toolBar.addAction(self.actionEnregistrer)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRafraichir)
        self.toolBar.addAction(self.actionDialogue_de_conversion)
        self.toolBar.addAction(self.actionVoirDansNavigateur)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuitter)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "reSTinPeace", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Editeur", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Browser", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("MainWindow", "Fichier", None, QtGui.QApplication.UnicodeUTF8))
        self.menuA_propos.setTitle(QtGui.QApplication.translate("MainWindow", "A propos", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTransform.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNouveau.setText(QtGui.QApplication.translate("MainWindow", "Nouveau", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOuvrir.setText(QtGui.QApplication.translate("MainWindow", "Ouvrir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnregistrer.setText(QtGui.QApplication.translate("MainWindow", "Enregistrer", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuitter.setText(QtGui.QApplication.translate("MainWindow", "Quitter", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHTML.setText(QtGui.QApplication.translate("MainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLaTeX.setText(QtGui.QApplication.translate("MainWindow", "LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.actionDialogue_de_conversion.setText(QtGui.QApplication.translate("MainWindow", "Dialogue de conversion", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRafraichir.setText(QtGui.QApplication.translate("MainWindow", "Rafraichir", None, QtGui.QApplication.UnicodeUTF8))
        self.actionVoirDansNavigateur.setText(QtGui.QApplication.translate("MainWindow", "Voir dans le navigateur", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc
