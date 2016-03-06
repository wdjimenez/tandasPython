#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import integrantesView as integrante
import tandaView as	tanda
import pagosView as pago
import salidasView as salidas
import cerrarView as cerrar

# Cargar nuestro archivo .ui
form_class_tanda = uic.loadUiType("tandaMainView.ui")[0]

class tandaMainViewClass(QtGui.QMainWindow, form_class_tanda):
# class MyWindowClass(QtGui.QDialog, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.actionCrearTanda.triggered.connect(self.crearTanda)
		self.actionCrearIntegrante.triggered.connect(self.crearIntegrante)
		self.actionEntradas.triggered.connect(self.tandaEntradas)
		self.actionSalidas.triggered.connect(self.tandaSalidas)
		# self.actionCerrar.triggered.connect(self.tandaCerrar)

	def crearTanda(self):
		tandaWindow = tanda.tandaViewClass(self)
		tandaWindow.show()
		tandaWindow.exec_()

	def crearIntegrante(self):
		# intApp = QtGui.QApplication()
		intWindow = integrante.integrantesViewClass(self)
		intWindow.show()
		intWindow.exec_()

	def tandaEntradas(self):
		entWindow = pago.pagosViewClass(self)
		entWindow.show()
		# app.exec_()

	def tandaSalidas(self):
		entWindow = salidas.salidasViewClass(self)
		entWindow.show()
		entWindow.exec_()

	def tandaCerrar(self):
		entWindow = cerrar.cerrarViewClass(self)
		entWindow.show()
		entWindow.exec_()

app = QtGui.QApplication(sys.argv)
MyWindow = tandaMainViewClass(None)
MyWindow.show()
app.exec_()
