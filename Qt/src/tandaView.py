#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import integrantesView as integrante
 
# Cargar nuestro archivo .ui
form_class_tanda = uic.loadUiType("tandaView.ui")[0]
 
class tandaViewClass(QtGui.QMainWindow, form_class_tanda):
# class MyWindowClass(QtGui.QDialog, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)  
		self.actionCrearTanda.triggered.connect(self.crearTanda)
		self.actionCrearIntegrante.triggered.connect(self.crearIntegrante)

	def crearTanda(self):
		QtGui.QMessageBox.about(self,"About","This is an about box \n shown with QAction of QMenu.")

	def crearIntegrante(self):
		# intApp = QtGui.QApplication()
		intWindow = integrante.integrantesViewClass(None)
		intWindow.show()
		intWindow.exec_()
 
app = QtGui.QApplication(sys.argv)
MyWindow = tandaViewClass(None)
MyWindow.show()
app.exec_()
