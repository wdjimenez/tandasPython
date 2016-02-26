#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_integrantes = uic.loadUiType("integrantesView.ui")[0]

class integrantesViewClass(QtGui.QDialog, form_class_integrantes):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)  
		#self.actionCrearTanda.triggered.connect(self.crearTanda)
		#self.actionCrearIntegrante.triggered.connect(self.crearTanda)
		# self.buttonBox.accepted.connect(self.guardarIntegrante)
		# self.buttonBox.rejected.connect(self.guardarIntegrante)
		self.pushSave.clicked.connect(self.guardarIntegrante)
		self.pushCancel.clicked.connect(self.guardarIntegrante)
  
	def guardarIntegrante(self):
	 	# print self.entryNombre.text()
	 	tandaControl = t.tandaController()
	 	nombre = self.entryNombre.text()
	 	apellido = self.entryApellidos.text()
	 	telefono = self.entryTelefono.text()
	 	if (len(nombre) == 0 and len(apellido) == 0 and len(telefono) == 0):
			QtGui.QMessageBox.about(self,"Información","Es necesario capturar al menos el nombre del integrante")
		elif len(nombre) > 0:
			result = tandaControl.insertarIntegrante(nombre, apellido, telefono)
			self.close()
	  #   else:
	  #   	result = tandaControl.insertarIntegrante(nombre, apellido, telefono)
	  #   	if result:
	  #       	tkMessageBox.showinfo( "Información", "Se agregó el integrante correctamente")

 # def crearTanda(self):
 #   QtGui.QMessageBox.about(self,"About","This is an about box \n shown with QAction of QMenu.")
 
# app = QtGui.QApplication(sys.argv)
# MyWindow = integrantesViewClass(None)
# MyWindow.show()
# app.exec_()