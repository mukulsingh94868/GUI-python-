import random 
import time
from tkinter import Tk , Button, DISABLED

win = Tk()

for x in range(6):
    for y in range(4):
        button = Button(width = 10,height = 8)
        button.grid(column = x , row = y)  
        button[x,y] = button




win.mainloop()