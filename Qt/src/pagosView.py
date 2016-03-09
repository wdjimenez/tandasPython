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

        self._tandaControl = t.tandaController()
        listaTandas = self._tandaControl.recuperarTandas()
        self._tandas = {}
        self._currentSelected = ""

        # comboBoxTandas
        for tanda in listaTandas:
			itemTanda = str(tanda[0]) + ' - ' + str(tanda[1])
			self._tandas[itemTanda] = str(tanda[0])
			self.comboBoxTandas.addItem(itemTanda)

    def mostrarByPeriodo(self):
        #  Fecha
        self._fechaHoy = QtCore.QDate.currentDate()
        self.lineFecha.setText(self._fechaHoy.toString("yyyy-MM-dd"))
        self.lineFecha.setDisabled(1)
        #
        self._currentSelected = self._tandas[str(self.comboBoxTandas.currentText())]
        inforTandaSeleccionada = self._tandaControl.recuperarTandas(self._currentSelected)

        periodicidad = self._tandaControl.recuperarPeriodicidad(str(inforTandaSeleccionada[0][2]))
        self._periodoDias = periodicidad[0][2]

        fechaInicio = inforTandaSeleccionada[0][1]
        cantInte = inforTandaSeleccionada[0][5]
        fechaInf = QtCore.QDate.fromString(fechaInicio, "yyyy-MM-dd")

        for pos in range(cantInte - 1):
            self._fi = fechaInf.addDays(self._periodoDias * pos )
            self._fs = fechaInf.addDays(self._periodoDias * ( pos + 1) )
            # self._fechaHoy = self._fechaHoy.fromString(fechaInicio, "yyyy-MM-dd").addDays(15)
            if not(self._fechaHoy >= self._fi and self._fechaHoy <= self._fs ):
                continue
            self.actualizarTableWidgetByPeriodo(self._currentSelected, pos)

    def actualizarTableWidgetByPeriodo(self, idTanda, periodo):

        self.tableWidget.clearContents()
        self.tableWidget.setRowCount(0)

        self._idIntegrantes = {}
        integrantesDict = self._tandaControl.recuperarIntegrantesByTandaEntrada(idTanda, periodo)
        for integrante in integrantesDict:
            print integrante
            row = self.tableWidget.rowCount()
            self._idIntegrantes[row] = str(integrante[0])
            nombre = QtGui.QTableWidgetItem(str(integrante[1]) + " " + str(integrante[2]))
            periodo = QtGui.QTableWidgetItem(str(integrante[6]))
            fecha = QtGui.QTableWidgetItem(self._fi.toString("yyyy-MM-dd") + " - " + self._fs.toString("yyyy-MM-dd"))

            pWidget = QtGui.QWidget()
            pCheckBox = QtGui.QCheckBox()
            if str(integrante[7]) == '1':
                pCheckBox.setCheckState(QtCore.Qt.Checked)
                pCheckBox.setDisabled(True)

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
        print "Aceptar"
        self.close()

# app = QtGui.QApplication(sys.argv)
# MyWindow = pagosViewClass(None)
# MyWindow.show()
# app.exec_()
