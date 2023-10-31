from dataclasses import InitVar
from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        
from tkinter import messagebox
import os


class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("REGISTER")
        self.root.geometry("1366x700+0+0")

        self.var_firname=StringVar()
        self.var_connum=StringVar()
        self.var_pass=StringVar()
        self.var_lname=StringVar()
        self.var_email=StringVar()
        self.var_confpass=StringVar()
        self.var_secq=StringVar()
        self.var_seca=StringVar()
    
         
        
        
        
        
        
        
        
        
        
        
        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\aniru\Pictures\Camera Roll\regidterbg.jpg")
        
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        self.bg1=ImageTk.PhotoImage(file=r"C:\Users\aniru\Pictures\Camera Roll\leftbg3.jpg")
        
        left_lbl=Label(self.root,image=self.bg1)
        left_lbl.place(x=50,y=100,width=470,height=550)

        frame=Frame(self.root,bg="antiquewhite4")
        frame.place(x=520,y=100,width=700,height=550)

        get_str=Label(frame,text="REGISTER HERE :",font=("italics",20,"bold"),fg="white",bg="antiquewhite4")
        get_str.place(x=50,y=30)

        username=Label(frame,text="FIRST NAME :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=50,y=85)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_firname,font=("italics",15,"bold"))
        self.txtuser.place(x=50,y=120,width=270)

        username=Label(frame,text="CONTACT NUMBER :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=50,y=180)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_connum,font=("italics",15,"bold"))
        self.txtuser.place(x=50,y=220,width=270)


        username=Label(frame,text="PASSWORD :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=50,y=285)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_pass,font=("italics",15,"bold"),show='*')
        self.txtuser.place(x=50,y=320,width=270)

        username=Label(frame,text="LAST NAME :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=400,y=85)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_lname,font=("italics",15,"bold"))
        self.txtuser.place(x=400,y=120,width=270)

        username=Label(frame,text="EMAIL ID :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=400,y=180)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_email,font=("italics",15,"bold"))
        self.txtuser.place(x=400,y=220,width=270)


        username=Label(frame,text="CONFIRM PASSWORD :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=400,y=285)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_confpass,font=("italics",15,"bold"),show='*')
        self.txtuser.place(x=400,y=320,width=270)
        

        self.var_check=IntVar()
        self.checkbtn=Checkbutton(frame,variable=self.var_check,text="i agree to all terms and conditions",font=("italics",15,"bold"),onvalue=1,offvalue=0)
        self.checkbtn.place(x=20,y=480,width=350,height=20)

        username=Label(frame,text="SECURITY ANSWER :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=400,y=385)
        self.txtuser=ttk.Entry(frame,textvariable=self.var_seca,font=("italics",15,"bold"))
        self.txtuser.place(x=400,y=420,width=270)


        username=Label(frame,text="SECURITY QUESTION :",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        username.place(x=50,y=385)

        self.combo_security_Q=ttk.Combobox(frame,textvariable=self.var_secq,font=("italics",15,"bold"),state="readonly")
        self.combo_security_Q["values"]=("select","your fathers name","your mothers name")
        self.combo_security_Q.place(x=50,y=420,width=270)
        self.combo_security_Q.current(0)

        img2=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\registernow.jpg")
        img2=img2.resize((80,80),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        b1=Button(frame,image=self.photoimage2,command=self.register_data,borderwidth=0,cursor="hand2",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        b1.place(x=400,y=460,width=100,height=80)

        
        get_str=Label(frame,text="OR",font=("italics",20,"bold"),fg="white",bg="antiquewhite4")
        get_str.place(x=500,y=480)



        img3=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\login2.jpg")
        img3=img3.resize((80,80),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        b1=Button(frame,image=self.photoimage3,borderwidth=0,cursor="hand2",font=("italics",15,"bold"),fg="white",bg="antiquewhite4")
        b1.place(x=550,y=460,width=100,height=80)



    def register_data(self):
        if self.var_firname.get()=="" or self.var_email.get()=="" or self.var_secq.get()=="select":
            messagebox.showerror("error","all fields required")
        elif self.var_pass.get()!=self.var_confpass.get():
            messagebox.showerror("error","passwords must be same")    
        elif self.var_check.get()==0:
            messagebox.showerror("error","t and c not viewed")
        else:
            messagebox.showinfo("sucess","welcome to thrift bookstore")













if __name__ == "__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()