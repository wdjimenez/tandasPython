# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_salidas = uic.loadUiType("salidasView.ui")[0]

class salidasViewClass(QtGui.QDialog, form_class_salidas):
	def __init__(self, parent=None):
		QtGui.QDialog.__init__(self, parent)
		self.setupUi(self)

		self.pushButtonCancel.clicked.connect(self.close)
		self.comboBoxTandas.currentIndexChanged.connect(self.actualizarIntegrantes)

		self._tandaControl = t.tandaController()
		tandas = self._tandaControl.recuperarTandas()
		self._tandas = {}
		for tan in tandas:
			key = str(tan[0]) + ' - ' + str(tan[1])
			self._tandas[key] = str(tan[0])			
			self.comboBoxTandas.addItem(key)

		# integrantes = tanda.recuperarIntegrantesByTandaSalida(self._tandas[str(self.comboBoxTandas.currentText())])

		# self.actualizarTableWidget(integrantes)			


	def actualizarTableWidget(self, integrantesDict):
		self.tableWidget.clearContents()
		self.tableWidget.setRowCount(0)

		for integrante in integrantesDict:

			row = self.tableWidget.rowCount()

			nombre = QtGui.QTableWidgetItem(str(integrante[1]))
			apellido = QtGui.QTableWidgetItem(str(integrante[2]))			

			nombre.setFlags(QtCore.Qt.ItemIsEnabled)
			apellido.setFlags(QtCore.Qt.ItemIsEnabled)

			self.tableWidget.insertRow(row)
			self.tableWidget.setItem(row, 0, nombre)			
			self.tableWidget.setItem(row, 1, apellido)			

			pWidget = QtGui.QWidget()
			pCheckBox = QtGui.QCheckBox()
			pLayout = QtGui.QHBoxLayout(pWidget)
			pLayout.addWidget(pCheckBox)
			pLayout.setAlignment(QtCore.Qt.AlignCenter)
			pLayout.setContentsMargins(0,0,0,0)
			pWidget.setLayout(pLayout)
			self.tableWidget.setCellWidget(row, 2, pWidget)

	def actualizarIntegrantes(self, newIndex):	
		integrantes = self._tandaControl.recuperarIntegrantesByTandaSalida(self._tandas[str(self.comboBoxTandas.currentText())])
		self.actualizarTableWidget(integrantes)		

app = QtGui.QApplication(sys.argv)
MyWindow = salidasViewClass(None)
MyWindow.show()
app.exec_()