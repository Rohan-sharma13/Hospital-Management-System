from tkinter import *
from tkinter import ttk
from tkinter.ttk import Labelframe

from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox
class History:
    def __init__(self,root) :
       self.root=root
       self.root.title("Hospital Management system")
       self.root.geometry("1295x550+230+220")
       
       #*******Title***********
       labl=Label(self.root,text="Full History ",font=("times new roman",30,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
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

       image4=Image.open(r"C:\Users\LENOVO G3\Downloads\images\full_history.jfif")
       image4=image4.resize((1295,550),Image.ANTIALIAS)
       self.photoimag4=ImageTk.PhotoImage(image4)

       lblimg3=Label(self.root,image=self.photoimag4,bd=4,relief=RIDGE)
       lblimg3.place(x=0,y=60,width=1295,height=500)

       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="History",font=("times new roman",12,"bold"),padx=2)
       labelframeleft.place(x=250,y=68,width=800,height=480)
       
       detail_table=Frame(labelframeleft,bd=2,relief=RIDGE)
       detail_table.place(x=0,y=0,width=790,height=400)

       scroll_x=ttk.Scrollbar(detail_table,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(detail_table,orient=VERTICAL)
       self.patient_detail=ttk.Treeview(detail_table,columns=("Patient Id","name","Contact No","Age","Gender","Blood Group","Address","Any Major Disease","Symptoms","diagonsis","medicines","ward_req","ward"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
       
       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

       
       btn_close=Button(labelframeleft,text="CLOSE",bd=5,command=self.close,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_close.place(x=330,y=410,width=100,height=30)
   
       scroll_x.config(command=self.patient_detail.xview)
       scroll_y.config(command=self.patient_detail.yview)
       self.patient_detail.heading("Patient Id",text="Patient ID")
       self.patient_detail.heading("name",text="Name")
       self.patient_detail.heading("Contact No",text="Contact No")
       self.patient_detail.heading("Age",text="Age")
       self.patient_detail.heading("Gender",text="Gender")
       self.patient_detail.heading("Blood Group",text="Blood Group")
       self.patient_detail.heading("Address",text="Adress")
       self.patient_detail.heading("Any Major Disease",text="Major Diesases")
       self.patient_detail.heading("Symptoms",text="Symptoms")
       self.patient_detail.heading("diagonsis",text="Diagonsis")
       self.patient_detail.heading("medicines",text="Medicines")
       self.patient_detail.heading("ward_req",text="Ward Required")
       self.patient_detail.heading("ward",text="Ward")

       self.patient_detail["show"]="headings"

       self.patient_detail.column("Patient Id",width=100)
       self.patient_detail.column("name",width=100)
       self.patient_detail.column("Contact No",width=100)
       self.patient_detail.column("Age",width=100)
       self.patient_detail.column("Gender",width=100)
       self.patient_detail.column("Blood Group",width=100)
       self.patient_detail.column("Address",width=100)
       self.patient_detail.column("Any Major Disease",width=100)
       self.patient_detail.column("Symptoms",width=100)
       self.patient_detail.column("diagonsis",width=100)
       self.patient_detail.column("medicines",width=100)
       self.patient_detail.column("ward_req",width=100)
       self.patient_detail.column("ward",width=100)

       self.patient_detail.pack(fill=BOTH,expand=1)
       self.fatch_data()
   
        
        

    def fatch_data(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root2001",database="registeration_database")
        my_cursor=conn.cursor()  
        my_cursor.execute("select * from patient_data") 
        rows=my_cursor.fetchall()
        if len(rows)!=0:
            self.patient_detail.delete(*self.patient_detail.get_children())
            for i in rows:
                self.patient_detail.insert("",END,values=i)
            conn.commit()
        conn.close()
    def close(self):
        self.root.destroy()
    

              
if __name__=="__main__":
    root=Tk()
    obj=History(root)
    root.mainloop()