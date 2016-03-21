# -*- coding: utf-8 -*-
#!/usr/bin/python
import sys
from PyQt4 import QtCore, QtGui, uic
import tandaController as t

form_class_salidas = uic.loadUiType("forms/cerrarView.ui")[0]

class cerrarViewClass(QtGui.QDialog, form_class_salidas):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.setupUi(self)

        self.pushButtonCerrar.clicked.connect(self.cerrarTanda)
        self.pushButtonCancelar.clicked.connect(self.close)

        self._tandaControl = t.tandaController()
        # listaTandas = self._tandaControl.recuperarTandas()

        self._tandas = {}
        self.actualizarComboBox(self._tandaControl.recuperarTandas())
        

    def cerrarTanda(self):
        """Método para el evento Cerrar Tanda"""
        reply = QtGui.QMessageBox.question(self, 'Confirmar', '¿Desea cerrar la Tanda?', QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            self._tandaControl.cerrarTanda(self._tandas[str(self.comboBoxTandas.currentText())])
            QtGui.QMessageBox.information(self, 'Información', 'Tanda Finalizada', QtGui.QMessageBox.Yes)
            self.actualizarComboBox(self._tandaControl.recuperarTandas())


    def actualizarComboBox(self, dictIntegrantes):
        """Agrega las Tandas al Combo Box"""
        self.comboBoxTandas.clear()

        for tanda in dictIntegrantes:
            key = str(tanda[0]) + ' - ' + str(tanda[1])
            self._tandas[key] = str(tanda[0])         
            self.comboBoxTandas.addItem(key)

# app = QtGui.QApplication(sys.argv)
# MyWindow = cerrarViewClass(None)
# MyWindow.show()
# app.exec_()