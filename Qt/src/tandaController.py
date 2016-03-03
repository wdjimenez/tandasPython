# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

class tandaController:
    """Clase para manipular información de los integrantes"""
    def __init__(self, db = 'TandaDB.db'):
        """Se recibe la BD que se va a utilizar"""
        self._db = db

    def crearTanda(self, listIdIntegrantes, fechaInicio, idPeriodo, monto):
        """Método para generar una nueva tanda, integrantes es una lista con los ID integrantes"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Tandas(fechaInicio, idPer, monto, finalizada) VALUES(?, ?, ?, ?)', (fechaInicio, idPeriodo, monto, 0))
            lid = cur.lastrowid
            #Agregamos los registros de TandaSalida y TandaEntrada para cada integrante
            for idIntegrante in listIdIntegrantes:
                cur.execute('INSERT INTO TandaSalida(idTandas, idIntegrante, pagado) VALUES(?, ?, ?)', (lid, idIntegrante, 0))
                for pos in range(0, len(listIdIntegrantes)):
                    cur.execute('INSERT INTO TandaEntrada(idTandas, idIntegrante, pos, pagado) VALUES(?, ?, ?, ?)', (lid, idIntegrante, pos, 0))
            con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

    def recuperarTandas(self, idTandas = None):
        """Método para recuperar información de una tanda o de todas las tandas si no se pasa el parámetro idTandas"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idTandas is None):
                cur.execute('SELECT * FROM Tandas WHERE idTandas = ?', (idTandas))
            else:
                cur.execute('SELECT * FROM Tandas')
            rows = cur.fetchall()
        except Exception as e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

    def insertarIntegrante(self, nombre, apellido, telefono):
        """Método para insertar un nuevo integrante"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Integrantes(nombre, apellido, telefono) VALUES(?, ?, ?)', (nombre, apellido, telefono))
            con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

    def recuperarIntegrantes(self, idIntegrante = None):
        """Método para recuperar los integrantes disponibles o un integrante en especifico"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()

            if idIntegrante is None:
                cur.execute('SELECT * FROM Integrantes')
            else:
                cur.execute('SELECT * FROM Integrantes WHERE idIntegrante = ?', (idIntegrante))
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

    def recuperarPeriodicidad(self):
        """Método para recuperar las periodicidades disponibles"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('SELECT * FROM Periodicidad')
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

    def insertarTandaSalida(self, idTandas, idIntegrante, pagado):
        """Método para insertar un pago hecho a un tandero"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Pagos(idTandas, idIntegrante, pagado) VALUES(?, ?, ?)', (idTandas, idIntegrante, pagado))
            con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

    def recuperarTandaSalida(self, idTandas = None, idIntegrante = None):
        """Método para recuperar los pagos rentantes de una tanda"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idTandas is None and idIntegrante is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idTandas = ? and idIntegrante = ? and pagado = ?', (idTandas, idIntegrante, 0))
            elif not(idTandas is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idTandas = ? and pagado = ?', (idTandas, 0))
            elif not(idIntegrante is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idIntegrante = ? and pagado = ?', (idIntegrante, 0))
            else:
                cur.execute('SELECT * FROM TandaSalida WHERE pagado = ?', (0))
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

    def recuperarTandaEntrada(self, idTandas, idIntegrante = None):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idIntegrante is None):
                cur.execute('SELECT * FROM TandaEntrada WHERE idTandas = ? and idIntegrante = ? and pagado = ?', (idTandas, idIntegrante, 0))
            else:
                cur.execute('SELECT * FROM TandaEntrada WHERE idTandas = ? and pagado = ?', (idTandas, 0))
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows
    # def insertarTandaEntrada(self, idTandas, idIntegrantes):

# tanda = tandaController()
# for p in tanda.recuperarPeriodicidad():
#     print p[0], p[1]
# #tanda.recuperarIntegrantes()
# tanda.crearTanda('10', '2016-02-06', '1', '3000')
