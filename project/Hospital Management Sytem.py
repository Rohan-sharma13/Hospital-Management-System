from cProfile import label
from cgitb import text
from logging import root
from tkinter import*
from tkinter import ttk
import random
import time
import datetime
from tkinter import messagebox
import mysql.connector

class Hospital:
    def __init__(self,root):
        self.root=root
        self.root.title("Hospital Management System")
        self.root.geometry("1540x800+0+0")
        lbtitle1=Label(self.root,bd=10,relief=GROOVE,text="+ HOSPITAL MANAGEMENT SYSTEM +",fg="white",bg="red",font=("times new romen",50,"bold"))
        lbtitle1.pack(side=TOP,fill=X)

        # **************** DATA FRAME ***************
        dataframe=Frame(self.root,bd=20,relief=RIDGE)
        dataframe.place(x=0,y=130,width=1530,height=400)

        dataframeLeft=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20
        ,font=("arial",12,"bold"),text="PATIENT INFORTMATION")
        dataframeLeft.place(x=0,y=5,width=900,height=350 )
        
        dataframeRight=LabelFrame(dataframe,bd=10,relief=RIDGE,padx=20
        ,font=("arial",12,"bold"),text="PRESCRIPTION")
        dataframeRight.place(x=910,y=5,width=580,height=350 )

       
root=Tk()
obj=Hospital(root)
root.mainloop()