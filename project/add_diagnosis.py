from hashlib import blake2b
from sqlite3 import Cursor
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox
class Diagnosis:
    def __init__(self,root) :
       self.root=root
       self.root.title("Hospital Management system")
       self.root.geometry("1295x550+230+220")
       #*********** Varialbles************
       self.var_patient_id=StringVar()
       self.var_symptoms=StringVar()
       self.var_diagonisis=StringVar()
       self.var_medicines=StringVar()
       self.var_ward_req=StringVar()
       self.var_ward=StringVar()
       #*******Title***********
       labl=Label(self.root,text="Diagnosis Information ",font=("times new roman",30,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
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

       image4=Image.open(r"C:\Users\LENOVO G3\Downloads\images\diagnosis.jfif")
       image4=image4.resize((1295,550),Image.ANTIALIAS)
       self.photoimag4=ImageTk.PhotoImage(image4)

       lblimg3=Label(self.root,image=self.photoimag4,bd=4,relief=RIDGE)
       lblimg3.place(x=0,y=60,width=1295,height=500)

       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Diagnosis",font=("times new roman",12,"bold"),padx=2)
       labelframeleft.place(x=250,y=68,width=800,height=480)

       self.search_var=StringVar()
       combo_search=ttk.Combobox(labelframeleft,textvariable=self.search_var,font=("times new roman",17,"bold"),width=10,state="readonly")
       combo_search["values"]=("Contact_No","Patient_ID")
       combo_search.current(0)
       combo_search.place(x=100,y=8)

       self.txt_search=StringVar()
       entry_id=ttk.Entry(labelframeleft,textvariable=self.txt_search,font=("arial",17,'bold'),width=20)
       entry_id.place(x=250,y=7)


       
       btn_search=Button(labelframeleft,text="Search",command=self.search,bg="black",fg="white",bd=4,relief=RAISED)
       btn_search.place(x=520,y=8,width=50,height=33)

       #************* Show Data******************
       table_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
       table_frame.place(x=50,y=50,width=700,height=70)
       scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
       scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
       self.patient_detail=ttk.Treeview(table_frame,columns=("Patient Id","name","Contact No","Age","Gender","Blood Group","Address","Any Major Disease"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

       scroll_x.pack(side=BOTTOM,fill=X)
       scroll_y.pack(side=RIGHT,fill=Y)

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

       self.patient_detail["show"]="headings"
    
       self.patient_detail.column("Patient Id",width=100)
       self.patient_detail.column("name",width=100)
       self.patient_detail.column("Contact No",width=100)
       self.patient_detail.column("Age",width=100)
       self.patient_detail.column("Gender",width=100)
       self.patient_detail.column("Blood Group",width=100)
       self.patient_detail.column("Address",width=100)
       self.patient_detail.column("Any Major Disease",width=100)

       self.patient_detail.pack(fill=BOTH,expand=1)

       lbl_symptom=Label(labelframeleft,text="Symptom's:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_symptom.place(x=50,y=152)
       entry_symtoms=ttk.Entry(labelframeleft,textvariable=self.var_symptoms,font=("arial",17,'bold'),width=15)
       entry_symtoms.place(x=180,y=150)

       lbl_diagnosis=Label(labelframeleft,text="Diagonsis:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_diagnosis.place(x=50,y=222)
       entry_diagnosis=ttk.Entry(labelframeleft,textvariable=self.var_diagonisis,font=("arial",17,'bold'),width=15)
       entry_diagnosis.place(x=180,y=220)

       lbl_medicines=Label(labelframeleft,text="Medicines:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_medicines.place(x=50,y=292)
       entry_medicines=ttk.Entry(labelframeleft,textvariable=self.var_medicines,font=("arial",17,'bold'),width=15)
       entry_medicines.place(x=180,y=290)

       lbl_ward_req=Label(labelframeleft,text="Ward Required:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_ward_req.place(x=440,y=152)

       combo_ward_req=ttk.Combobox(labelframeleft,textvariable=self.var_ward_req,font=("times new roman",15,"bold"),width=7,state="readonly")
       combo_ward_req["values"]=("Yes","No")
       combo_ward_req.current(0)
       combo_ward_req.place(x=620,y=152)

       lbl_ward=Label(labelframeleft,text="Ward:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_ward.place(x=500,y=222)
       
       
       combo_ward=ttk.Combobox(labelframeleft,textvariable=self.var_ward,font=("times new roman",15,"bold"),width=10,state="readonly")
       combo_ward["values"]=("General","Single","Duo")
       combo_ward.current(0)
       combo_ward.place(x=590,y=222)

       lbl_patient_id=Label(labelframeleft,text="Patient ID:",font=("times new roman",17,"bold"),bg="white",fg="black")
       lbl_patient_id.place(x=440,y=292)
       entry_mpatient_id=ttk.Entry(labelframeleft,textvariable=self.var_patient_id,font=("arial",17,'bold'),width=15)
       entry_mpatient_id.place(x=560,y=290)

       btn_save=Button(labelframeleft,text="SAVE",bd=5,command=self.save_data,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_save.place(x=150,y=400,width=100,height=30)

       btn_close=Button(labelframeleft,text="CLOSE",command=self.close,bd=5,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_close.place(x=550,y=400,width=100,height=30)

       btn_reset=Button(labelframeleft,text="RESET",command=self.reset,bd=5,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_reset.place(x=350,y=400,width=100,height=30)

    def search(self):
        conn=mysql.connector.connect(host="localhost",username="root",password="root2001",database="registeration_database")
        my_cursor=conn.cursor()

        my_cursor.execute("select * from patient_data where " +str(self.search_var.get())+" LIKE '%" +str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows)!=0:
            self.patient_detail.delete(*self.patient_detail.get_children())
            for i in rows:
                self.patient_detail.insert("",END,values=i)
            conn.commit()
        conn.close()
    def save_data(self):
        if self.var_symptoms.get()=="" or self.var_diagonisis.get()=="" or self.var_medicines.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
           
                    conn=mysql.connector.connect(host="localhost",username="root",password="root2001",database="registeration_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update  patient_data set Symptoms=%s,diagonsis=%s,medicines=%s,ward_req=%s,ward=%s where Patient_ID=%s",(self.var_symptoms.get(),
                          self.var_diagonisis.get(),
                          self.var_medicines.get(),
                          self.var_ward_req.get(),
                          self.var_ward.get(),
                          self.var_patient_id.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("success","Successfully Saved data",parent=self.root)
    def close(self):
        self.root.destroy()
    def reset(self):
        self.var_symptoms.set(""),
        self.var_diagonisis.set(""),
        self.var_medicines.set(""),
        self.var_patient_id.set(""),
        
if __name__=="__main__":
    root=Tk()
    obj=Diagnosis(root)
    root.mainloop()