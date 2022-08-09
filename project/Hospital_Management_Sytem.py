from ast import Import
from cProfile import label
from cgitb import text
from http.client import ImproperConnectionState
from logging import root
from tkinter import*
from tkinter import ttk
from new_patient_data import New_data
from add_diagnosis import Diagnosis
from Full_history import History
from Hospital_info import hospital_info
from upgrade_patient import  Upgrade
import random
import time
import datetime
from tkinter import messagebox
from turtle import width
from PIL import Image,ImageTk
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")

        image1=Image.open(r"C:\Users\LENOVO G3\Downloads\images\sign.jpg")
        image1=image1.resize((1550,140),Image.ANTIALIAS)
        self.photoimag=ImageTk.PhotoImage(image1)

        lblimg=Label(self.root,image=self.photoimag,bd=4,relief=RIDGE)
        lblimg.place(x=0,y=0,width=1550,height=140)
        
        #**************title HMS*****************
        lbl_title=Label(self.root,text="HOSPITAL MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="black",bd=4,relief=RIDGE)
        lbl_title.place(x=226,y=140,width=1320,height=50)


        #***********LOGO******************************
        image2=Image.open(r"C:\Users\LENOVO G3\Downloads\images\logo3.png")
        image2=image2.resize((230,180),Image.ANTIALIAS)
        self.photoimag2=ImageTk.PhotoImage(image2)

        lblimg1=Label(self.root,image=self.photoimag2,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=230,height=190)
        #*************Frame***************
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=190,width=1535,height=600)
        #***********MENU***************
        lbl_menu=Label(main_frame,text="Menu",font=("times new roman",30,"bold"),bg="black",fg="white",relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=225,height=70)
        
        btn_frame=Frame(main_frame,bd=4,relief=RIDGE)
        btn_frame.place(x=0,y=75,width=225,height=530)

        new_patient_record=Button(btn_frame,text="Add New Patient Record",command=self.patient_data,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        new_patient_record.grid(row=0,column=0,pady=3)

        patient_info=Button(btn_frame,text="Diagnosis Information",command=self.patient_diagnosis,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        patient_info.grid(row=1,column=0,pady=3)

        patient_full_history=Button(btn_frame,text="Full History of Patient",command=self.patient_History,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        patient_full_history.grid(row=2,column=0,pady=3)

        update_record=Button(btn_frame,text="Update Patient Record",command=self.upgrade_info,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        update_record.grid(row=3,column=0,pady=3)

        hospital_info=Button(btn_frame,text="Hospital Information",command=self.hospital_info,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        hospital_info.grid(row=4,column=0,pady=3)

        logout_btn=Button(btn_frame,text="Logout",command=self.logout,width=19,height=3,relief=RAISED,font=("times new roman",14,"bold"),bg="lightblue4",fg="white",bd=0,cursor="hand2")
        logout_btn.grid(row=5,column=0,pady=3)
        #********** Right side image***************
        
        image3=Image.open(r"C:\Users\LENOVO G3\Downloads\images\right.jpg")
        image3=image3.resize((1310,600),Image.ANTIALIAS)
        self.photoimag1=ImageTk.PhotoImage(image3)

        lblimg2=Label(self.root,image=self.photoimag1,bd=4,relief=RIDGE)
        lblimg2.place(x=225,y=190,width=1310,height=600)
        
    def patient_data(self):
        self.new_window=Toplevel(self.root)
        self.app=New_data(self.new_window)
    def patient_diagnosis(self):
        self.new_window=Toplevel(self.root)
        self.app=Diagnosis(self.new_window)
    def patient_History(self):
        self.new_window=Toplevel(self.root)
        self.app=History(self.new_window)
    def hospital_info(self):
        self.new_window=Toplevel(self.root)
        self.app=hospital_info(self.new_window)
    def upgrade_info(self):
        self.new_window=Toplevel(self.root)
        self.app=Upgrade(self.new_window)

    def logout(self):
        self.root.destroy()
            

















root=Tk()
obj=Hospital(root)
root.mainloop()