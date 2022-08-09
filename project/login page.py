from ast import Raise
from cProfile import label
from logging import root
from tkinter import *
from tkinter import ttk
import random
import time
import datetime
from new_patient_data import New_data
from add_diagnosis import Diagnosis
from Full_history import History
from Hospital_info import hospital_info
from upgrade_patient import  Upgrade
from tkinter import Entry, Tk
from turtle import bgcolor
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
def main():
    win=Tk()
    app=login_window(win)
    win.mainloop()
class login_window:
    def __init__(self,root):
        self.root=root
        self.root.title("Login")
        self.root.geometry("1580x800+0+0")   
        
        self.bg=Image.open(r"C:\Users\LENOVO G3\Downloads\images\hospital3.jpg")
        resized=self.bg.resize((1580,800),Image.ANTIALIAS)
        self.bg1= ImageTk.PhotoImage(resized)
        lb1_bg=Label(self.root,image=self.bg1)
        lb1_bg.place(x=0,y=0,relwidth=1,relheight=1)
        frame=Frame(self.root,bg="white")
        frame.place(x=610,y=170,width=340,height=450)

        img1=Image.open(r"C:\Users\LENOVO G3\Downloads\images\loginimage.png")
        img1=img1.resize((100,100),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(img1)
        lbimg1=Label(image=self.photoimage1,bg="white",borderwidth=0)
        lbimg1.place(x=730,y=175,width=100,height=100)
        
        get_str=Label(frame,text="GET STARTED",font=("times new roman",20,"bold"),fg="black",bg="white")
        get_str.place(x=70,y=100)
        #label 
        username=Label(frame,text="E-Mail",font=("times new roman",15,"bold"),fg="black",bg="white")
        username.place(x=65,y=145)
        
        self.textuser=ttk.Entry(frame,font=("time new roman",15,"bold"))
        self.textuser.place(x=40,y=173,width=270)

        password=Label(frame,text="Password",font=("times new roman",15,"bold"),fg="black",bg="white")
        password.place(x=65,y=215)

        self.textuser1=ttk.Entry(frame,font=("time new roman",15,"bold"),show="*")
        self.textuser1.place(x=40,y=245,width=270)
        #logo
        img2=Image.open(r"C:\Users\LENOVO G3\Downloads\images\logo1.png")
        img2=img2.resize((25,25),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(img2)
        lbimg2=Label(frame,image=self.photoimage2,borderwidth=0)
        lbimg2.place(x=39,y=145,width=25,height=25)

        img3=Image.open(r"C:\Users\LENOVO G3\Downloads\images\logo2.jpg")
        img3=img3.resize((25,25),Image.ANTIALIAS)
        self.photoimage3=ImageTk.PhotoImage(img3)
        lbimg3=Label(frame,image=self.photoimage3,borderwidth=0)
        lbimg3.place(x=39,y=215,width=25,height=25)
       #login button
        
        loginbtn=Button(frame,text="LOGIN",font=("times new roman",15,"bold"),bd=3,relief=RIDGE,command=self.login,fg="black",bg="white",activebackground="white",activeforeground="black")
        loginbtn.place(x=110,y=300,width=120,height=35)
     # REGISTRATION BUTTON
        registerbtn=Button(frame,text="New user Register",command=self.register_window,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activebackground="white",activeforeground="black")
        registerbtn.place(x=-50,y=340,width=240,height=35)
       
    # FORGET PASSWORD
        forgetbtn=Button(frame,text="Forget Password",command=self.forget_password,font=("times new roman",10,"bold"),borderwidth=0,fg="black",bg="white",activebackground="white",activeforeground="black")
        forgetbtn.place(x=-55,y=365,width=240,height=35)
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Register(self.new_window)


    def login(self):
        if self.textuser.get()==""or self.textuser1.get()=="":
            messagebox.showerror("Error","All fields Required")
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="root2001",database="registeration_database")
           my_cursor=conn.cursor()
           my_cursor.execute("select * from register where email=%s and password=%s",(
            self.textuser.get(),
            self.textuser1.get(),
           ))
           row=my_cursor.fetchone()
           if row== None:
            messagebox.showerror("Error","Invailed Username & Password")
           else:
            open_main=messagebox.askyesno("YesNo","Access only admin")
            if open_main>0:
                self.new_window=Toplevel(self.root)
                self.app=Hospital(self.new_window)
            else:
                if not open_main:
                    return

           conn.commit()
           conn.close()  
           # **************Reset Password***********************
    def reset_password(self):
        if self.combo_scty.get()=="select":
            messagebox.showerror("Error","Select Security Question",parent=self.root2)
        elif self.entry_sctyans.get()=="":
            messagebox.showerror("Error","Enter Security Answer",parent=self.root2)
        elif self.entry_new_pass.get()=="":
            messagebox.showerror("Error","Please Enter New Password",parent=self.root2)
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root2001",database="registeration_database")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s and securityQ=%s and securityA=%s")
            value=(self.textuser.get(),self.combo_scty.get(),self.entry_sctyans.get())
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("error","please Enter the Correct Answer",parent=self.root2)
            else:
                query=("update register set password=%s where email=%s")
                value=(self.entry_new_pass.get(),self.textuser.get())
                my_cursor.execute(query,value)
                conn.commit()
                conn.close()
                messagebox.showinfo("info","Your Password has been Reset,PLease Login",parent=self.root2)
                self.root2.destroy()
    def forget_password(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Address to Reset Password")
        else:
            conn=mysql.connector.connect(host="localhost",user="root",password="root2001",database="registeration_database")
            my_cursor=conn.cursor()
            query=("select * from register where email=%s")
            value=(self.textuser.get(),)
            my_cursor.execute(query,value)
            row=my_cursor.fetchone()
            if row==None:
                messagebox.showerror("Error","Please Enter the Valid Email")
            else:
                conn.close()
                self.root2=Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")
                self.root2.config(bg="white")

                lbl1=Label(self.root2,text="Forget Password",font=("times new roman",20,"bold"),fg="black",bg="white",relief=RIDGE)
                lbl1.place(x=0,y=10,relwidth=1)
                sctyques=Label(self.root2,text="Select Security Question:",font=("times new ronam",15,"bold"),bg="white")
                sctyques.place(x=50,y=80)
                self.combo_scty=ttk.Combobox(self.root2,font=("times new roman",13,"bold"),state="readonly")
                self.combo_scty["values"]=("Select","Your Birth Place","Your First school Name","Your Nickname","Your Pet Name")
                self.combo_scty.place(x=50,y=110,width=250)
                self.combo_scty.current(0)

                sctyans=Label(self.root2,text="Security Answer:",font=("times new ronam",15,"bold"),bg="white")
                sctyans.place(x=50,y=150)
                self.entry_sctyans=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.entry_sctyans.place(x=50,y=180,width=250)

                new_pass=Label(self.root2,text="New Password:",font=("times new ronam",15,"bold"),bg="white")
                new_pass.place(x=50,y=220)
                self.entry_new_pass=ttk.Entry(self.root2,font=("times new roman",13,"bold"))
                self.entry_new_pass.place(x=50,y=250,width=250)

                btn=Button(self.root2,text="RESET",command=self.reset_password,font=("times new roman",15,"bold"),bg="blue",fg="white")
                btn.place(x=130,y=290)
     
class Register:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1580x800+0+0")
        #********** Variables**********
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_security_Q=StringVar()
        self.var_security_A=StringVar()
        self.var_Password=StringVar()
        self.var_C_passwoed=StringVar()
        self.var_checkbtn=IntVar()
        
        # *******Background Image********
        bg=Image.open(r"C:\Users\LENOVO G3\Downloads\images\hospital2.jpg")
        bg=bg.resize((1580,800),Image.ANTIALIAS)
        self.bgi=ImageTk.PhotoImage(bg)
        
        bg_lbl=Label(self.root,image=self.bgi)
        bg_lbl.place(x=0,y=0,relwidth=1,relheight=1)
        # *******Left image************
        self.bg2=ImageTk.PhotoImage(file=r"C:\Users\LENOVO G3\Downloads\images\hospital1.jpg")
        left_label=Label(self.root,image=self.bg2)
        left_label.place(x=70,y=100,width=450,height=550)
        # ****** main frame***********
        frame1=Frame(self.root,bg="white")
        frame1.place(x=520,y=100,width=800,height=550)
        register_lbl=Label(frame1,text="REGISTER HERE",font=("times new roman",25,"bold"),fg="black",bg="white")
        register_lbl.place(x=200,y=20)
        # ******* Label & EntryField*******
        fname=Label(frame1,text="First Name:",font=("times new ronam",15,"bold"),bg="white")
        fname.place(x=50,y=100)
        self.entry_fname=ttk.Entry(frame1,textvariable=self.var_fname,font=("times new roman",13,"bold"))
        self.entry_fname.place(x=50,y=130,width=250)

        lname=Label(frame1,text="Last Name:",font=("times new ronam",15,"bold"),bg="white")
        lname.place(x=400,y=100)
        self.entry_lname=ttk.Entry(frame1,textvariable=self.var_lname,font=("times new roman",13,"bold"))
        self.entry_lname.place(x=400,y=130,width=250)

        contact=Label(frame1,text="Contact:",font=("times new ronam",15,"bold"),bg="white")
        contact.place(x=50,y=180)
        entry_contact=ttk.Entry(frame1,textvariable=self.var_contact,font=("times new roman",13,"bold"))
        entry_contact.place(x=50,y=210,width=250)

        e_mail=Label(frame1,text="E-Mail:",font=("times new ronam",15,"bold"),bg="white")
        e_mail.place(x=400,y=180)
        self.entry_e_mail=ttk.Entry(frame1,textvariable=self.var_email,font=("times new roman",13,"bold"))
        self.entry_e_mail.place(x=400,y=210,width=250)

        sctyques=Label(frame1,text="Select Security Question:",font=("times new ronam",15,"bold"),bg="white")
        sctyques.place(x=50,y=260)
        self.combo_scty=ttk.Combobox(frame1,textvariable=self.var_security_Q,font=("times new roman",13,"bold"),state="readonly")
        self.combo_scty["values"]=("Select","Your Birth Place","Your First school Name","Your Nickname","Your Pet Name")
        self.combo_scty.place(x=50,y=290,width=250)
        self.combo_scty.current(0)

        sctyans=Label(frame1,text="Security Answer:",font=("times new ronam",15,"bold"),bg="white")
        sctyans.place(x=400,y=260)
        self.entry_sctyans=ttk.Entry(frame1,textvariable=self.var_security_A,font=("times new roman",13,"bold"))
        self.entry_sctyans.place(x=400,y=290,width=250)

        password=Label(frame1,text="Password:",font=("times new ronam",15,"bold"),bg="white")
        password.place(x=50,y=340)
        self.entry_password=ttk.Entry(frame1,textvariable=self.var_Password,font=("times new roman",13,"bold"))
        self.entry_password.place(x=50,y=370,width=250)

        password_conf=Label(frame1,text="Confirm Password:",font=("times new ronam",15,"bold"),bg="white")
        password_conf.place(x=400,y=340)
        self.entry_password_conf=ttk.Entry(frame1,textvariable=self.var_C_passwoed,font=("times new roman",13,"bold"))
        self.entry_password_conf.place(x=400,y=370,width=250)
      # ********** Check-Button***********
        check_btn=Checkbutton(frame1,variable=self.var_checkbtn,text="I Agree to the Terms and Conditions",font=("times new ronam",15,"bold"),bg="white",onvalue=1,offvalue=0)
        check_btn.place(x=30,y=410)
      # ******* Submit BUtton************
        imag=Image.open(r"C:\Users\LENOVO G3\Downloads\images\submit.jpg")
        imag=imag.resize((200,50),Image.ANTIALIAS)
        self.photoimage1=ImageTk.PhotoImage(imag)
        b1=Button(frame1,image=self.photoimage1,command=self.register_data,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=50,y=480,width=200)

        imag1=Image.open(r"C:\Users\LENOVO G3\Downloads\images\login.png")
        imag1=imag1.resize((200,50),Image.ANTIALIAS)
        self.photoimage2=ImageTk.PhotoImage(imag1)
        b1=Button(frame1,image=self.photoimage2,command=self.return_login,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=400,y=480,width=200)
        #******* function defination******
    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_security_Q.get()=="Select":
            messagebox.showerror("Error","All field are required",parent=self.root)
        elif self.var_Password.get()!=self.var_C_passwoed.get():
            messagebox.showerror("Error","Password Does not Match",parent=self.root)
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please Agree Terms And Conditions",parent=self.root)
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="root2001",database="registeration_database")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
            messagebox.showerror("Error","User Already Exist,Please Try another Email",parent=self.root)
           else:
            my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
             self.var_fname.get(),
             self.var_lname.get(),
             self.var_contact.get(),
             self.var_email.get(),
             self.var_security_Q.get(),
             self.var_security_A.get(),
             self.var_Password.get()                                                    ) )
           conn.commit()
           conn.close()
           messagebox.showinfo("Sucess","Register Successful",parent=self.root)
           self.root.destroy()
    def return_login(self):
        self.root.destroy()
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
            

if __name__=="__main__":
   main()