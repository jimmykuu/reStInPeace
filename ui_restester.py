# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_restester.ui'
#
# Created: Sat Oct 20 21:43:31 2007
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(QtCore.QSize(QtCore.QRect(0,0,792,645).size()).expandedTo(MainWindow.minimumSizeHint()))
        MainWindow.setWindowIcon(QtGui.QIcon(":/new/prefix1/icones/crayon.svg"))

        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.hboxlayout = QtGui.QHBoxLayout(self.centralwidget)
        self.hboxlayout.setObjectName("hboxlayout")

        self.splitter = QtGui.QSplitter(self.centralwidget)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")

        self.widget = QtGui.QWidget(self.splitter)
        self.widget.setObjectName("widget")

        self.vboxlayout = QtGui.QVBoxLayout(self.widget)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label = QtGui.QLabel(self.widget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.editor = QtGui.QTextEdit(self.widget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.editor.sizePolicy().hasHeightForWidth())
        self.editor.setSizePolicy(sizePolicy)

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
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(11)
        self.editor.setFont(font)
        self.editor.setAcceptRichText(False)
        self.editor.setObjectName("editor")
        self.vboxlayout.addWidget(self.editor)

        self.widget1 = QtGui.QWidget(self.splitter)
        self.widget1.setObjectName("widget1")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.widget1)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.label_2 = QtGui.QLabel(self.widget1)

        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.vboxlayout1.addWidget(self.label_2)

        self.viewer = QtGui.QTextBrowser(self.widget1)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy)

        font = QtGui.QFont()
        font.setFamily("DejaVu Sans Mono")
        font.setPointSize(11)
        self.viewer.setFont(font)
        self.viewer.setObjectName("viewer")
        self.vboxlayout1.addWidget(self.viewer)
        self.hboxlayout.addWidget(self.splitter)
        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0,0,792,27))
        self.menubar.setObjectName("menubar")

        self.menuFichier = QtGui.QMenu(self.menubar)
        self.menuFichier.setObjectName("menuFichier")

        self.menuAbout = QtGui.QMenu(self.menubar)
        self.menuAbout.setObjectName("menuAbout")

        self.menuTransform = QtGui.QMenu(self.menubar)
        self.menuTransform.setObjectName("menuTransform")

        self.menuLangages = QtGui.QMenu(self.menubar)
        self.menuLangages.setObjectName("menuLangages")
        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(self.toolBar)

        self.actionNew = QtGui.QAction(MainWindow)
        self.actionNew.setIcon(QtGui.QIcon(":/new/prefix1/icones/Nouveau.svg"))
        self.actionNew.setObjectName("actionNew")

        self.actionOpen = QtGui.QAction(MainWindow)
        self.actionOpen.setIcon(QtGui.QIcon(":/new/prefix1/icones/Ouvrir.svg"))
        self.actionOpen.setObjectName("actionOpen")

        self.actionSave = QtGui.QAction(MainWindow)
        self.actionSave.setIcon(QtGui.QIcon(":/new/prefix1/icones/Enregistrer.svg"))
        self.actionSave.setObjectName("actionSave")

        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setIcon(QtGui.QIcon(":/new/prefix1/icones/Quitter.svg"))
        self.actionQuit.setObjectName("actionQuit")

        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setIcon(QtGui.QIcon(":/new/prefix1/icones/APropos.svg"))
        self.actionAbout.setObjectName("actionAbout")

        self.actionHTML = QtGui.QAction(MainWindow)
        self.actionHTML.setObjectName("actionHTML")

        self.actionLaTeX = QtGui.QAction(MainWindow)
        self.actionLaTeX.setObjectName("actionLaTeX")

        self.actionConversionDialog = QtGui.QAction(MainWindow)
        self.actionConversionDialog.setIcon(QtGui.QIcon(":/new/prefix1/icones/ConversionDialog.svg"))
        self.actionConversionDialog.setObjectName("actionConversionDialog")

        self.actionSettings = QtGui.QAction(MainWindow)
        self.actionSettings.setIcon(QtGui.QIcon(":/new/prefix1/icones/Settings.svg"))
        self.actionSettings.setObjectName("actionSettings")

        self.actionRefresh = QtGui.QAction(MainWindow)
        self.actionRefresh.setIcon(QtGui.QIcon(":/new/prefix1/icones/reload.svg"))
        self.actionRefresh.setObjectName("actionRefresh")

        self.actionSeeInDefaultBrowser = QtGui.QAction(MainWindow)
        self.actionSeeInDefaultBrowser.setIcon(QtGui.QIcon(":/new/prefix1/icones/Navigateur.svg"))
        self.actionSeeInDefaultBrowser.setObjectName("actionSeeInDefaultBrowser")

        self.actionEnglish = QtGui.QAction(MainWindow)
        self.actionEnglish.setObjectName("actionEnglish")

        self.actionFrench = QtGui.QAction(MainWindow)
        self.actionFrench.setObjectName("actionFrench")

        self.actionSaveAs = QtGui.QAction(MainWindow)
        self.actionSaveAs.setIcon(QtGui.QIcon(":/new/prefix1/icones/Enregistrer_Sous.svg"))
        self.actionSaveAs.setObjectName("actionSaveAs")

        self.actionHelp = QtGui.QAction(MainWindow)
        self.actionHelp.setIcon(QtGui.QIcon(":/new/prefix1/icones/Help.svg"))
        self.actionHelp.setObjectName("actionHelp")
        self.menuFichier.addAction(self.actionOpen)
        self.menuFichier.addAction(self.actionSave)
        self.menuFichier.addAction(self.actionNew)
        self.menuFichier.addSeparator()
        self.menuFichier.addAction(self.actionQuit)
        self.menuAbout.addSeparator()
        self.menuAbout.addAction(self.actionAbout)
        self.menuAbout.addAction(self.actionHelp)
        self.menuTransform.addAction(self.actionConversionDialog)
        self.menuTransform.addAction(self.actionSettings)
        self.menuTransform.addAction(self.actionRefresh)
        self.menuTransform.addAction(self.actionSeeInDefaultBrowser)
        self.menuLangages.addAction(self.actionEnglish)
        self.menuLangages.addAction(self.actionFrench)
        self.menubar.addAction(self.menuFichier.menuAction())
        self.menubar.addAction(self.menuTransform.menuAction())
        self.menubar.addAction(self.menuLangages.menuAction())
        self.menubar.addAction(self.menuAbout.menuAction())
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionSaveAs)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionRefresh)
        self.toolBar.addAction(self.actionConversionDialog)
        self.toolBar.addAction(self.actionSeeInDefaultBrowser)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionSettings)
        self.toolBar.addAction(self.actionHelp)
        self.toolBar.addAction(self.actionAbout)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "reSTinPeace", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Editor View", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("MainWindow", "Browser View", None, QtGui.QApplication.UnicodeUTF8))
        self.menuFichier.setTitle(QtGui.QApplication.translate("MainWindow", "File", None, QtGui.QApplication.UnicodeUTF8))
        self.menuAbout.setTitle(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.menuTransform.setTitle(QtGui.QApplication.translate("MainWindow", "Actions", None, QtGui.QApplication.UnicodeUTF8))
        self.menuLangages.setTitle(QtGui.QApplication.translate("MainWindow", "Langages", None, QtGui.QApplication.UnicodeUTF8))
        self.toolBar.setWindowTitle(QtGui.QApplication.translate("MainWindow", "toolBar", None, QtGui.QApplication.UnicodeUTF8))
        self.actionNew.setText(QtGui.QApplication.translate("MainWindow", "New", None, QtGui.QApplication.UnicodeUTF8))
        self.actionOpen.setText(QtGui.QApplication.translate("MainWindow", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSave.setText(QtGui.QApplication.translate("MainWindow", "Save", None, QtGui.QApplication.UnicodeUTF8))
        self.actionQuit.setText(QtGui.QApplication.translate("MainWindow", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.actionAbout.setText(QtGui.QApplication.translate("MainWindow", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHTML.setText(QtGui.QApplication.translate("MainWindow", "HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.actionLaTeX.setText(QtGui.QApplication.translate("MainWindow", "LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConversionDialog.setText(QtGui.QApplication.translate("MainWindow", "Conversion dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConversionDialog.setIconText(QtGui.QApplication.translate("MainWindow", "Conversion Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionConversionDialog.setToolTip(QtGui.QApplication.translate("MainWindow", "Conversion Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSettings.setText(QtGui.QApplication.translate("MainWindow", "Settings", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setText(QtGui.QApplication.translate("MainWindow", "Refresh browser view", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setIconText(QtGui.QApplication.translate("MainWindow", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.actionRefresh.setToolTip(QtGui.QApplication.translate("MainWindow", "Refresh the browser view", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSeeInDefaultBrowser.setText(QtGui.QApplication.translate("MainWindow", "See in my default browser", None, QtGui.QApplication.UnicodeUTF8))
        self.actionEnglish.setText(QtGui.QApplication.translate("MainWindow", "English", None, QtGui.QApplication.UnicodeUTF8))
        self.actionFrench.setText(QtGui.QApplication.translate("MainWindow", "French", None, QtGui.QApplication.UnicodeUTF8))
        self.actionSaveAs.setText(QtGui.QApplication.translate("MainWindow", "SaveAs", None, QtGui.QApplication.UnicodeUTF8))
        self.actionHelp.setText(QtGui.QApplication.translate("MainWindow", "Help", None, QtGui.QApplication.UnicodeUTF8))

import ressources_rc


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
