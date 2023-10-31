# import tkinter module
from tkinter import *
from PIL import Image,ImageTk  
import os
# make a window
window = Tk()
# specify it's size
window.geometry("1366x700")
bg=ImageTk.PhotoImage(file=r"C:\Users\aniru\Pictures\Camera Roll\bg.png")
        
bg_lbl=Label(window,image=bg)
bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
 
frame=Frame(window,bg="black")
frame.place(x=100,y=90,width=440,height=550)

get_str=Label(frame,text="THRIFT BOOK STORE",font=("italics",20,"bold"),fg="white",bg="black")
get_str.place(x=70,y=40)
get_str1=Label(frame,text="welcome to thrift book store",font=("italics",20,"bold"),fg="white",bg="black")
get_str1.place(x=22,y=90)

get_str2=Label(frame,text="where we provide the customer",font=("italics",20,"bold"),fg="white",bg="black")
get_str2.place(x=15,y=130)
















frame=Frame(window,bg="black")
frame.place(x=888,y=90,width=340,height=500)






reciepttitle=Label(window,text="RECIEPT",font=("algerian",20,"underline"))
reciepttitle.place(x=1000,y=100)

bookstitle=Label(window,text="BOOKS",font=("algerian",15,"underline"))
bookstitle.place(x=900,y=150)

pricetitle=Label(window,text="PRICE",font=("algerian",15,"underline"))
pricetitle.place(x=1150,y=150)

totaltitle=Label(window,text="TOTAL",font=("algerian",15,"underline"))
totaltitle.place(x=900,y=500)



label8 = Label(window, text="THRIFT BOOK STORE",
               font="times 28 bold")
label8.place(x=650, y=20, anchor="center")

def codh():
    
    cmd="cash_on_del.py"   
    
    os.system(cmd)

cod=Button(window,text="cash on delivery",command=codh,font=("italics",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
cod.place(x=800,y=600)

def upih():
    cmd="upi.py"
    os.system(cmd)

upi=Button(window,text="upi",command=upih,font=("italics",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
upi.place(x=1050,y=600)




window.mainloop()

