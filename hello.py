from tkinter import *
from PIL import Image,ImageTk

 
def logout():
    root.destroy()
    import hotelman
def customer_details():
    root.destroy()
    import customersus

def open_room():
    root.destroy()
    import room

def menu_open():
    root.destroy()
    import menuu


def open_report():
    root.destroy()
    import report
    

root=Tk()
root.title("Hotel Management System")
root.geometry("1500x1000+0+0")
 
label_title=Label(root,text="WELCOME TO ROYAL HOTEL",font=("times new roman",40,"bold"),bg="white",fg="brown",bd=0,relief=RIDGE)
label_title.place(x=0,y=0,width=1500,height=100)
 
img1=Image.open("C:\Softwarica\Python\WhatsApp Image 2024-02-29 at 10.14.42_92198718.jpg")
img1=img1.resize((1250,900),)
photoimg1=ImageTk.PhotoImage(img1)
 
 
labelimg = Label(root,image=photoimg1,bd=1,relief=RIDGE)
labelimg.place(x=300,y=100,width=1200,height=900)
 
 

 
 
button_frame=Frame(bg="green",bd=0,relief=RIDGE)
button_frame.place(x=0,y=100,width=300,height=280)
 
menu_button=Button(button_frame,text="MENU",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=menu_open)
menu_button.grid(row=1,column=0,pady=2)
 
cust_button=Button(button_frame,text="CUSTOMER",command=customer_details,width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
cust_button.grid(row=2,column=0,pady=2)
       
 
Room_button=Button(button_frame,text="ROOM",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=open_room)
Room_button.grid(row=4,column=0,pady=2)
 
Report_button=Button(button_frame,text="REPORT",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=open_report)
Report_button.grid(row=5,column=0,pady=2)
 
logout_button=Button(button_frame,text="LOGOUT",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=logout)
logout_button.grid(row=6,column=0,pady=2)
 
root.mainloop()