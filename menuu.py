from tkinter import *

from PIL import Image,ImageTk


root=Tk()
root.geometry("1200x800")
def logout_home():
    root.destroy()
    import hello
       

label_title=Label(root,text="MENU",font=("times new roman",40,"bold"),bg="white",fg="brown",bd=2,relief=RIDGE)
label_title.place(x=0,y=0,width=1250,height=100)

img_men=Image.open("C:\\Softwarica\\Python\\restaurant-patio-hotel-menu-card-brochure-fly-design-template-f52da4bcfe7a823b84d82cb6190fcd83_screen.jpg")
img_men=img_men.resize((1000,500),)
photoimg_men=ImageTk.PhotoImage(img_men)
 
 
labelimg = Label(root,image=photoimg_men,bd=1,relief=RIDGE)
labelimg.place(x=0,y=0,width=1250,height=800)
logout_button1=Button(root,text="Home Page",width=15,font=("times new roman",20,"bold"),bg="white",fg="black",command=logout_home)
logout_button1.place(x=920,y=680)
root.mainloop()


