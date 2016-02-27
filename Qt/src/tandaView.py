
# -*- coding: utf-8 -*-
#!/usr/bin/python

import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_integrantes = uic.loadUiType("tandaView.ui")[0]

class tandaViewClass(QtGui.QDialog, form_class_integrantes):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)      
        tanda = t.tandaController()
        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate());
        self.montoEdit.textChanged.connect(self.validarNumero)
        self.pushCrear.clicked.connect(self.crearTanda)

        periodicidad = tanda.recuperarPeriodicidad()
        integrantes = tanda.recuperarIntegrantes()
        self._integrantes = {}
        self._periodicidad = {}
        for per in periodicidad:
            self._periodicidad[str(per[1])] = per[0]
            self.listWidgetPeriodo.addItem(str(per[1]))
        if len(periodicidad) > 0:
            self.listWidgetPeriodo.setItemSelected(self.listWidgetPeriodo.item(0), True)        
        for integrante in integrantes:
            self._integrantes[str(integrante[1]) + ' ' + str(integrante[2])] = integrante[0]
            self.listWidgetIntegrantes.addItem(str(integrante[1]) + ' ' + str(integrante[2]))
        print self._periodicidad

        # print self.dateEdit.date().toPyDate()

    def crearTanda(self):
        #Validamos que se haya seleccionado al menos un integrante
        selectedItems = self.listWidgetIntegrantes.selectedItems()
        selectedPeriodo = self.listWidgetPeriodo.selectedItems()
        if len(selectedItems) == 0:
            QtGui.QMessageBox.about(self,"Error!","Debe seleccionar al menos un integrante")
            return
        for per in selectedPeriodo:
            periodo = self._periodicidad[str(per.text())]
        listIdIntegrantes = []
        for integrante in selectedItems:
            listIdIntegrantes.append(self._integrantes[str(integrante.text())])
        print periodo
        print listIdIntegrantes
        result = None

        # for item in selectedItems:
        #     print item.text()

    def validarNumero(self, entry):
        if len(entry) == 0:
            return

        result = entry.toInt()
        if not(result[1]):
            # QtGui.QMessageBox.about(self,"Error!","Introduzca solo números")
            entry.chop(1)
            self.montoEdit.setText(entry)
        