from tkinter import *
from PIL import Image,ImageTk
from customer import Customerwin
from Menu import menuwin
 
 
class HotelManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("Hotel Management System")
        self.root.geometry("1500x1000+0+0")
 
        label_title=Label(self.root,text="WELCOME TO ROYAL HOTEL",font=("times new roman",40,"bold"),bg="white",fg="brown",bd=0,relief=RIDGE)
        label_title.place(x=0,y=0,width=1500,height=100)
 
        img1=Image.open(r"C:\Users\Sushant Shrestha\Desktop\images hotel\dwarika.jpg")
        img1=img1.resize((1250,900),)
        photoimg1=ImageTk.PhotoImage(img1)
 
 
        labelimg = Label(self.root,image=photoimg1,bd=1,relief=RIDGE)
        labelimg.place(x=300,y=100,width=1200,height=900)
 
 
        img2=Image.open(r"C:\Users\Sushant Shrestha\Desktop\images hotel\food3.jpg")
        img2=img2.resize((300,450),)
        photoimg2=ImageTk.PhotoImage(img2)
 
 
        labelimg = Label(self.root,image=photoimg2,bd=1,relief=RIDGE)
        labelimg.place(x=0,y=270,width=300,height=450)
 
        img3=Image.open(r"C:\Users\Sushant Shrestha\Desktop\images hotel\food1.jpg")
        img3=img3.resize((300,300),)
        photoimg3=ImageTk.PhotoImage(img3)
 
 
        labelimg = Label(self.root,image=photoimg3,bd=1,relief=RIDGE)
        labelimg.place(x=0,y=700,width=300,height=300)
 
 
        button_frame=Frame(bg="green",bd=0,relief=RIDGE)
        button_frame.place(x=0,y=100,width=300,height=280)
 
        menu_button=Button(button_frame,text="MENU",command=self.menu_details,width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        menu_button.grid(row=1,column=0,pady=2)
 
        cust_button=Button(button_frame,text="CUSTOMER",command=self.customer_details,width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        cust_button.grid(row=2,column=0,pady=2)
       
         
        Room_button=Button(button_frame,text="ROOM",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        Room_button.grid(row=4,column=0,pady=2)
 
        Report_button=Button(button_frame,text="REPORT",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        Report_button.grid(row=5,column=0,pady=2)
 
        logout_button=Button(button_frame,text="LOGOUT",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        logout_button.grid(row=6,column=0,pady=2)
 
        self,root,mainloop()
    

    def menu_details(self):
        self.new_window=Toplevel(self.root)
        self.app=menuwin(self.new_window)    
 
    def customer_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customerwin(self.new_window)
 
if __name__ == "__main__":
     root=Tk()
     obj=HotelManagementSystem(root)
     root.mainloop()