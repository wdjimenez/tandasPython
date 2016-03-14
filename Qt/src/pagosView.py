#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_pagos = uic.loadUiType("pagosView.ui")[0]

class pagosViewClass(QtGui.QMainWindow, form_class_pagos):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.setupUi(self)
        self.pushButtonAceptar.clicked.connect(self.actualizarEntradas)
        self.pushButtonCancel.clicked.connect(self.close)
        self.comboBoxTandas.currentIndexChanged.connect(self.mostrarByPeriodo)
        self.calendarWidget.setMinimumDate(QtCore.QDate.currentDate())
        self.calendarWidget.clicked[QtCore.QDate].connect(self.mostrarByPeriodo)
        # self.dateEdit.setMinimumDate(QtCore.QDate.currentDate())
        # self.dateEdit.dateChanged.connect(self.mostrarByPeriodo)

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
        self._fecha = self.calendarWidget.selectedDate()
        self._currentSelected = self._tandas[str(self.comboBoxTandas.currentText())]
        inforTandaSeleccionada = self._tandaControl.recuperarTandas(self._currentSelected)

        periodicidad = self._tandaControl.recuperarPeriodicidad(str(inforTandaSeleccionada[0][2]))
        self._periodoDias = periodicidad[0][2]

        fechaInicio = inforTandaSeleccionada[0][1]
        cantInte = inforTandaSeleccionada[0][5]
        fechaInf = QtCore.QDate.fromString(fechaInicio, "yyyy-MM-dd")

        fechaFinal = fechaInf.addDays(self._periodoDias * cantInte)
        self.calendarWidget.setMaximumDate(fechaFinal)

        for pos in range(cantInte):
            self._fi = fechaInf.addDays(self._periodoDias * pos )
            self._fs = fechaInf.addDays(self._periodoDias * ( pos + 1) )
            if not(self._fecha >= self._fi and self._fecha <= self._fs ):
                continue
            self._pos = pos
            self.actualizarTableWidgetByPeriodo(self._currentSelected, pos)

    def actualizarTableWidgetByPeriodo(self, idTanda, periodo):

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        self._idIntegrantes = {}
        integrantesDict = self._tandaControl.recuperarIntegrantesByTandaEntrada(idTanda, periodo)
        for integrante in integrantesDict:
            # print integrante
            row = self.tableWidget.rowCount()
            self._idIntegrantes[row] = str(integrante[0])
            nombre = QtGui.QTableWidgetItem(str(integrante[1]) + " " + str(integrante[2]))
            periodo = QtGui.QTableWidgetItem(str(integrante[6]))
            fecha = QtGui.QTableWidgetItem(self._fi.toString("yyyy-MM-dd") + " - " + self._fs.toString("yyyy-MM-dd"))

            pWidget = QtGui.QWidget()
            pCheckBox = QtGui.QCheckBox()
            if str(integrante[7]) == '1':
                continue

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

    def actualizarEntradas(self):
		listaIntegrantes = []
		for row in range(0, self.tableWidget.rowCount()):
			checkBox = self.tableWidget.cellWidget(row, 3).layout().itemAt(0).widget()
			if checkBox.isEnabled() and checkBox.isChecked():
				listaIntegrantes.append(self._idIntegrantes[row])
		if len(listaIntegrantes):
			self._tandaControl.actualizarTandaEntrada(self._currentSelected , listaIntegrantes, self._pos)
		if self.sender() and self.sender().text() == 'Aceptar':
			self.close()

# app = QtGui.QApplication(sys.argv)
# MyWindow = pagosViewClass(None)
# MyWindow.show()
# app.exec_()
