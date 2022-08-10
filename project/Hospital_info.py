from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox
class hospital_info:
    def __init__(self,root) :
       self.root=root
       self.root.title("Hospital Management system")
       self.root.geometry("1295x550+230+220")
       
       #*******Title***********
       labl=Label(self.root,text="About ",font=("times new roman",30,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
       labl.place(x=0,y=0,width=1295,height=60)
       #*************Logo****************
       image2=Image.open(r"C:\Users\LENOVO G3\Downloads\images\logo4.jfif")
       image2=image2.resize((100,55),Image.ANTIALIAS)
       self.photoimag2=ImageTk.PhotoImage(image2)

       lblimg1=Label(self.root,image=self.photoimag2,bd=4,relief=RIDGE)
       lblimg1.place(x=0,y=0,width=100,height=60)
       
       image3=Image.open(r"C:\Users\LENOVO G3\Downloads\images\logo4.jfif")
       image3=image3.resize((100,55),Image.ANTIALIAS)
       self.photoimag3=ImageTk.PhotoImage(image3)

       lblimg1=Label(self.root,image=self.photoimag3,bd=4,relief=RIDGE)
       lblimg1.place(x=1195,y=0,width=100,height=60)

       image4=Image.open(r"C:\Users\LENOVO G3\Downloads\images\hospital2.jpg")
       image4=image4.resize((1295,550),Image.ANTIALIAS)
       self.photoimag4=ImageTk.PhotoImage(image4)

       lblimg3=Label(self.root,image=self.photoimag4,bd=4,relief=RIDGE)
       lblimg3.place(x=0,y=60,width=1295,height=500)

       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Diagnosis",font=("times new roman",12,"bold"),padx=2)
       labelframeleft.place(x=250,y=68,width=800,height=480)

       image5=Image.open(r"C:\Users\LENOVO G3\Downloads\images\hospital4.jpg")
       image5=image5.resize((785,150),Image.ANTIALIAS)
       self.photoimag5=ImageTk.PhotoImage(image5)
       
       lblimg4=Label(labelframeleft,image=self.photoimag5,bd=4,relief=RIDGE)
       lblimg4.place(x=0,y=0,width=789,height=150)

       lbl_text=Label(labelframeleft,text="Hospital management system is a computer system \nthat helps manage the information \nrelated to health care and aids in the job \ncompletion of health care providers effectively.",font=("times new roman",25,"bold"),bg="lightblue")
       lbl_text.place(x=0,y=170,width=789,height=230)

       btn_close=Button(labelframeleft,text="CLOSE",bd=5,command=self.close,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_close.place(x=330,y=410,width=100,height=30)

    def close(self):
        self.root.destroy()
       

if __name__=="__main__":
    root=Tk()
    obj=hospital_info(root)
    root.mainloop()