#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_integrantes = uic.loadUiType("tandaView.ui")[0]

class tandaViewClass(QtGui.QDialog, form_class_integrantes):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)  		