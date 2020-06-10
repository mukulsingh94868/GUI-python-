import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")
c1 = IntVar()
c2 = IntVar()
cb = Checkbutton(win, text='Music' , offvalue=0 , onvalue=1 , height=5 , width=10, variable=c1)
cb.pack()

cb2 = Checkbutton(win, text='Value' , offvalue=0 , onvalue=1 , height=5 , width=10, variable=c2)
cb2.pack()
var = IntVar()
r1 = RadioButton(win, text='option1' , variable=var , value=1)
r1.pack()

r2 = RadioButton(win, text='option2' , variable=var , value=1)
r2.pack()

r3 = RadioButton(win, text='option3' , variable=var , value=1)
r3.pack()
win.mainloop()
