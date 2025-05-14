from tkinter import messagebox
from tkinter.ttk import Progressbar
import time
from tkinter import *
import tkinter as tk
from PIL import Image,ImageTk
import os
window=Tk()
window.title("Login to Medicaps")
window.config(bg="skyblue")

w=window.winfo_screenwidth()-800
h=window.winfo_screenheight()-400
sw=window.winfo_screenwidth()
sh=window.winfo_screenheight()
wpos=(sw/2)-(w/2)
hpos=(sh/2)-(h/2)
window.geometry("%dx%d+%d+%d"%(w,h,wpos,hpos))

bg=ImageTk.PhotoImage(file="Image\\Medilogin.png")
bgl=Label(window,image=bg)
bgl.place(x=-2,y=-3)

def login():
    user=name.get()
    passw=psw.get()

    if user=="admin" and passw=="root":
        messagebox.showinfo("PASSWORD VERIFICATION", "You are login to Medicaps")
        window.destroy()
        os.system('Dashboard.py')
    else:
        messagebox.showinfo("PASSWORD VERIFICATION", "Invalid Username or Password")
        var1.set('')
        var2.set('')
        name.focus()
l1=Label(window,text="LOGIN TO MEDICAPS",font=("comic sans ms",18,"bold"))    
l1.place(x=240,y=10)     
#label
nameL=Label(window,text="Enter Username:",width=0,height=0,font=("comic sans ms",20,"bold"))
nameL.config(bg="Black",fg="White")
nameL.place(x=150,y=150)
passL=Label(window,text="Enter Password :",width=0,height=0,font=("comic sans ms",20,"bold"))
passL.config(bg="Black",fg="White")
passL.place(x=150,y=250)

#entry
var1=StringVar()
name=Entry(window,textvariable=var1,width=16,font=("comic sans ms",18,"bold"))
name.config(bg="white",fg="black")
name.place(x=400,y=150)
var2=StringVar()
psw=Entry(window,textvariable=var2,show="*",width=16,font=("comic sans ms",18,"bold"))
psw.config(bg="white",fg="black")
psw.place(x=400,y=250)

#button
ok=Button(window,text="OK",width=0,height=0,font=("comic sans ms",15,"bold"),command=login)
ok.config(bg="white",fg="black")
ok.place(x=270,y=340)
can=Button(window,text="CANCEL",width=0,height=0,font=("comic sans ms",15,"bold"),command=window.destroy)
can.config(bg="white",fg="black")
can.place(x=370,y=340)

#forgot password
pas=Label(window,text="Forgot Password..?",font=("comic sans ms",12,"bold"))
pas.config(bg="white",fg="red")
pas.place(x=230,y=420)
rst=Button(window,text="Reset Password",width=0,height=0,font=("comic sans ms",9,"bold"),command=window.destroy)
rst.config(bg="white",fg="black")
rst.place(x=400,y=420)

window.mainloop()
