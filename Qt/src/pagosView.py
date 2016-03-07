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

        self.containerLayout = QtGui.QVBoxLayout()
        self.container = QtGui.QWidget()
        self.container.setLayout(self.containerLayout)
        self.scrollArea.setWidget(self.container)
        table = QtGui.QTableWidget()
        table.setColumnCount(4)

        matriz = []
        for i in range(len(integrantes)):
            matriz.append([])
            for j in range(4):
                matriz[i].append()
        # for i in integrantes:
        #     table.setItem(1,0, QtGui.QTableWidgetItem(str(i[0] + " " + i[1])))
        # f = 0
        # for n, key in enumerate(table.data):
        #     for m, item in enumerate(table.data[key]):
        #         newitem = QTableWidgetItem(item)
        #         table.setItem(m, n, newitem)
        self.containerLayout.addWidget(table)
        # listWidgetNombres = QtGui.QListWidget()
        # listWidgetNombres.setFixedWidth(125)
        # listWidgetPeriodo = QtGui.QListWidget()
        # listWidgetPeriodo.setFixedWidth(125)
        # for i in integrantes:
        #     item = QtGui.QListWidgetItem(str(i[0] + " " + i[1]))
        #     listWidgetNombres.addItem(item)
        #     itemPeriodo = QtGui.QListWidgetItem(str(i[0] + " " + i[1]))
        #     listWidgetPeriodo.addItem(itemPeriodo)
        # self.containerLayout.addWidget(listWidgetNombres)
        # self.containerLayout.addWidget(listWidgetPeriodo)
            # label = QtGui.QLabel(str(integrante[0] + " " + integrante[1]))

        # for i in integrantes:
        #     print i
        # SELECT * FROM TandaEntrada as t JOIN Integrantes as i on t.idTandas = 1;


# app = QtGui.QApplication(sys.argv)
# MyWindow = pagosViewClass(None)
# MyWindow.show()
# app.exec_()
