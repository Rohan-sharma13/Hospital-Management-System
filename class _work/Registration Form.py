from ssl import Options
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from mysql import connector
import tkinter
from tkinter.font import BOLD
def database():
    conn = connector.connect(
        user='root',

        password='root2001',

        host='127.0.0.1',

        port='3306',

        database='data_base1')
    mycursor=conn.cursor()
    mycursor.execute("insert into details values(%s,%s,%s,%s,%s,%s)",
    (entry_1.get(),entry_2.get(),entry_3.get(),entry_4.get(),c.get(),var1.get()))
    messagebox.showinfo("info"," Data submitted Successfully")
    conn.commit()
root =Tk()
root.geometry("500x500")
root.title("Registration Form")
label_0=Label(root,text="Registration Form",width=20,font=("bold",20))
label_0.place(x=90,y=53)
label_1=Label(root,text="Serial.No",width=20,font=("bold",10))
label_1.place(x=80,y=110)
entry_1=Entry(root)
entry_1.place(x=240,y=110)
label_2=Label(root,text="Name",width=20,font=("bold",10))
label_2.place(x=78,y=150)
entry_2=Entry(root)
entry_2.place(x=240,y=150)
label_3=Label(root,text="Roll.no",width=20,font=("bold",10))
label_3.place(x=75,y=190)
entry_3=Entry(root)
entry_3.place(x=240,y=190)
label_4=Label(root,text="Address",width=20,font=("bold",10))
label_4.place(x=75,y=230)
entry_4=Entry(root)
entry_4.place(x=240,y=230)
label_5=Label(root,text="Branch",width=20,font=("bold",10))
label_5.place(x=75,y=275)
option_list=["Aerospace Engineering","Automobile Engineering","Civil Engineering","Computer Science Engineering","Electrical Engineering","Electronics & Communication","Electronics Engineering","Mechanical Engineering"]
c=StringVar()
droplist=OptionMenu(root,c, *option_list)
droplist.config(width=30)
c.set("Select your Branch")
droplist.place(x=235,y=270)
label_6=Label(root,text="Gender",width=20,font=("bold",10))
label_6.place(x=75,y=320)
var1=IntVar()
Radiobutton(root,text="Male",padx=5,variable=var1,value=1).place(x=235,y=320)
Radiobutton(root,text="Female",padx=20,variable=var1,value=2).place(x=290,y=320)
Button(root,text="Submit",width=20,bg="brown",fg="white",command=database).place(x=180,y=420)

root.mainloop()