# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_preferences.ui'
#
# Created: Sun Oct 21 10:04:26 2007
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_preferences(object):
    def setupUi(self, preferences):
        preferences.setObjectName("preferences")
        preferences.resize(QtCore.QSize(QtCore.QRect(0,0,400,300).size()).expandedTo(preferences.minimumSizeHint()))

        self.hboxlayout = QtGui.QHBoxLayout(preferences)
        self.hboxlayout.setObjectName("hboxlayout")

        self.vboxlayout = QtGui.QVBoxLayout()
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(preferences)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.hboxlayout1 = QtGui.QHBoxLayout(self.tab)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)

        spacerItem = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem,0,1,1,1)

        self.lineEdit = QtGui.QLineEdit(self.tab)
        self.lineEdit.setObjectName("lineEdit")
        self.gridlayout.addWidget(self.lineEdit,0,2,1,1)

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,1,0,1,1)

        spacerItem1 = QtGui.QSpacerItem(40,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.gridlayout.addItem(spacerItem1,1,1,1,1)

        self.lineEdit_2 = QtGui.QLineEdit(self.tab)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.gridlayout.addWidget(self.lineEdit_2,1,2,1,1)
        self.hboxlayout1.addLayout(self.gridlayout)
        self.tabWidget.addTab(self.tab,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.editorFontButton = QtGui.QPushButton(self.tab_2)
        self.editorFontButton.setGeometry(QtCore.QRect(10,20,151,29))
        self.editorFontButton.setObjectName("editorFontButton")
        self.tabWidget.addTab(self.tab_2,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.buttonBox = QtGui.QDialogButtonBox(preferences)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout.addWidget(self.buttonBox)
        self.hboxlayout.addLayout(self.vboxlayout)

        self.retranslateUi(preferences)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),preferences.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),preferences.reject)
        QtCore.QMetaObject.connectSlotsByName(preferences)

    def retranslateUi(self, preferences):
        preferences.setWindowTitle(QtGui.QApplication.translate("preferences", "Configuration dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("preferences", "Default directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("preferences", "Default output directory :", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QtGui.QApplication.translate("preferences", "General", None, QtGui.QApplication.UnicodeUTF8))
        self.editorFontButton.setText(QtGui.QApplication.translate("preferences", "Choose editor font", None, QtGui.QApplication.UnicodeUTF8))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QtGui.QApplication.translate("preferences", "Editor", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    preferences = QtGui.QDialog()
    ui = Ui_preferences()
    ui.setupUi(preferences)
    preferences.show()
    sys.exit(app.exec_())
