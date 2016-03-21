#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import src.tandaMainView as tandaMain

app = QtGui.QApplication(sys.argv)
MyWindow = tandaMain.tandaMainViewClass(None)
MyWindow.show()
app.exec_()