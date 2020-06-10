import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
lb = Listbox(win)
lb.insert(1,'python')
lb.insert(2,'c')
lb.insert(3,'c++')
lb.insert(4,'jquery')
lb.insert(5,'ruby')

lb.pack()




win.mainloop()
