#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as controller
import integrantesView as integrante
import tandaView as	tanda
import pagosView as pago
import salidasView as salidas
import cerrarView as cerrar

# Cargar nuestro archivo .ui
form_class_tanda = uic.loadUiType("forms/tandaMainView.ui")[0]

class tandaMainViewClass(QtGui.QMainWindow, form_class_tanda):
# class MyWindowClass(QtGui.QDialog, form_class):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.actionCrearTanda.triggered.connect(self.crearTanda)
		self.actionCrearIntegrante.triggered.connect(self.crearIntegrante)
		self.actionEntradas.triggered.connect(self.tandaEntradas)
		self.actionSalidas.triggered.connect(self.tandaSalidas)
		self.actionCerrar.triggered.connect(self.tandaCerrar)
		self.pic.setPixmap(QtGui.QPixmap("img/22-512.png"))
		self.setWindowIcon(QtGui.QIcon('img/tanda32x32.ico'))
		t = controller.tandaController()
		t.initDB()


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