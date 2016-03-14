# -*- coding: utf-8 -*-
import sqlite3 as lite
import sys

class tandaController:
    """Clase para manipular información de los integrantes"""
    def __init__(self, db = 'TandaDB.db'):
        """Se recibe la BD que se va a utilizar"""
        self._db = db

    def crearTanda(self, listIdIntegrantes, fechaInicio, idPeriodo, monto, cantInte):
        """Método para generar una nueva tanda, integrantes es una lista con los ID integrantes"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Tandas(fechaInicio, idPer, monto, finalizada, cantInte) VALUES(?, ?, ?, ?, ?)', (fechaInicio, idPeriodo, monto, 0, cantInte))
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

    def cerrarTanda(self, idTanda):
        """Método para cerrar una tanda a partir de su ID"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute("UPDATE Tandas SET finalizada = 1 WHERE idTandas = ?", idTanda)
            con.commit()
        except Exception as e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

    def recuperarTandas(self, idTandas = None):
        """Método para recuperar información de una tanda o de todas las tandas si no se pasa el parámetro idTandas"""
        rows = {}
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idTandas is None):
                cur.execute('SELECT * FROM Tandas WHERE idTandas = ? and finalizada = 0', (idTandas))
            else:
                cur.execute('SELECT * FROM tandas WHERE finalizada = 0')
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

    def recuperarIntegrantesByTandaSalida(self, idTanda):
        """Método para recuperar los integrantes disponibles de una tanda"""
        rows = {}
        try:
            con = lite.connect(self._db)
            cur = con.cursor()

            cur.execute('SELECT tandasalida.idIntegrante, nombre, apellido, pagado FROM tandasalida INNER JOIN integrantes ON tandasalida.idIntegrante = integrantes.idIntegrante WHERE idTandas = ?', (idTanda))
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

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

    def recuperarPeriodicidad(self, idPeriodo = None):
        """Método para recuperar las periodicidades disponibles"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idPeriodo is None):
                cur.execute('SELECT * FROM Periodicidad WHERE idPer = ?', (idPeriodo))
            else:
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

    def actualizarTandaSalida(self, idTanda, idIntegrantes):
        """Método para actualizar los pagos hechos a los tanderos"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            for idInte in idIntegrantes:
                cur.execute("UPDATE TandaSalida SET pagado = 1 WHERE idTandas = ? and idIntegrante = ?", (idTanda, idInte))
            con.commit()
        except Exception, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

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

    def recuperarIntegrantesByTandaEntrada(self, idTanda, pos):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('SELECT * FROM Integrantes AS I INNER JOIN tandaEntrada AS T ON I.idIntegrante = T.idIntegrante AND T.idTandas = ? AND T.pos = ?', (idTanda, pos))
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows

    def actualizarTandaEntrada(self, idTanda, idIntegrantes, pos):
        """Método para actualizar los pagos hechos a los tanderos"""
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            for idInte in idIntegrantes:
                cur.execute("UPDATE TandaEntrada SET pagado = 1 WHERE idTandas = ? and idIntegrante = ? and pos = ?", (idTanda, idInte, pos))
            con.commit()
        except Exception, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

# tanda = tandaController()
# for p in tanda.recuperarPeriodicidad():
#     print p[0], p[1]
# #tanda.recuperarIntegrantes()
# tanda.crearTanda('10', '2016-02-06', '1', '3000')
