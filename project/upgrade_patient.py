from fileinput import close
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Labelframe
from PIL import Image,ImageTk
import mysql.connector
import random
from tkinter import messagebox
class Upgrade:
    def __init__(self,root) :
       self.root=root
       self.root.title("Hospital Management system")
       self.root.geometry("1295x550+230+220")
       self.var_Id=StringVar()
       self.var_Name=StringVar()
       self.var_contact=StringVar()
       self.var_age=StringVar()
       self.var_gender=StringVar()
       self.var_blood=StringVar()
       self.var_address=StringVar()
       self.var_major_disease=StringVar()
        #*******Title***********
       labl=Label(self.root,text="Upgrade Patient Details",font=("times new roman",30,"bold"),bg="black",fg="white",bd=4,relief=RIDGE)
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
       #****************Label frame***********
       image4=Image.open(r"C:\Users\LENOVO G3\Downloads\images\upgrade.jfif")
       image4=image4.resize((1295,550),Image.ANTIALIAS)
       self.photoimag4=ImageTk.PhotoImage(image4)

       lblimg3=Label(self.root,image=self.photoimag4,bd=4,relief=RIDGE)
       lblimg3.place(x=0,y=60,width=1295,height=500)

       labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="Upgrade",font=("times new roman",12,"bold"),padx=2)
       labelframeleft.place(x=350,y=68,width=600,height=470)

       #************** Label Entry************
       lbl_patient_id=Label(labelframeleft,text="Pateint ID:",font=("times new roman",17,"bold"),padx=2,pady=6)
       lbl_patient_id.grid(row=0,column=0)
       entry_id=ttk.Entry(labelframeleft,textvariable=self.var_Id,font=("arial",17,'bold'),width=33)
       entry_id.grid(row=0,column=1)

       lbl_patient_name=Label(labelframeleft,text="Name:",font=("times new roman",17,"bold"),padx=25,pady=6)
       lbl_patient_name.grid(row=1,column=0,sticky=W)
       entry_name=ttk.Entry(labelframeleft,textvariable=self.var_Name,font=("arial",17,"bold"),width=33)
       entry_name.grid(row=1,column=1)

       lbl_patient_coontact=Label(labelframeleft,text="Contact No:",font=("times new roman",17,"bold"),padx=2,pady=6)
       lbl_patient_coontact.grid(row=2,column=0,sticky=W)
       entry_coontact=ttk.Entry(labelframeleft,textvariable=self.var_contact,font=("arial",17,"bold"),width=33)
       entry_coontact.grid(row=2,column=1)

       lbl_patient_Age=Label(labelframeleft,text="Age:",font=("times new roman",17,"bold"),padx=30,pady=6)
       lbl_patient_Age.grid(row=3,column=0,sticky=W)
       entry_Age=ttk.Entry(labelframeleft,textvariable=self.var_age,font=("arial",17,"bold"),width=33)
       entry_Age.grid(row=3,column=1)

       lbl_patient_Gender=Label(labelframeleft,text="Gender:",font=("times new roman",17,"bold"),padx=15,pady=6)
       lbl_patient_Gender.grid(row=4,column=0,sticky=W)
    
       combo_gender=ttk.Combobox(labelframeleft,textvariable=self.var_gender,font=("times new roman",12,"bold"),width=50,state="randomly")
       combo_gender["values"]=("Male","Female","Other")
       combo_gender.current(0)
       combo_gender.grid(row=4,column=1)

       lbl_patient_blood=Label(labelframeleft,text="Blood Group:",font=("times new roman",17,"bold"),padx=2,pady=6)
       lbl_patient_blood.grid(row=5,column=0,sticky=W)
       entry_blood=ttk.Entry(labelframeleft,textvariable=self.var_blood,font=("arial",17,"bold"),width=33)
       entry_blood.grid(row=5,column=1)

       lbl_patient_Address=Label(labelframeleft,text="Address:",font=("times new roman",17,"bold"),padx=10,pady=6)
       lbl_patient_Address.grid(row=6,column=0,sticky=W)
       entry_Address=ttk.Entry(labelframeleft,textvariable=self.var_address,font=("arial",17,"bold"),width=33)
       entry_Address.grid(row=6,column=1)

       lbl_patient_major=Label(labelframeleft,text="Any Major disease Suffered Before:",font=("times new roman",17,"bold"))
       lbl_patient_major.place(x=10,y=290)
       entry_major=ttk.Entry(labelframeleft,textvariable=self.var_major_disease,font=("arial",17,"bold"),width=33)
       entry_major.place(x=10,y=330,width=580)

       btn_save=Button(labelframeleft,text="Upgrade",command=self.save_data,bd=5,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_save.place(x=50,y=400,width=100,height=30)

       btn_close=Button(labelframeleft,text="CLOSE",bd=5,command=self.close,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_close.place(x=250,y=400,width=100,height=30)

       btn_reset=Button(labelframeleft,text="RESET",command=self.reset,bd=5,relief=RAISED,bg="black",fg="white",font=("arial",15,"bold"),cursor="hand2")
       btn_reset.place(x=450,y=400,width=100,height=30)
    def save_data(self):
        if self.var_Id.get()=="" or self.var_Name.get()=="" or self.var_contact.get()=="":
            messagebox.showerror("Error","All fields are Required",parent=self.root)
        else:
           
                    conn=mysql.connector.connect(host="localhost",username="root",password="root2001",database="registeration_database")
                    my_cursor=conn.cursor()
                    my_cursor.execute("update  patient_data set Name=%s, Contact_No=%s, Age=%s, Gender=%s, Blood_Group=%s, Address=%s, Major_disease=%s where Patient_ID=%s",(
                       self.var_Name.get(),
                       self.var_contact.get(),
                       self.var_age.get(),
                       self.var_gender.get(),
                       self.var_blood.get(),
                       self.var_address.get(),
                       self.var_major_disease.get(),
                       self.var_Id.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo("success","Successfully Saved data",parent=self.root)
    def close(self):
        self.root.destroy()
    def reset(self):
        self.var_Id.set("")
        self.var_Name.set(""),
        self.var_contact.set(""),
        self.var_age.set(""),
        self.var_blood.set(""),
        self.var_address.set(""),
        self.var_major_disease.set(""),
       


if __name__=="__main__":
    root=Tk()
    obj=Upgrade(root)
    root.mainloop()