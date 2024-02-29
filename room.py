from tkinter import *
from PIL import Image,ImageTk

def book_now():
    root.destroy()
    import my




root=Tk()
root.title("Hotel Management System")
root.geometry("1500x1000+0+0")



 
img1=Image.open("C:\Softwarica\Python\pexels-photo-164595.jpeg")
img1=img1.resize((350,160),)
photoimg1=ImageTk.PhotoImage(img1)
 
 
labelimg = Label(root,image=photoimg1,bd=1,relief=RIDGE)
labelimg.place(x=30,y=30)

label1=Label(root,text="Room no:100",font=('Courier New Normal',14))
label1.place(x=60,y=210)
 
img2=Image.open("C:\Softwarica\Python\KATHM-P062-Guestroom.16x9.webp")
img2=img2.resize((350,160),)
photoimg2=ImageTk.PhotoImage(img2)
 
 
labelimg2 = Label(root,image=photoimg2,bd=1,relief=RIDGE)
labelimg2.place(x=500,y=30)
label2=Label(root,text="Room no:101",font=('Courier New Normal',14))
label2.place(x=550,y=210)
 
 
img3=Image.open("C:\Softwarica\Python\hotel room with beachfront view.jpg")
img3=img3.resize((350,160),)
photoimg3=ImageTk.PhotoImage(img3)
 
 
labelimg3 = Label(root,image=photoimg3,bd=1,relief=RIDGE)
labelimg3.place(x=1000,y=30)
label3=Label(root,text="Room no:103",font=('Courier New Normal',14))
label3.place(x=1000,y=210)


img4=Image.open("C:\Softwarica\Python\images (1).jpeg")
img4=img4.resize((350,160),)
photoimg4=ImageTk.PhotoImage(img4)
labelimg4 = Label(root,image=photoimg4,bd=1,relief=RIDGE)
labelimg4.place(x=1000,y=300)

label4=Label(root,text="Room no:104",font=('Courier New Normal',14))
label4.place(x=1000,y=500)

img5=Image.open("C:\Softwarica\Python\images.jpeg")
img5=img5.resize((350,160),)
photoimg5=ImageTk.PhotoImage(img5)
 
 
labelimg5 = Label(root,image=photoimg5,bd=1,relief=RIDGE)
labelimg5.place(x=500,y=300)


label5=Label(root,text="Room no:105",font=('Courier New Normal',14))
label5.place(x=550,y=500)



img6=Image.open("C:\Softwarica\Python\hotel-room-beautiful-orange-sofa-included-43642330.webp")
img6=img6.resize((350,160),)
photoimg6=ImageTk.PhotoImage(img6)
 
 
labelimg6 = Label(root,image=photoimg6,bd=1,relief=RIDGE)
labelimg6.place(x=30,y=300)

label6=Label(root,text="Room no:106",font=('Courier New Normal',14))
label6.place(x=50,y=500)



but=Button(root,text="Book Now",bg="black",fg="white",font=('Courier New Normal',16),command=book_now)
but.place(x=600,y=600)

root.mainloop()