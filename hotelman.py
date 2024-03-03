from tkinter import*
from PIL import ImageTk,Image
import mysql.connector
from tkinter import messagebox


con = mysql.connector.connect(host="localhost", username="root", password="rojan7722", database="hotel")
cursor = con.cursor()


def login_window():
    root.destroy()
    import hello



def login_user():
    if userentry.get() == "" or passentry.get() == "":
        messagebox.showinfo("Error", "Please enter username and password.")
    else:
        try:
            cursor.execute("SELECT * FROM login WHERE username=%s AND password=%s", (userentry.get(), passentry.get()))
            row = cursor.fetchone()
            if row is None:
                messagebox.showinfo("Error", "Invalid username and password")
            else:
                messagebox.showinfo("Success", "Congratulations!!!!")
                login_window()
        except mysql.connector.Error as err:
            messagebox.showerror("Error", f"Error accessing database: {err}")


 
 
def connect_database():
    if  entry5.get() == "" or entry6.get() == "" or entry7.get() == "":
        messagebox.showerror("Error", "Please enter all the data")
    elif entry6.get() != entry7.get():
        messagebox.showerror("error","error ")
    else:
        messagebox.showinfo("Data entered succesfully")
        store_data()

def open_galler():
    gallery_window=Toplevel(root)
    
def open_registration():
    global entry5, entry6, entry7
    registration_window = Toplevel(root)
    registration_window.title("Register customer")
    registration_window.geometry("1750x750")

    img6 = Image.open("C:\Softwarica\Python\_9f2b6346-ffd3-11e8-9457-b1b429387a4e.jpg")  # Added 'r' before the path for raw string
    img6 = img6.resize((1550, 850))
    photoimg6 = ImageTk.PhotoImage(img6)

    labelimg7 = Label(registration_window, image=photoimg6, bd=1, relief=RIDGE)
    labelimg7.image = photoimg6 
    labelimg7.place(x=0, y=0)  
    label12 = Label(registration_window, text="Create New Account",bg="black",fg="white",font=('Courier New Normal',16))
    label12.place(x=550, y=230)

    entry5 = Entry(registration_window, width=30)
    entry5.place(y=300, x=550)
    label12 = Label(registration_window, text="Username:",bg="black",fg="white")
    label12.place(x=480, y=300)

    entry5 = Entry(registration_window, width=30,)
    entry5.place(y=300, x=550)

    label13 = Label(registration_window, text="Password:",bg="black",fg="white")
    label13.place(x=480, y=340)

    entry6 = Entry(registration_window, width=30, show="*") 
    entry6.place(y=340, x=550)

    label14 = Label(registration_window, text="Confirm Password:",bg="black",fg="white")
    label14.place(x=430, y=380)

    entry7 = Entry(registration_window, width=30, show="*") 
    entry7.place(y=380, x=550)

    store_button = Button(registration_window, text="Create", command=connect_database,bg="black",fg="white",font=(15))
    store_button.place(x=550, y=420)
    
def store_data():
    query = "INSERT INTO login (username, password, confirm) VALUES (%s, %s, %s)"
    values = (entry5.get(), entry6.get(), entry7.get())
 
    try:
        cursor.execute(query, values)
        con.commit()
        print("Data has been stored successfully!")
    except mysql.connector.Error as err:
        print("Error:", err)

root=Tk()
root.geometry('1750x750')
root.title('Hotel Management System')
root.configure(bg='SkyBlue')

def about():
    new_window=Toplevel(root)
    new_window.geometry("100x600")

    label14=Label(new_window,text="“Welcome to Volta Vicharles Homes, an exclusive retreat collected in the cultural\n richness of Bhaktapur, Nepal. As the only 7-star hotel in the country, we offer a luxury\n experience that seamlessly blends modern opulence with timeless elegance. Our\n meticulously designed rooms and suites ensure a harmonious stay, catering to both\n leisure and business travelers. Indulge your senses in the culinary delights of our\n signature restaurant, featuring authentic Newari cuisines. At Volta Vicharles Homes,\n we invite you to immerse yourself in a haven of cultural sophistication, where every\n detail is crafted to provide an unparalleled experience in the heart of Nepal.”",font=("Times New Roman", 18, "italic", "bold")
                  )
    label14.pack()
img2=Image.open("C:\Softwarica\Python\KATHM-P0428-Entrance-Porch.16x9 (1).webp")
img=img2.resize((1000,490),Image.ANTIALIAS)

img1=ImageTk.PhotoImage(img)
label5=Label(root,image=img1,background='goldenrod')
label5.place(x=100,y=200,)

label1=Label(root,bg="black",width=10,height=10,padx=1000,).pack()

img4=Image.open("C:\Softwarica\Python\hotel.jpg")
img5=img4.resize((250,151),Image.ANTIALIAS)
img3=ImageTk.PhotoImage(img5)
label6=Label(root,image=img3,background='black')
label6.place(x=90,y=0)

label8=Button(root,text='Facilities',font=('Courier New Normal',12),command=open_galler,relief=RIDGE)
label8.place(x=1000,y=100)


label9=Button(root,text='About us',font=('Courier New Normal',12),command=about,relief=RIDGE)
label9.place(x=1200,y=100)

frame = LabelFrame(root, padx=100, pady=100, background='black')
frame.place(x=1100, y=200)
 
sign_in = Label(frame, text='Sign Up', fg='white', bg='black', font=(
    'Aerial', 16))
sign_in.pack()
 
user = Label(frame, text='Username', font=('Aerial', 13), fg='white', bg='black')
user.place(y=30)
 
userentry = Entry(frame, width=30)
userentry.pack(pady=30)
 
passs = Label(frame, text='Password', font=('Aerial', 13), fg='white', bg='black')
passs.place(y=160)
 
passentry = Entry(frame, width=30)
passentry.pack(pady=80)
 
butty = Button(frame, text="Sign In", bg="white", font=('Aerial', 13), fg='black',background='#0866FF',command=login_user)
butty.place(x=80, y=250)
 
butt = Button(frame, text="Create new account", bg="white", font=('Aerial', 13), fg='black',background='#0866FF', command=open_registration)
butt.place(x=30, y=290)
 
buttuu = Button(frame, text="Forgot password?", bg="white", font=('Aerial', 13), fg='red',background='#0866FF', command=open_registration)
buttuu.place(x=40, y=330)

root.mainloop() 
