import tkinter
from tkinter import *
from functools import partial

win = Tk()
win.geometry("400x400")

def sum(label,x1,x2):
    n1 = (x1.get())
    n2 = (x2.get())
    sum = int(n1) + int(n2)
    label.config(text='sum is: %d' %sum)
    return
l1 = Label(win,text='First no')
l1.grid(row=1,column=0)

l1 = Label(win,text='Second no')
l1.grid(row=2,column=0)

label = Label(win)
label.grid(row=6,column=2)

x1 = StringVar()
x2 = StringVar()

e1 = Entry(win,textvariable=x1)
e1.grid(row=1,column=2)

e2 = Entry(win,textvariable=x2)
e2.grid(row=2,column=2)

sum = partial(sum, label,x1,x2)

button = Button(win,text='calculate', command=sum)
button.grid(row=3,column=0)
win.mainloop()

