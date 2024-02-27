from tkinter import *
from tkinter import ttk
import mysql.connector

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
    id_proof = combo1.get()
    id_number = entry6.get()
    
    query = "INSERT INTO customer (customer_name, email, number, gender, address, nationality, id_proof, idnum) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
    values = (customer_name, email, phone_number, gender, address, nationality, id_proof, id_number)
    
    cursor.execute(query, values)
    con.commit()
    print("Data inserted successfully!")

root = Tk()
root.title("CUSTOMER PAGE")
root.geometry("1250x900+250+100")

label_title = Label(root, text="ENTER CUSTOMER DETAILS", font=("times new roman", 40, "bold"), bg="green", fg="white", bd=3, relief=RIDGE)
label_title.place(x=0, y=0, width=1250, height=50)

labelframeleft = LabelFrame(root, bd=2, relief=RIDGE, text="CUSTOMER DETAILS", font=("new times roman", 18, "bold"), padx=2)
labelframeleft.place(x=3, y=50, width=425, height=490)

label_cust_name = Label(labelframeleft, text="Customer Name", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_cust_name.grid(row=10, column=0)
entry1 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry1.grid(row=10, column=1)

label_cust_email = Label(labelframeleft, text="Email", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_cust_email.grid(row=30, column=0)
entry2 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry2.grid(row=30, column=1)

label_cust_phone = Label(labelframeleft, text="Phone number", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_cust_phone.grid(row=50, column=0)
entry3 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry3.grid(row=50, column=1)

label_gender = Label(labelframeleft, text="Gender", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_gender.grid(row=70, column=0)
combo_gender = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=18)
combo_gender["value"] = ("Male", "Female", "other")
combo_gender.grid(row=70, column=1)
   
label_cust_address = Label(labelframeleft, text="Address", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_cust_address.grid(row=90, column=0)
entry4 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry4.grid(row=90, column=1)

label_cust_nationality = Label(labelframeleft, text="Nationality", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_cust_nationality.grid(row=110, column=0)
entry5 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry5.grid(row=110, column=1)

label_id_proof = Label(labelframeleft, text="Id card proof", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_id_proof.grid(row=130, column=0)
combo1 = ttk.Combobox(labelframeleft, font=("arial", 12, "bold"), width=18)
combo1["value"] = ("Citizenship", "License card", "Password")
combo1.grid(row=130, column=1)

label_id_number = Label(labelframeleft, text="Id number", font=("times new roman", 12, "bold"), padx=2, pady=6)
label_id_number.grid(row=150, column=0)
entry6 = ttk.Entry(labelframeleft, width=22, font=('times new roman', 12, "bold"))
entry6.grid(row=150, column=1)

butt = Button(labelframeleft, text="Add", font=('times new roman', 14, 'bold'), command=add_data)
butt.grid(row=170, column=1)

root.mainloop()
