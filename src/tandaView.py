import Tkinter
import tkMessageBox
import tanda

class tandaView:
    def __init__(self, master):
        self._master = master
        self._master.title("Tanda")

        buttonNew = Tkinter.Button(self._master, text = "Nueva T", command = self.crearTanda)
        buttonView = Tkinter.Button(self._master, text = "Mostrar T", command = self.crearTanda)

        buttonNew.grid(row = 0, column = 0, padx = 50)
        buttonView.grid(row = 1, column = 0, padx = 50)
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

    def destroyCrearTanda(self):
        self._crearTanda.destroy()


#     def helloCallBack():
#         tkMessageBox.showinfo( "Hello Python", "Hello World")

top = Tkinter.Tk()
tandaView(top)
# tanda.Tanda()
