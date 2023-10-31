from cProfile import label
from tkinter import*
window = Tk()
# specify it's size
window.geometry("1366x700")



frame=Frame(window,bg="black")
frame.place(x=100,y=90,width=440,height=550)

get_str=Label(frame,text="THRIFT BOOK STORE",font=("italics",20,"bold"),fg="white",bg="black")
get_str.place(x=70,y=40)

finaltxt=Label(frame,text="thank you from",font=("italics",20,"bold"),fg="white",bg="black")
finaltxt.place(x=20,y=90)






window.mainloop()