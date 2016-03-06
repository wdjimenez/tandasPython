
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
        self.pushCancel.clicked.connect(self.close)

        self.dateEdit.setMinimumDate(QtCore.QDate.currentDate());
        self.montoEdit.textChanged.connect(self.validarNumero)
        self.pushCrear.clicked.connect(self.crearTanda)
        self.spinBoxIntegrantes.valueChanged.connect(self.generarIntegrantes)
        
        # the default label
        self.containerLayout = None
        self.container = None

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
                

    def crearTanda(self):
        #Validamos que se introduzca un integrante        
        if self.spinBoxIntegrantes.value() == 0:
            QtGui.QMessageBox.about(self,"Error!","Debe seleccionar al menos un integrante")
            return
        #Validamos que el monto no sea cero
        if self.montoEdit.text().toInt()[0] == 0:
            QtGui.QMessageBox.about(self,"Error!","El monto debe ser mayor a cero")
            return
        idPeriodo = ""
        for per in self.listWidgetPeriodo.selectedItems():
            idPeriodo = self._periodicidad[str(per.text())]
        idList = []
        for elemento in range(0, self.containerLayout.count()):
            idList.append(self._integrantes[str(self.containerLayout.itemAt(elemento).widget().currentText())])

        tandaControl = t.tandaController()
        tandaControl.crearTanda(idList, str(self.dateEdit.date().toPyDate()), idPeriodo, self.montoEdit.text().toInt()[0])
        self.close()


    def validarNumero(self, entry):
        if len(entry) == 0:
            return

        result = entry.toInt()
        if not(result[1]):
            # QtGui.QMessageBox.about(self,"Error!","Introduzca solo números")
            entry.chop(1)
            self.montoEdit.setText(entry)

    def generarIntegrantes(self, value):
        self.containerLayout = QtGui.QVBoxLayout()
        self.container = QtGui.QWidget()
        self.container.setLayout(self.containerLayout)
        self.scrollArea.setWidget(self.container)
        for _ in range(value):
            comboBox = QtGui.QComboBox()
            for key, _ in self._integrantes.items():                
                comboBox.addItem(key)
            self.containerLayout.addWidget(comboBox)
            # self.listWidgetIntegrantes.addItem(str(integrante[1]) + ' ' + str(integrante[2]))
        
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)
		tanda = t.tandaController()
		self._periodicidad = tanda.recuperarPeriodicidad()		
		# for per in self._periodicidad:
			# self.listWidgetPeriodo.addItem(per[1])

