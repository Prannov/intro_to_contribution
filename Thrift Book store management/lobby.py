from cProfile import label
from email.mime import image
from tkinter import*
from PIL import Image,ImageTk  

window = Tk()
# specify it's size
window.geometry("1366x700")

loginbtn=Button(window,command=window,text="GO TO CART",font=("italics",15,"bold"),bd=3,relief=RIDGE,fg="white",bg="red")
loginbtn.place(x=40,y=20,width=300,height=35)

frame=Frame(window,bg="grey")
frame.place(x=400,y=10,width=940,height=680)

img1=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\oldschool.jfif")
img1=img1.resize((100,100),Image.ANTIALIAS)
photoimage1=ImageTk.PhotoImage(img1)
lblimg1=Label(image=photoimage1,bg='black',borderwidth=0)
lblimg1.place(x=440,y=20,width=100,height=100)
        
get_str1=Label(frame,text="old school",font=("italics",8,"bold"),fg="white",bg="black")
get_str1.place(x=60,y=120)

get_str1=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str1.place(x=60,y=150)

loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=47,y=175,width=90,height=25)


img2=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\ncert.png")
img2=img2.resize((100,100),Image.ANTIALIAS)
photoimage2=ImageTk.PhotoImage(img2)
lblimg2=Label(image=photoimage2,bg='black',borderwidth=0)
lblimg2.place(x=600,y=20,width=100,height=100)
        
get_str2=Label(frame,text="class 12 computer science",font=("italics",8,"bold"),fg="white",bg="black")
get_str2.place(x=175,y=120)

get_str2=Label(frame,text="price=₹99",font=("italics",8,"bold"),fg="white",bg="black")
get_str2.place(x=215,y=150)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=202,y=175,width=90,height=25)


img3=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\hungergames.png")
img3=img3.resize((100,100),Image.ANTIALIAS)
photoimage3=ImageTk.PhotoImage(img3)
lblimg1=Label(image=photoimage3,bg='black',borderwidth=0)
lblimg1.place(x=760,y=20,width=100,height=100)
        
get_str3=Label(frame,text="hunger games",font=("italics",8,"bold"),fg="white",bg="black")
get_str3.place(x=367,y=120)

get_str3=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str3.place(x=375,y=150)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=367,y=175,width=90,height=25)

img4=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\theguestlist.png")
img4=img4.resize((100,100),Image.ANTIALIAS)
photoimage4=ImageTk.PhotoImage(img4)
lblimg1=Label(image=photoimage4,bg='black',borderwidth=0)
lblimg1.place(x=920,y=20,width=100,height=100)
        
get_str4=Label(frame,text="the guest list",font=("italics",8,"bold"),fg="white",bg="black")
get_str4.place(x=530,y=120)

get_str4=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str4.place(x=537,y=150)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=527,y=175,width=90,height=25)

img5=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\thedavincicode.png")
img5=img5.resize((100,100),Image.ANTIALIAS)
photoimage5=ImageTk.PhotoImage(img5)
lblimg1=Label(image=photoimage5,bg='black',borderwidth=0)
lblimg1.place(x=1080,y=20,width=100,height=100)
        
get_str5=Label(frame,text="the da vinci code",font=("italics",8,"bold"),fg="white",bg="black")
get_str5.place(x=680,y=120)

get_str5=Label(frame,text="price=₹99",font=("italics",8,"bold"),fg="white",bg="black")
get_str5.place(x=700,y=150)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=687,y=175,width=90,height=25)

img6=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\finance.png")
img6=img6.resize((100,100),Image.ANTIALIAS)
photoimage6=ImageTk.PhotoImage(img6)
lblimg1=Label(image=photoimage6,bg='black',borderwidth=0)
lblimg1.place(x=1230,y=20,width=100,height=100)
        
get_str6=Label(frame,text="financial intelligence",font=("italics",8,"bold"),fg="white",bg="black")
get_str6.place(x=820,y=120)

get_str6=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str6.place(x=850,y=150)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=837,y=175,width=90,height=25)

img7=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\helloworld.png")
img7=img7.resize((100,100),Image.ANTIALIAS)
photoimage7=ImageTk.PhotoImage(img7)
lblimg1=Label(image=photoimage7,bg='black',borderwidth=0)
lblimg1.place(x=440,y=240,width=100,height=100)
        
get_str7=Label(frame,text="hello world",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=60,y=340)

get_str7=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=60,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=47,y=395,width=90,height=25)

img8=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\wheelchair.png")
img8=img8.resize((100,100),Image.ANTIALIAS)
photoimage8=ImageTk.PhotoImage(img8)
lblimg1=Label(image=photoimage8,bg='black',borderwidth=0)
lblimg1.place(x=600,y=240,width=100,height=100)
        
get_str7=Label(frame,text="the theory of everything",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=175,y=340)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=215,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=202,y=395,width=90,height=25)

img9=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\meltdown.png")
img9=img9.resize((100,100),Image.ANTIALIAS)
photoimage9=ImageTk.PhotoImage(img9)
lblimg1=Label(image=photoimage9,bg='black',borderwidth=0)
lblimg1.place(x=760,y=240,width=100,height=100)
        
get_str7=Label(frame,text="the meltdown",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=367,y=340)

get_str7=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=375,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=367,y=395,width=90,height=25)

img10=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\think.png")
img10=img10.resize((100,100),Image.ANTIALIAS)
photoimage10=ImageTk.PhotoImage(img10)
lblimg1=Label(image=photoimage10,bg='black',borderwidth=0)
lblimg1.place(x=920,y=240,width=100,height=100)
        
get_str7=Label(frame,text="think and grow",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=530,y=340)

get_str7=Label(frame,text="price=₹99",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=537,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=527,y=395,width=90,height=25)

img11=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\buddha.png")
img11=img11.resize((100,100),Image.ANTIALIAS)
photoimage11=ImageTk.PhotoImage(img11)
lblimg1=Label(image=photoimage11,bg='black',borderwidth=0)
lblimg1.place(x=1080,y=240,width=100,height=100)
        
get_str7=Label(frame,text="siddhartha",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=700,y=340)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=700,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=687,y=395,width=90,height=25)

img12=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\end.png")
img12=img12.resize((100,100),Image.ANTIALIAS)
photoimage12=ImageTk.PhotoImage(img12)
lblimg1=Label(image=photoimage12,bg='black',borderwidth=0)
lblimg1.place(x=1230,y=240,width=100,height=100)
        
get_str7=Label(frame,text="it ends with us",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=835,y=340)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=850,y=370)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=837,y=395,width=90,height=25)

img13=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\life.png")
img13=img13.resize((100,100),Image.ANTIALIAS)
photoimage13=ImageTk.PhotoImage(img13)
lblimg1=Label(image=photoimage13,bg='black',borderwidth=0)
lblimg1.place(x=440,y=460,width=100,height=100)
        
get_str7=Label(frame,text="a little life",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=60,y=560)

get_str7=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=57,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=47,y=620,width=90,height=25)

img14=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\belljar.png")
img14=img14.resize((100,100),Image.ANTIALIAS)
photoimage14=ImageTk.PhotoImage(img14)
lblimg1=Label(image=photoimage14,bg='black',borderwidth=0)
lblimg1.place(x=600,y=460,width=100,height=100)
        
get_str7=Label(frame,text="bell jar",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=225,y=560)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=215,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=202,y=620,width=90,height=25)

img15=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\c++.png")
img15=img15.resize((100,100),Image.ANTIALIAS)
photoimage15=ImageTk.PhotoImage(img15)
lblimg1=Label(image=photoimage15,bg='black',borderwidth=0)
lblimg1.place(x=760,y=460,width=100,height=100)
        
get_str7=Label(frame,text="let us c++",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=380,y=560)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=377,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=367,y=620,width=90,height=25)

img16=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\sherlock.png")
img16=img16.resize((100,100),Image.ANTIALIAS)
photoimage16=ImageTk.PhotoImage(img16)
lblimg1=Label(image=photoimage16,bg='black',borderwidth=0)
lblimg1.place(x=920,y=460,width=100,height=100)
        
get_str7=Label(frame,text="sherlock holmes",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=520,y=560)

get_str7=Label(frame,text="price=₹199",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=537,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=527,y=620,width=90,height=25)

img17=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\it.png")
img17=img17.resize((100,100),Image.ANTIALIAS)
photoimage17=ImageTk.PhotoImage(img17)
lblimg1=Label(image=photoimage17,bg='black',borderwidth=0)
lblimg1.place(x=1080,y=460,width=100,height=100)
        
get_str7=Label(frame,text="it",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=720,y=560)

get_str7=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=700,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=687,y=620,width=90,height=25)

img18=Image.open(r"C:\Users\aniru\Pictures\Camera Roll\got.png")
img18=img18.resize((100,100),Image.ANTIALIAS)
photoimage18=ImageTk.PhotoImage(img18)
lblimg1=Label(image=photoimage18,bg='black',borderwidth=0)
lblimg1.place(x=1230,y=460,width=100,height=100)
        
get_str7=Label(frame,text="game of thrones",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=830,y=560)

get_str7=Label(frame,text="price=₹299",font=("italics",8,"bold"),fg="white",bg="black")
get_str7.place(x=850,y=590)


loginbtn=Button(frame,command=window,text="add to cart",font=("italics",10,"bold"),bd=3,relief=RIDGE,fg="white",bg="blue")
loginbtn.place(x=837,y=620,width=90,height=25)






























































































window.mainloop()