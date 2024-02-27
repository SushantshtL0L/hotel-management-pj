from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import random
import mysql.connector
from tkinter import messagebox



con = mysql.connector.connect(host="localhost", username="root", password="rojan7722", database="hotel")
cursor = con.cursor()  
def add_data():
    global entry1, entry2, entry3, entry4, entry5, entry6, combo_gender, combo1
    
    customer_name = entry1.get()
    email = entry2.get()
    phone_number = entry3.get()
    gender = combo_gender.get()
    address = entry4.get()
    nationality = entry5.get()
    id_proof = combo_ID.get()
    id_number = entry6.get()
    
    query = "INSERT INTO customer (custome_name,email,number, gender, address, nationality, id_proof, idnum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (customer_name, email, phone_number, gender, address, nationality, id_proof, id_number)
    
    cursor.execute(query, values)
    con.commit()
    print("Data inserted successfully!")


root = Tk()
root.title("CUSTOMER PAGE")
root.geometry("1250x900+250+100")

# ________________________variable________________________

var_ref = StringVar()
x = random.randint(1000, 9990)
var_ref.set(str(x))

var_cutomer_name = StringVar()
var_Email = StringVar()
var_Phone_number = StringVar()
var_Gender = StringVar()
var_Address = StringVar()
var_Nationality = StringVar()
var_Id_proof = StringVar()
var_Id_number = StringVar()

# ***********TITLEEEEEEEEE********************************************************************************************

label_title = Label(root, text="ENTER  CUSTOMER  DETAILS", font=(
    "times new roman", 40, "bold"), bg="black", fg="gold", bd=1, relief=RIDGE)
label_title.place(x=0, y=0, width=1250, height=50)

labelframeleft = LabelFrame(root, bd=2, relief=RIDGE,
                            text="CUSTOMER DETAILS", font=("new times roman", 18, "bold"), padx=2)
labelframeleft.place(x=430, y=50, width=450, height=400)

label1 = Label(labelframeleft, text="Customer Name", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label1.grid(row=10, column=0)

entry1 = Entry(labelframeleft, width=22, textvariable=var_cutomer_name,
               font=('times new roman', 15, "bold"))
entry1.grid(row=10, column=1)

label2 = Label(labelframeleft, text="Email", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label2.grid(row=30, column=0)

entry2 = Entry(labelframeleft, width=22, textvariable=var_Email,
               font=('times new roman', 15, "bold"))
entry2.grid(row=30, column=1)

label3 = Label(labelframeleft, text="Phone number", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label3.grid(row=50, column=0)

entry3 = Entry(labelframeleft, width=22, textvariable=var_Phone_number,
               font=('times new roman', 15, "bold"))
entry3.grid(row=50, column=1)

label_gender = Label(labelframeleft, text="Gender", font=(
    "times new roman", 15, "bold"), padx=40, pady=6)
label_gender.grid(row=70, column=0, sticky=W)

combo_gender = ttk.Combobox(labelframeleft, textvariable=var_Gender, font=(
    "arial", 15, "bold"), width=18, state="readonly")
combo_gender["value"] = ("Male", "Female", "other")
combo_gender.current(0)
combo_gender.grid(row=70, column=1)

label4 = Label(labelframeleft, text="Address", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label4.grid(row=90, column=0)

entry4 = Entry(labelframeleft, textvariable=var_Address,
               width=22, font=('times new roman', 15, "bold"))
entry4.grid(row=90, column=1)

label5 = Label(labelframeleft, text="Nationality", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label5.grid(row=110, column=0)

entry5 = Entry(labelframeleft, textvariable=var_Nationality,
               width=22, font=('times new roman', 15, "bold"))
entry5.grid(row=110, column=1)

label6 = Label(labelframeleft, text="Id card proof ", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label6.grid(row=130, column=0, sticky=W)

combo_ID = ttk.Combobox(labelframeleft, textvariable=var_Id_proof, font=(
    "arial", 15, "bold"), width=18, state="readonly")
combo_ID["value"] = ("Citizenship", "License card", "Passport")
combo_ID.grid(row=130, column=1)

label7 = Label(labelframeleft, text="Id number", font=(
    "times new roman", 15, "bold"), padx=2, pady=6)
label7.grid(row=150, column=0)

entry6 = Entry(labelframeleft, textvariable=var_Id_number,
               width=22, font=('times new roman', 15, "bold"))
entry6.grid(row=150, column=1)

# ______________________________BUTTONS___________________________________________

btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
btn_frame.place(x=150, y=320, width=190, height=40)

butt = Button(btn_frame, text="Add", font=(
    'times new roman', 14, 'bold'), bg="brown", fg="white",command=add_data)
butt.grid(row=180, column=0, padx=0)



# *****************************NOTE*************************************

Note_frame = LabelFrame(root, bd=2, relief=RIDGE,
                        text="NOTE", font=("new times roman", 25, "bold"), fg="red")
Note_frame.place(x=20, y=150, width=390, height=150)

label_note_name = Label(Note_frame, text="If  you are  foreigner  please mention your passport and  ",
                        font=("times new roman", 12, "bold"))
label_note_name.grid(row=1, column=0)

label_note_name = Label(Note_frame, text="don't forget to choose the identification type to passport ",
                        font=("times new roman", 12, "bold"))
label_note_name.grid(row=3, column=0)

label_note_name = Label(Note_frame, text="and do mention  your  passport  number  on Id number . ",
                        font=("times new roman", 12, "bold"))
label_note_name.grid(row=5, column=0)

label_note_name = Label(Note_frame, text="THANK YOU. ", font=(
    "times new roman", 18, "bold"), fg="blue")
label_note_name.grid(row=10, column=0)

# ___________________DOWN TABLE___________________



details_table=LabelFrame(root,bd=2,relief=RIDGE,text="View Details",font=("new times roman",18,"bold"),padx=2)
details_table.place(x=10,y=450,width=1220,height=430)

lblsearchBy=Label(details_table,font=("arial",12,"bold"),text="Check your Details",bg="blue",fg="white")
lblsearchBy.grid(row=0,column=0,sticky=W)


   #______________________________________SCROLL__________________________________________

details_table=Frame(details_table,bd=2,relief=RIDGE)
details_table.place(x=0,y=35,width=1200,height=350)

Scroll_x=Scrollbar(details_table,orient=HORIZONTAL)
Scroll_y=Scrollbar(details_table,orient=VERTICAL)

Cust_Details_Table=ttk.Treeview(details_table,column=("name","email","phone number","gender","Address","Nationality","Id type","Id number"),xscrollcommand=Scroll_x,yscrollcommand=Scroll_y.set)

Scroll_x.pack(side=BOTTOM,fill=X)
Scroll_y.pack(side=RIGHT,fill=Y)

Scroll_x.config(command=Cust_Details_Table.xview)
Scroll_y.config(command=Cust_Details_Table.yview)

   #+++++++++++++++++++++HEADINGS++++++++++++++++++++++++++++++++++++++++++++++++++

Cust_Details_Table.heading("name",text="Name")
Cust_Details_Table.heading("email",text="Email")
Cust_Details_Table.heading("phone number",text="Phone Number")
Cust_Details_Table.heading("gender",text="Gender")
Cust_Details_Table.heading("Address",text="Address")
Cust_Details_Table.heading("Nationality",text="Nationality")
Cust_Details_Table.heading("Id type",text="ID type")
Cust_Details_Table.heading("Id number",text="ID Number")

Cust_Details_Table["show"]="headings"

Cust_Details_Table.column("name",width=100)
Cust_Details_Table.column("email",width=100)
Cust_Details_Table.column("phone number",width=100)
Cust_Details_Table.column("gender",width=100)
Cust_Details_Table.column("Address",width=100)
Cust_Details_Table.column("Nationality",width=100)
Cust_Details_Table.column("Id type",width=100)
Cust_Details_Table.column("Id number",width=100)

Cust_Details_Table.pack(fill=BOTH,expand=1)

root.mainloop()





