import re
from PyQt4 import QtCore, QtGui

# Copyright (C) 2007 Christophe Kibleur <kib2@free.fr>
#
# This file is part of reSTinPeace (http://kib2.alwaysdata.net).
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

class Highlighter(QtGui.QSyntaxHighlighter):

    def __init__(self, parent):
        QtGui.QSyntaxHighlighter.__init__(self, parent)
        self.rules = []

    def resetRules(self):
        self.rules = []

    def addRule(self, pattern, color, texformats = []):
        if len(texformats) > 0:
            tcf = QTextCharFormat()
            for f in texformats:
                if f == 'bold':
                    kk.append(QFont.Bold)
                if f == 'italic':
                    kk.append(QFont.Italic)

        if isinstance(pattern, tuple):
            pattern = (re.compile(pattern[0]), re.compile(pattern[1]))
        else:
            pattern = (re.compile(pattern), None)

        color = QtGui.QColor(color)

        self.rules.append((pattern, color))

    def modeRest(self):

        self.resetRules()

        # Colors
        indented_block = r"^(\s{4}|\t).+$"
        bullet_list  = r"^\s*[-+]\s.+$"
        directives = r"\.\.\s\w+::"
        fieldlist = r":\w+:"
        hyperlink = r"\.\. [\w+ _]*: "
        hyperlink_target = r"\b\w+_\b"
        deco = r"^(\*|\-|=|#|~)+$"
        bold = r"[*]{2}.*?[*]{2}"
        italic = r"[*]{1}.*?[*]{1}"
        links = r"`.*?`_"
        litt_string = r"``.*?``"
        snip = r"\$(\w+)"
        tables =  "(\|.*\|)|((\+(\-|\+|\=)+)\+)"

        self.addRule(indented_block, QtGui.QColor('#aea148')) # vert
        self.addRule(bullet_list, 'yellowgreen') #
        self.addRule(directives, QtGui.QColor('#9B703F')) # marron
        self.addRule(fieldlist, QtGui.QColor('#D09C10')) # marron-jaune
        self.addRule(hyperlink, QtGui.QColor(207,106,76)) # brique
        self.addRule(hyperlink_target, QtGui.QColor(207,106,76)) # brique
        self.addRule(deco, QtGui.QColor('#BF2F2F')) # rouge
        self.addRule(bold, QtGui.QColor('#FF6666')) # bleu
        self.addRule(italic, QtGui.QColor('#FF0000')) # bleu
        self.addRule(links, QtGui.QColor('#FFE04F')) # jaune
        self.addRule(litt_string, QtGui.QColor('#0078A4')) # bleu marine
        self.addRule(snip, QtGui.QColor('#99CCFF')) # bleu clair
        self.addRule(tables, QtGui.QColor('#3b77bf')) # bleu clair


    def _spanFindEnd(self, pos, pattern, text):
        while pos < len(text):
            match = pattern.match(text, pos)
            if match is not None:
                self.setCurrentBlockState(-1)
                return match.end()
            pos += 1
        return pos

    def highlightBlock(self, text):

        if self.previousBlockState() >= 0:
            self.setCurrentBlockState(self.previousBlockState())
            ((pattern, span), color) = self.rules[self.previousBlockState()]
            pos = self._spanFindEnd(0, span, text)
            self.setFormat(0, pos, color)
            pos += 1
        else:
            pos = 0

        while pos < len(text):

            index = 0
            for ((pattern, span), color) in self.rules:
                match = pattern.match(unicode(text), pos)
                if match is not None:
                    pos = match.end()
                    if span is not None:
                        self.setCurrentBlockState(index)
                        pos = self._spanFindEnd(pos, span, text)

                    self.setFormat(match.start(), pos - match.start(), color)
                    #self.setFormat(match.start(), pos - match.start(), color)
                    pos -= 1
                    break
                index += 1

            pos += 1

