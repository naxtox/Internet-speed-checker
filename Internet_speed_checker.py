from tkinter import *
from tkinter import messagebox
import pyspeedtest

def one():
    speed = pyspeedtest.SpeedTest("www.google.com")
    a1 = (str(speed.download())+"[Bytes per second]")
    messagebox.showinfo("your internet speed",a1)
root = Tk()
root.title("INTERNET SPEED CHECKER")
root.config(bg="lightblue")
root.geometry("500x250")

Label1 = Label(root,text="Internet speed checker",font=("Arial",30,"bold"),bg="white").pack()
button1 = Button(root, text="Click !",font=("Arial",20,"bold"),bg="white",height=1,width=10,command=one).pack()


root.mainloop()