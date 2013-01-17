# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_converter.ui'
#
# Created: Wed Aug 29 16:19:59 2007
#      by: PyQt4 UI code generator 4-snapshot-20070727
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_Converter(object):
    def setupUi(self, Converter):
        Converter.setObjectName("Converter")
        Converter.resize(QtCore.QSize(QtCore.QRect(0,0,235,156).size()).expandedTo(Converter.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(Converter)
        self.vboxlayout.setObjectName("vboxlayout")

        self.vboxlayout1 = QtGui.QVBoxLayout()
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.gridlayout = QtGui.QGridLayout()
        self.gridlayout.setObjectName("gridlayout")

        self.label_2 = QtGui.QLabel(Converter)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,0,0,1,1)

        self.combo_out = QtGui.QComboBox(Converter)
        self.combo_out.setMinimumSize(QtCore.QSize(0,0))
        self.combo_out.setModelColumn(0)
        self.combo_out.setObjectName("combo_out")
        self.gridlayout.addWidget(self.combo_out,0,1,1,1)

        self.label_4 = QtGui.QLabel(Converter)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,1,0,1,1)

        self.combo_style = QtGui.QComboBox(Converter)
        self.combo_style.setMinimumSize(QtCore.QSize(0,0))
        self.combo_style.setObjectName("combo_style")
        self.gridlayout.addWidget(self.combo_style,1,1,1,1)

        self.label_5 = QtGui.QLabel(Converter)
        self.label_5.setObjectName("label_5")
        self.gridlayout.addWidget(self.label_5,2,0,1,1)

        self.combo_options = QtGui.QComboBox(Converter)
        self.combo_options.setMinimumSize(QtCore.QSize(0,0))
        self.combo_options.setObjectName("combo_options")
        self.gridlayout.addWidget(self.combo_options,2,1,1,1)

        self.but_process = QtGui.QPushButton(Converter)
        self.but_process.setObjectName("but_process")
        self.gridlayout.addWidget(self.but_process,3,0,1,1)

        self.changedir = QtGui.QPushButton(Converter)
        self.changedir.setObjectName("changedir")
        self.gridlayout.addWidget(self.changedir,3,1,1,1)
        self.vboxlayout1.addLayout(self.gridlayout)

        self.buttonBox = QtGui.QDialogButtonBox(Converter)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.NoButton|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.vboxlayout1.addWidget(self.buttonBox)
        self.vboxlayout.addLayout(self.vboxlayout1)

        self.retranslateUi(Converter)
        self.combo_out.setCurrentIndex(0)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("accepted()"),Converter.accept)
        QtCore.QObject.connect(self.buttonBox,QtCore.SIGNAL("rejected()"),Converter.reject)
        QtCore.QMetaObject.connectSlotsByName(Converter)

    def retranslateUi(self, Converter):
        Converter.setWindowTitle(QtGui.QApplication.translate("Converter", "Convertisseur", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Converter", "Output format :", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_out.addItem(QtGui.QApplication.translate("Converter", "(X)HTML", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_out.addItem(QtGui.QApplication.translate("Converter", "LaTeX", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_out.addItem(QtGui.QApplication.translate("Converter", "OpenOffice", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_out.addItem(QtGui.QApplication.translate("Converter", "Lout", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Converter", "StyleSheet :", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_style.addItem(QtGui.QApplication.translate("Converter", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Converter", "Options :", None, QtGui.QApplication.UnicodeUTF8))
        self.combo_options.addItem(QtGui.QApplication.translate("Converter", "Default", None, QtGui.QApplication.UnicodeUTF8))
        self.but_process.setText(QtGui.QApplication.translate("Converter", "Process", None, QtGui.QApplication.UnicodeUTF8))
        self.changedir.setText(QtGui.QApplication.translate("Converter", "Change saves directory", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    Converter = QtGui.QDialog()
    ui = Ui_Converter()
    ui.setupUi(Converter)
    Converter.show()
    sys.exit(app.exec_())
