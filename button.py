import tkinter
from tkinter import *

win = Tk()
win.geometry("400x400")

def pr():
    print('hi')
    
b = Button(win, text='button' , command=pr , padx=20,pady=50 , activeforeground='red')
b.place(x=100,y=200)



win.mainloop()
