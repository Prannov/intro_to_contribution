from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk        
from tkinter import messagebox
import os
class window:
    
    def __init__(self,root):
        self.root=root
        self.root.title("NEXT")
        self.root.geometry("1366x700+0+0")

        
        self.bg=ImageTk.PhotoImage(file=r"C:\Users\aniru\Pictures\Camera Roll\bg.png")
        bg_lbl=Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)

        lbl_bg=Label(self.root,image=self.bg)
        lbl_bg.place(x=0,y=0,relwidth=1,relheight=1)

        frame=Frame(self.root,bg="black")
        frame.place(x=500,y=120,width=340,height=450)

        img1=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\log in logo.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lblimg1=Label(image=self.photoimage1,bg='black',borderwidth=0)
        lblimg1.place(x=620,y=124,width=100,height=100)
        
        
        get_str=Label(frame,text="ONLINE BANKING",font=("italics",20,"bold"),fg="white",bg="black")
        get_str.place(x=70,y=100)


        username=lbl=Label(frame,text="CARD NUMBER",font=("italics",15,"bold"),fg="white",bg="black")
        username.place(x=70,y=155)

        self.txtuser=ttk.Entry(frame,font=("italics",15,"bold"))
        self.txtuser.place(x=40,y=180,width=270)

        password=lbl=Label(frame,text="PIN",font=("italics",15,"bold"),fg="white",bg="black")
        password.place(x=70,y=225)


        self.txtpass=ttk.Entry(frame,font=("italics",15,"bold"),show='*')
        self.txtpass.place(x=40,y=250,width=270)

        img2=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\username.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lblimg2=Label(image=self.photoimage2,bg='black',borderwidth=0)
        lblimg2.place(x=510,y=303,width=25,height=25)

        
        img3=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\download.jfif")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lblimg3=Label(image=self.photoimage3,bg='black',borderwidth=0)
        lblimg3.place(x=510,y=371,width=25,height=25)
    
        loginbtn=Button(frame,command=self.login,text="NEXT",font=("italics",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
        loginbtn.place(x=110,y=300,width=120,height=35)


       

       

    def login(self):
        if self.txtuser.get()=="" or self.txtpass.get()=="":
            messagebox.showerror("error","all field required")
        elif  len (self.txtuser.get())==16 and len(self.txtpass.get())==4:
            try:
                txtu=int(self.txtuser.get())
                txtp=int(self.txtpass.get())
                if(txtu)>-1 and txtp>-1:
                    messagebox.showinfo("success","payment successful")
            except ValueError:
                messagebox.showerror("invalid","invalid card number or pin")
                
        else:
            messagebox.showerror("invalid","invalid card number or pin")





if __name__ == "__main__":
    root=Tk()
    app=window(root)
    root.mainloop()
