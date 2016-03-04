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
        self.pushCancel.clicked.connect(self.close)
        self.lineFecha.setDisabled(1)
        tanda = t.tandaController()
        tandas = tanda.recuperarTandas()
        for tan in tandas:
            itemTanda = str(tan[0]) + ' - ' + str(tan[1])
            self.comboBoxTandas.addItem(itemTanda)
        self.comboBoxTandas.currentIndexChanged.connect(self.mostrarInfor)

    def mostrarInfor(self):
        textoIndex = self.comboBoxTandas.currentText()
        tandastr = str(textoIndex).split(' ')
        tandaId = tandastr[0]
        tanda = t.tandaController()
        res = tanda.recuperarTandas(tandaId)
        for r in res:
            self.lineFecha.setText(r[1])
        integrantes = tanda.recuperarIntegrantesTanda(tandaId)
        for i in integrantes:
            print i
        # SELECT * FROM TandaEntrada as t JOIN Integrantes as i on t.idTandas = 1;


# app = QtGui.QApplication(sys.argv)
# MyWindow = pagosViewClass(None)
# MyWindow.show()
# app.exec_()
