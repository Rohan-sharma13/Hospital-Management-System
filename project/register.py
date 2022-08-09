from getopt import gnu_getopt
from time import sleep
from tkinter import *
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector

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
        b1=Button(frame1,image=self.photoimage2,borderwidth=0,cursor="hand2",bg="white")
        b1.place(x=400,y=480,width=200)
        #******* function defination******
    def register_data(self):
        if self.var_fname.get()==""or self.var_email.get()==""or self.var_security_Q.get()=="Select":
            messagebox.showerror("Error","All field are required")
        elif self.var_Password.get()!=self.var_C_passwoed.get():
            messagebox.showerror("Error","Password Does not Match")
        elif self.var_checkbtn.get()==0:
            messagebox.showerror("Error","Please Agree Terms And Conditions")
        else:
           conn=mysql.connector.connect(host="localhost",user="root",password="root2001",database="registeration_database")
           my_cursor=conn.cursor()
           query=("select * from register where email=%s")
           value=(self.var_email.get(),)
           my_cursor.execute(query,value)
           row=my_cursor.fetchone()
           if row!=None:
            messagebox.showerror("Error","User Already Exist,Please Try another Email")
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
           messagebox.showinfo("Sucess","Register Successful")
if __name__=="__main__":
    root=Tk()
    app=Register(root)
    root.mainloop()