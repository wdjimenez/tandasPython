#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import integrantesView as integrante
import tandaView as	tanda
 
# Cargar nuestro archivo .ui
form_class_tanda = uic.loadUiType("tandaMainView.ui")[0]
 
class tandaMainViewClass(QtGui.QMainWindow, form_class_tanda):
# class MyWindowClass(QtGui.QDialog, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)  
		self.actionCrearTanda.triggered.connect(self.crearTanda)
		self.actionCrearIntegrante.triggered.connect(self.crearIntegrante)

	def crearTanda(self):
		tandaWindow = tanda.tandaViewClass(self)
		tandaWindow.show()
		tandaWindow.exec_()

	def crearIntegrante(self):
		# intApp = QtGui.QApplication()
		intWindow = integrante.integrantesViewClass(self)
		intWindow.show()
		intWindow.exec_()
 
app = QtGui.QApplication(sys.argv)
MyWindow = tandaMainViewClass(None)
MyWindow.show()
app.exec_()
