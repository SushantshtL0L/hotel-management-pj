from tkinter import *
from PIL import Image,ImageTk



class menuwin:
    def __init__(self,root):
        self.root=root
        self.root.title("MENU")
        self.root.geometry("1250x900+250+100")
       

        label_title=Label(root,text="MENU",font=("times new roman",40,"bold"),bg="green",fg="white",bd=5,relief=RIDGE)
        label_title.place(x=0,y=0,width=1250,height=100)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CATEGORIES",font=("new times roman",18,"bold"),padx=2)
        labelframeleft.place(x=5,y=100,width=350,height=210)

        veg_button=Button(labelframeleft,text=" 1           VEGETERIAN",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        veg_button.grid(row=3,column=0,pady=3)

        nonveg_button=Button(labelframeleft,text="2 NON VEGETERIAN",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        nonveg_button.grid(row=4,column=0,pady=3)

        drinks_button=Button(labelframeleft,text="3                     DRINKS",width=22,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2")
        drinks_button.grid(row=5,column=0,pady=3)
 
 
 


if __name__ == "__main__":
    root=Tk()
    obj=menuwin(root)
    root.mainloop()

        