import sqlite3 as lite
import sys

class tandaController:
    def __init__(self, db = 'TandaDB.db'):
        self._db = db

    def crearTanda(self, noIntegrantes, fechaInicio, idPeriodo, monto):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Tandas(noIntegrantes, fechaInicio, idPer, monto, finalizada) VALUES(?, ?, ?, ?, ?)', (noIntegrantes, fechaInicio, idPeriodo, monto, 0))
            con.commit()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return True

    def recuperarTandas(self, idTandas):
        try:
            con = lite.connect(self._db)
            cur = con.cursos()
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
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            if not(idTandas is None and idIntegrante is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idTandas = ? and idIntegrante = ?', (idTandas, idIntegrante))
            elif not(idTandas is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idTandas = ?', (idTandas))
            elif not(idIntegrante is None):
                cur.execute('SELECT * FROM TandaSalida WHERE idIntegrante = ?', (idIntegrante))
            else:
                cur.execute('SELECT * FROM TandaSalida')
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

    def insertarTandaEntrada(self, idTandas, idIntegrante):


# tanda = tandaController()
# for p in tanda.recuperarPeriodicidad():
#     print p[0], p[1]
# #tanda.recuperarIntegrantes()
# tanda.crearTanda('10', '2016-02-06', '1', '3000')
