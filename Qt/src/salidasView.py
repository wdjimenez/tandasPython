# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_salidas = uic.loadUiType("forms/salidasView.ui")[0]

class salidasViewClass(QtGui.QDialog, form_class_salidas):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)

		self.pushButtonGuardar.clicked.connect(self.actualizarSalidas)
		self.pushButtonCancel.clicked.connect(self.close)
		self.comboBoxTandas.currentIndexChanged.connect(self.actualizarIntegrantes)
		self._first = 'X'

		self._tandaControl = t.tandaController()
		listaTandas = self._tandaControl.recuperarTandas()
		self._tandas = {}
		self._idIntegrantes = {}
		self._currentSelected = ""

		for tan in listaTandas:
			key = str(tan[0]) + ' - ' + str(tan[1])
			self._tandas[key] = str(tan[0])
			self.comboBoxTandas.addItem(key)


	def actualizarIntegrantes(self, newIndex):
		if self._first == 'X':
			self._first = ''
		else:
			reply = QtGui.QMessageBox.question(self, 'Confirmar', '¿Desea guardar los cambios?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
			if reply == QtGui.QMessageBox.Yes:
				self.actualizarSalidas()

		self._currentSelected = self._tandas[str(self.comboBoxTandas.currentText())]
		integrantes = self._tandaControl.recuperarIntegrantesByTandaSalida(self._currentSelected)
		self.actualizarTableWidget(integrantes)

	def actualizarTableWidget(self, integrantesDict):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(0)
		self._idIntegrantes = {}

		for integrante in integrantesDict:
			row = self.tableWidget.rowCount()

			self._idIntegrantes[row] = str(integrante[0])

			nombre = QtGui.QTableWidgetItem(str(integrante[1]))
			apellido = QtGui.QTableWidgetItem(str(integrante[2]))

			nombre.setFlags(QtCore.Qt.ItemIsEnabled)
			apellido.setFlags(QtCore.Qt.ItemIsEnabled)

			self.tableWidget.insertRow(row)
			self.tableWidget.setItem(row, 0, nombre)
			self.tableWidget.setItem(row, 1, apellido)

			pWidget = QtGui.QWidget()
			pCheckBox = QtGui.QCheckBox()

			if str(integrante[3]) == '1':
				pCheckBox.setCheckState(QtCore.Qt.Checked)
				pCheckBox.setDisabled(True)

			pLayout = QtGui.QHBoxLayout(pWidget)
			pLayout.addWidget(pCheckBox)
			pLayout.setAlignment(QtCore.Qt.AlignCenter)
			pLayout.setContentsMargins(0,0,0,0)
			pWidget.setLayout(pLayout)
			self.tableWidget.setCellWidget(row, 2, pWidget)

	def actualizarSalidas(self):
		#Recorremos el table widget y verificamos si algún check esta activo
		listaIntegrantes = []
		for row in range(0, self.tableWidget.rowCount()):
			checkBox = self.tableWidget.cellWidget(row, 2).layout().itemAt(0).widget()
			if checkBox.isEnabled() and checkBox.isChecked():
				listaIntegrantes.append(self._idIntegrantes[row])
			# print "Row " + str(row) + " - " + str(self.tableWidget.cellWidget(row, 2).layout().itemAt(0).widget().isChecked())
		# print listaIntegrantes
		if len(listaIntegrantes):
			self._tandaControl.actualizarTandaSalida(self._currentSelected , listaIntegrantes)
		if self.sender() and self.sender().text() == 'Guardar':
			self.close()			
