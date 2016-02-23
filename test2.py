# import sqlite3 as lite
# import sys
# 
# con = lite.connect('TandaDB.db')
# 
# with con:    
#     
#     cur = con.cursor()    
#     cur.execute("SELECT * FROM Integrantes")
# 
#     rows = cur.fetchall()
# 
#     for row in rows:
#         print row
# from Tkinter import *
# 
# class App:
#     def __init__(self,master):
#         self.var = IntVar()
#         frame = Frame(master)
#         frame.grid()
#         f2 = Frame(master,width=200,height=100)
#         f2.grid(row=0,column=1)
#         button = Checkbutton(frame,text='show',variable=self.var,command=self.fx)
#         button.grid(row=0,column=0)
#         msg2="""I feel bound to give them full satisfaction on this point"""
#         self.v= Message(f2,text=msg2)
#     def fx(self):
#         if self.var.get():
#             self.v.grid(column=1,row=0,sticky=N)
#         else:
#             self.v.grid_remove()
# 
# top = Tk()
# app = App(top)            
# top.mainloop()

# import Tkinter  # tkinter with small t for python 3
# #import ttk  # nicer widgets
# 
# root = Tkinter.Tk()
# 
# mainFrame = Tkinter.Frame(root)
# mainFrame.grid()
# button = Tkinter.Button(mainFrame, text="dummy")
# button.grid()
# 
# 
# entryFrame = Tkinter.Frame(mainFrame, width=454, height=20)
# entryFrame.grid(row=0, column=1)
# 
# # allow the column inside the entryFrame to grow    
# entryFrame.columnconfigure(0, weight=10)  
# 
# # By default the frame will shrink to whatever is inside of it and 
# # ignore width & height. We change that:
# entryFrame.grid_propagate(False)
# # as far as I know you can not set this for x / y separately so you
# # have to choose a proper height for the frame or do something more sophisticated
# 
# # input entry
# inValue = Tkinter.StringVar()
# inValueEntry = Tkinter.Entry(entryFrame, textvariable=inValue)
# inValueEntry.grid(sticky="we")
# 
# 
# root.mainloop()


# from Tkinter import *
# 
# master = Tk()
# 
# Label(text="one").pack()
# 
# separator = Frame(height=2, bd=1, relief=SUNKEN)
# separator.pack(fill=X, padx=5, pady=5)
# 
# Label(text="two").pack()
# 
# mainloop()


# from Tkinter import *
# 
# class Application(Frame):
#     def __init__(self, master=None):
#         Frame.__init__(self, master)
#         self.master.title("Grid Manager")
# 
#         self.master.rowconfigure(0, weight=1)
#         self.master.columnconfigure(0, weight=1)
# 
#         for i in range(5):
#             self.master.button = Button(master, text = "Button {0}".format(i))
#             self.master.button.grid(row=6, column=i, sticky=W+E)
# 
#         self.Frame1 = Frame(master, bg="red")
#         self.Frame1.grid(row = 0, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S) 
#         self.Frame2 = Frame(master, bg="blue")
#         self.Frame2.grid(row = 2, column = 0, rowspan = 3, columnspan = 2, sticky = W+E+N+S)
#         self.Frame3 = Frame(master, bg="green")
#         self.Frame3.grid(row = 0, column = 2, rowspan = 6, columnspan = 3, sticky = W+E+N+S)
# 
# root = Tk()
# app = Application(master=root)
# app.mainloop()



from Tkinter import *
# from Tkinter import ttk

root = Tk()
root.title("Tanda")
content = Frame(root)
frame = Frame(content, borderwidth=5, relief="sunken", width=400, height=200)
namelbl = Label(content, text="Name")
name = Entry(content)

onevar = BooleanVar()
twovar = BooleanVar()
threevar = BooleanVar()
onevar.set(True)
twovar.set(False)
threevar.set(True)

one = Checkbutton(content, text="One", variable=onevar, onvalue=True)
two = Checkbutton(content, text="Two", variable=twovar, onvalue=True)
three = Checkbutton(content, text="Three", variable=threevar, onvalue=True)
ok = Button(content, text="Okay")
cancel = Button(content, text="Cancel")

content.grid(column=0, row=0)
frame.grid(column=0, row=0, columnspan=3, rowspan=2)
namelbl.grid(column=3, row=0, columnspan=2)
name.grid(column=3, row=1, columnspan=2)
one.grid(column=0, row=3)
two.grid(column=1, row=3)
three.grid(column=2, row=3)
ok.grid(column=3, row=3)
cancel.grid(column=4, row=3)

root.mainloop()