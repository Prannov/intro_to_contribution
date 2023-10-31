# import tkinter module
from cProfile import label
from PIL import Image,ImageTk  
from tkinter import *

# make a window
window = Tk()
# specify it's size
window.geometry("1366x700")
 
bg=ImageTk.PhotoImage(file=r"C:\Users\aniru\Pictures\Camera Roll\bg.png")
        
bg_lbl=Label(window,image=bg)
bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)


label8 = Label(window, text="THRIFT BOOK STORE",
               font="times 28 bold")
label8.place(x=650, y=70, anchor="center")

frame=Frame(window,bg="black")
frame.place(x=90,y=90,width=340,height=500)




username=lbl=Label(window,text="name:",font=("algerian",15,"italic"),fg="white",bg="black")
username.place(x=150,y=155)

txtadress=Entry(window,font=("italics",15,"bold"))
txtadress.place(x=120,y=180,width=270)

userphone=lbl=Label(window,text="phone number:",font=("algerian",15,"italic"),fg="white",bg="black")
userphone.place(x=150,y=255)

txtphone=Entry(window,font=("italics",15,"bold"))
txtphone.place(x=120,y=280,width=270)

useraddress=lbl=Label(window,text="address:",font=("algerian",15,"italic"),fg="white",bg="black")
useraddress.place(x=150,y=355)

txtuser=Entry(window,font=("italics",15,"bold"))
txtuser.place(x=120,y=380,width=270)

userland=lbl=Label(window,text="landmark:",font=("algerian",15,"italic"),fg="white",bg="black")
userland.place(x=150,y=455)

txtland=Entry(window,font=("italics",15,"bold"))
txtland.place(x=120,y=480,width=270)







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















def codh():
    pass

cod=Button(window,text="next",command=codh,font=("italics",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
cod.place(x=600,y=600,width=100,height=35)








window.mainloop()

