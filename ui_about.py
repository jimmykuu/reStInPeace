# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_about.ui'
#
# Created: Sat Oct 20 21:14:51 2007
#      by: PyQt4 UI code generator 4.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_About(object):
    def setupUi(self, About):
        About.setObjectName("About")
        About.resize(QtCore.QSize(QtCore.QRect(0,0,588,373).size()).expandedTo(About.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(About)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setObjectName("vboxlayout")

        self.label_2 = QtGui.QLabel(About)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.vboxlayout.addWidget(self.label_2)

        self.label = QtGui.QLabel(About)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred,QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setPixmap(QtGui.QPixmap("icones/logo.svg"))
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.vboxlayout.addWidget(self.label)

        self.label_3 = QtGui.QLabel(About)

        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(11)
        font.setItalic(True)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.vboxlayout.addWidget(self.label_3)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setSpacing(6)
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setObjectName("hboxlayout")

        spacerItem = QtGui.QSpacerItem(71,31,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem)

        self.okButton = QtGui.QPushButton(About)
        self.okButton.setObjectName("okButton")
        self.hboxlayout.addWidget(self.okButton)
        self.vboxlayout.addLayout(self.hboxlayout)

        self.retranslateUi(About)
        QtCore.QObject.connect(self.okButton,QtCore.SIGNAL("clicked()"),About.accept)
        QtCore.QMetaObject.connectSlotsByName(About)

    def retranslateUi(self, About):
        About.setWindowTitle(QtGui.QApplication.translate("About", "About", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("About", "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
        "p, li { white-space: pre-wrap; }\n"
        "</style></head><body style=\" font-family:\'Sans Serif\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Bitstream Vera Sans\';\"><span style=\" font-size:18pt; font-style:italic; color:#a52a2a;\">reSTinPeace</span><span style=\" font-size:18pt; font-style:italic;\">  </span><span style=\" font-style:italic;\"> </span></p>\n"
        "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Bitstream Vera Sans\'; font-style:italic;\">Manage your <span style=\" color:#b22222;\">reSTructuredText </span>documents easily.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("About", "(c) August 2007 by Kibleur Christophe <kib2@free.fr>\n"
        "More infos at http://kib2.free.fr/", None, QtGui.QApplication.UnicodeUTF8))
        self.okButton.setText(QtGui.QApplication.translate("About", "OK", None, QtGui.QApplication.UnicodeUTF8))



if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    About = QtGui.QDialog()
    ui = Ui_About()
    ui.setupUi(About)
    About.show()
    sys.exit(app.exec_())
