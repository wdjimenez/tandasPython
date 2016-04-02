#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
from datetime import datetime
import tandaController as t

form_class_pagos = uic.loadUiType("forms/pagosView.ui")[0]

class pagosViewClass(QtGui.QMainWindow, form_class_pagos):
	def __init__(self, parent=None):
		QtGui.QMainWindow.__init__(self, parent)
		self.setupUi(self)
		self.pushButtonAceptar.clicked.connect(self.actualizarEntradas)
		self.pushButtonCancel.clicked.connect(self.close)
		self.comboBoxTandas.currentIndexChanged.connect(self.mostrarByPeriodo)
		self.calendarWidget.setMinimumDate(QtCore.QDate.currentDate())
		self.calendarWidget.clicked[QtCore.QDate].connect(self.mostrarByPeriodo)

		self._tandaControl = t.tandaController()
		listaTandas = self._tandaControl.recuperarTandas()
		self._tandas = {}
		self._currentSelected = ""

		# _idIntegrantes se utilizará en actualizarEntradas
		self._idIntegrantes = {}
		self._pos = 0
		# comboBoxTandas
		for tanda in listaTandas:
			itemTanda = str(tanda[0]) + ' - ' + str(tanda[1])
			self._tandas[itemTanda] = str(tanda[0])
			self.comboBoxTandas.addItem(itemTanda)

	def mostrarByPeriodo(self):
		# Fecha Seleccionada
		selFecha = self.calendarWidget.selectedDate()
		# Tanda Seleccionada
		self._currentSelected = self._tandas[str(self.comboBoxTandas.currentText())]        
		# Recuperamos la información de la tanda
		inforTandaSeleccionada = self._tandaControl.recuperarTandas(self._currentSelected)
		# Recuperamos la información del periodo
		periodicidad = self._tandaControl.recuperarPeriodicidad(str(inforTandaSeleccionada[0][2]))
		# Cuantos días tiene el periodo?
		periodoDias = periodicidad[0][2]

		fechaInicio = inforTandaSeleccionada[0][1]
		fechaInf = QtCore.QDate.fromString(fechaInicio, "yyyy-MM-dd")

		fechaFinal = fechaInf.addDays(periodoDias * inforTandaSeleccionada[0][5])

		# Cambiamos el rango de fechas que se pueden seleccionar de acuerdo a la tanda
		self.calendarWidget.setMinimumDate(fechaInf)
		self.calendarWidget.setMaximumDate(fechaFinal)

		# Reiniciamos el grid
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(0)

		for n in range(inforTandaSeleccionada[0][5]):
			fi = fechaInf.addDays(periodoDias * n )
			fs = fechaInf.addDays(periodoDias * ( n + 1) )
			fecha = datetime(selFecha.year(), selFecha.month(), selFecha.day())
			rangoInicial = datetime(fi.year(), fi.month(), fi.day())
			rangoFinal = datetime(fs.year(), fs.month(), fs.day())

			if fecha >= rangoInicial and fecha <= rangoFinal:
				self.actualizarTableWidgetByPeriodo(self._currentSelected, fechaInf, n, periodoDias)
				break

	def actualizarTableWidgetByPeriodo(self, idTanda, fechaIni, periodo, dias):
		self._idIntegrantes = {}
		integrantesDict = self._tandaControl.recuperarIntegrantesByTandaEntrada(idTanda, periodo)

		for integrante in integrantesDict:
			row = self.tableWidget.rowCount()
			self._idIntegrantes[row] = str(integrante[0])
			nombre = QtGui.QTableWidgetItem(str(integrante[1]) + " " + str(integrante[2]))
			periodo = QtGui.QTableWidgetItem(str(integrante[6]))

			fi = fechaIni.addDays(dias * integrante[6] )
			fs = fechaIni.addDays(dias * ( integrante[6] + 1) )

			fecha = QtGui.QTableWidgetItem(fi.toString("yyyy-MM-dd") + " / " + fs.toString("yyyy-MM-dd"))

			nombre.setFlags(QtCore.Qt.ItemIsEnabled)
			periodo.setFlags(QtCore.Qt.ItemIsEnabled)
			fecha.setFlags(QtCore.Qt.ItemIsEnabled)

			pWidget = QtGui.QWidget()
			pCheckBox = QtGui.QCheckBox()

			pLayout = QtGui.QHBoxLayout(pWidget)
			pLayout.addWidget(pCheckBox)
			pLayout.setAlignment(QtCore.Qt.AlignCenter)
			pLayout.setContentsMargins(0,0,0,0)
			pWidget.setLayout(pLayout)

			self.tableWidget.insertRow(row)
			self.tableWidget.setItem(row, 0, nombre)
			self.tableWidget.setItem(row, 1, periodo)
			self.tableWidget.setItem(row, 2, fecha)
			self.tableWidget.setCellWidget(row, 3, pWidget)

			self.tableWidget.setColumnWidth(0,170)
			self.tableWidget.setColumnWidth(1,50)
			self.tableWidget.setColumnWidth(2,170)
			self.tableWidget.setColumnWidth(3,40)

	def actualizarEntradas(self):
		listaIntegrantes = []
		for row in range(0, self.tableWidget.rowCount()):
			checkBox = self.tableWidget.cellWidget(row, 3).layout().itemAt(0).widget()
			if checkBox.isEnabled() and checkBox.isChecked():
				listaIntegrantes.append((self._idIntegrantes[row], str(self.tableWidget.item(row, 1).text())))
		if len(listaIntegrantes):
			self._tandaControl.actualizarTandaEntrada(self._currentSelected , listaIntegrantes)
		if self.sender() and self.sender().text() == 'Guardar':
			self.close()