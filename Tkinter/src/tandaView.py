# -*- coding: utf-8 -*-
import Tkinter
import tkMessageBox
import tandaController as t
# Python modules have been installed and Homebrew's site-packages is not
# in your Python sys.path, so you will not be able to import the modules
# this formula installed. If you plan to develop with these modules,
# please run:
#   mkdir -p /Users/dariojimenez/Library/Python/2.7/lib/python/site-packages
#   echo 'import site; site.addsitedir("/usr/local/lib/python2.7/site-packages")' >> /Users/dariojimenez/Library/Python/2.7/lib/python/site-packages/homebrew.pth

class tandaView:
    def __init__(self, master):
        self._master = master
        self._master.geometry("200x300")
        self._master.title("Tanda")

        frameButtons = Tkinter.Frame(self._master)
        frameVersion = Tkinter.Frame(self._master)

        buttonNew = Tkinter.Button(frameButtons, text = "Nueva Tanda", command = self.crearTanda)
        buttonView = Tkinter.Button(frameButtons, text = "Tandas", command = self.crearTanda)
        buttonIntegrantes = Tkinter.Button(frameButtons, text = "Integrantes", command = self.crearIntegrantes)
        labelVersion = Tkinter.Label(frameVersion, text = "Tandas v1.0")

        frameButtons.grid(row = 0)
        frameVersion.grid(row = 1)
        buttonNew.grid(row = 0, column = 0, padx = 50, pady = 15)
        buttonView.grid(row = 1, column = 0, padx = 50, pady = 15)
        buttonIntegrantes.grid(row = 2, column = 0, padx = 50, pady = 15)
        # labelVersion.grid(row = 3, column = 0, padx = 50, pady = 90)
        labelVersion.pack(fill = Tkinter.BOTH, side = Tkinter.BOTTOM)
        self._master.mainloop()

    def crearTanda(self):
        top = Tkinter.Toplevel(self._master)

        labelIntegrantes = Tkinter.Label(top, text = 'Integrantes')
        entryIntegrantes = Tkinter.Entry(top)
        labelFechaInicio = Tkinter.Label(top, text = 'Fecha de Inicio')
        entryFechaInicio = Tkinter.Entry(top)

        labelIntegrantes.grid(row = 0, column = 0)
        entryIntegrantes.grid(row = 0, column = 1)
        labelFechaInicio.grid(row = 1, column = 0)
        entryFechaInicio.grid(row = 1, column = 1)

        self._master.wait_window(top)

    def crearIntegrantes(self):
        integrante = IntegranteView(self._master)

    def destroyCrearTanda(self):
        self._crearTanda.destroy()


#     def helloCallBack():
#         tkMessageBox.showinfo( "Hello Python", "Hello World")

class IntegranteView:
    """Clase para generar una pantalla de integrantes"""
    def __init__(self, master):

        self._integrante = Tkinter.Toplevel(master)
        self._integrante.title("Integrantes")

        self._nombre = Tkinter.StringVar()
        self._apellido = Tkinter.StringVar()
        self._tel = Tkinter.StringVar()

        labelNombre = Tkinter.Label(self._integrante, text = 'Nombre')
        entryNombre = Tkinter.Entry(self._integrante, textvariable = self._nombre)
        labelApellido = Tkinter.Label(self._integrante, text = 'Apellido')
        entryApellido = Tkinter.Entry(self._integrante, textvariable = self._apellido)
        labelTel = Tkinter.Label(self._integrante, text = 'Teléfono')
        entryTel = Tkinter.Entry(self._integrante, textvariable = self._tel)

        buttonCrear = Tkinter.Button(self._integrante, text = "Crear", command = self.crearIntegrante)
        buttonCancelar = Tkinter.Button(self._integrante, text = "Cancelar", command = self.cancel)

        labelNombre.grid(row = 0, column = 0)
        entryNombre.grid(row = 0, column = 1)
        labelApellido.grid(row = 1, column = 0)
        entryApellido.grid(row = 1, column = 1)
        labelTel.grid(row = 2, column = 0)
        entryTel.grid(row = 2, column = 1)
        buttonCrear.grid(row = 3, column = 0, pady = 10)
        buttonCancelar.grid(row = 3, column = 1, pady = 10)

        master.wait_window(self._integrante)

    def crearIntegrante(self):
        tandaControl = t.tandaController()
        if tandaControl.insertarIntegrante(self._nombre.get(), self._apellido.get(), self._tel.get()):
            tkMessageBox.showinfo( "Información", "Se agregó el integrante correctamente")
            self.limpiarCampos()
            self._integrante.update_idletasks()


    def cancel(self):
        self._integrante.destroy()

    def limpiarCampos(self):
        self._nombre.set("")
        self._apellido.set("")
        self._tel.set("")

top = Tkinter.Tk()
tandaView(top)
