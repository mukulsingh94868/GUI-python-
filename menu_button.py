import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
nb = Menubutton(win,text='File')
nb.grid()

nb.menu = Menu(nb)
nb['menu'] = nb.menu

x1 = IntVar()
x2 = IntVar()

nb.menu.add_checkbutton(label='open',variable=x1)
nb.menu.add_checkbutton(label='close',variable=x2)
nb.pack()
win.mainloop()
