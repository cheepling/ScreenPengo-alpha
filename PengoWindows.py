from tkinter import *
import tkinter as tk
from tkinter import *
from random import *
from time import sleep

window = tk.Tk()
x = 500
frames = 0
base = 730
idlelist = [1, 2, 3, 4, 5, 6, 7, 8]
walk1 = [9, 10]
walk2 = [11, 12]
singlist = [13]
labellist = []

frame = 0
idleframes = [tk.PhotoImage(file=r"./idle4.gif", format = "gif -index %i" %(i)) for i in range(24)]
idleframes2 = [tk.PhotoImage(file=r"./idle5.gif", format = "gif -index %i" %(i)) for i in range(24)]

def idle():
    global frames
    geo = window.winfo_geometry()
    geolist = geo.split('+')
    if frames < 23:
        frames += 0.5
    else:
        frames = 0
    label.config(image='')
    if int(geolist[1]) <= 700:
        label.config(image=idleframes[int(frames)])
    else:
        label.config(image=idleframes2[int(frames)])
    window.after(100, idle)

def makelabel():
    label = label = tk.Label(window, image=idleframes[0], anchor="c")
    return label


#window.overrideredirect(1)
window.overrideredirect(0)
window.config(bg="red")
window.wm_attributes("-transparentcolor", "red")
window.geometry('100x100+'+str(x)+'+730')
window.attributes("-topmost", True)

label = tk.Label(window, bd=0)
label.config(bg="red")
label.pack()


window.after(100, idle)
window.mainloop()

