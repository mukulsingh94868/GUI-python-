import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")

l1 = Label(win,text='Maths')
l1.place(x=10,y=10)

e1 = Entry(win, bd=5)
e1.place(x=20,y=10)

l2 = Label(win,text='English')
l2.place(x=10,y=12)

e2 = Entry(win, bd=5)
e2.place(x=60,y=64)

b = Button(win,text='submit')
b.place(x=100,y=200)
win.mainloop()
