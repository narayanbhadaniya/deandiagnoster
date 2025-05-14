from tkinter.ttk import Progressbar
import time
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os

window=Tk()
window.title("Bus Pass System")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-300
h=window.winfo_screenheight()-200
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
window.geometry("%dx%d"%(sw,sh))
window.maxsize(1600,1000)

bg=ImageTk.PhotoImage(file="Image\\Medi2.jpeg")
bgl=Label(window,image=bg)
bgl.place(x=0,y=0)


def display():
    for i in range(1,11):
        window.update_idletasks()
        P['value']+=10
        time.sleep(0.5)
        L['text']=P['value'],'%'
        L.config(bg="white")
        
    window.destroy()
    os.system("Login.py")


L1=Label(window,text="WELCOME TO MEDICAPS BUS SERVICE",width=0,height=0,font=("Comic Sans Ms",30,"bold"))
L1.config(fg="Black")
L1.place(x=400,y=10)

L2=Label(window,text="Version-1.0",width=0,height=0,font=("Comic Sans Ms",10,"bold"))
L2.config(bg="white",fg="Black")
L2.place(x=1400,y=750)

Load=Label(window,text="Loading ",width=0,height=0,font=("Comic Sans Ms",15,"bold"))
Load.place(x=750,y=750)

L=Label(window,font=("Comic Sans Ms",15,"bold"))
L.place(x=840,y=750)

P=Progressbar(window,orient=HORIZONTAL,length=300,mode='determinate',value=0)
P.place(x=670,y=720)

display()
window.mainloop()
