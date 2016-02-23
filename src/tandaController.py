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
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.commit()
                con.close()
                return True

    def recuperarTandas(self):
        try:
            con = lite.connect(self._db)
            cur = con.cursos()
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
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.commit()
                con.close()
                return True

    def recuperarIntegrantes(self):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('SELECT * FROM Integrantes')
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

    def insertarPago(self, idTandas, idIntegrante, periodo, pagado):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('INSERT INTO Pagos(idTandas, idIntegrante, periodo, pagado) VALUES(?, ?, ?, ?)', (idTandas, idIntegrante, periodo, pagado))
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.commit()
                con.close()
                return True

    def recuperarPagos(self):
        try:
            con = lite.connect(self._db)
            cur = con.cursor()
            cur.execute('SELECT * FROM Pagos')
            rows = cur.fetchall()
        except lite.Error, e:
            print "Error %s:" % e.args[0]
            sys.exit(1)
        finally:
            if con:
                con.close()
                return rows


# tanda = tandaController()
# for p in tanda.recuperarPeriodicidad():
#     print p[0], p[1]
# #tanda.recuperarIntegrantes()
# tanda.crearTanda('10', '2016-02-06', '1', '3000')
