#!/usr/bin/env python
# -*- coding: utf-8 -*-

## PyQt specific
from PyQt4 import QtGui, QtCore

t = [   ['alpha','beta','gamma'],
        ['one','two','three'],
        ['un','deux','trois']
    ]
    
def makeTable(tlist):
    return "|" + "|".join(tlist) + "|"
    
print makeTable(['alpha','beta','gamma'])
tablePainter(t)
        
