from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector

# Establish MySQL connection
con = mysql.connector.connect(host="localhost", user="root", password="rojan7722", database="hotel")
cursor = con.cursor()
def delete_record():
    selected_item = room_Details_Table.selection()
    if selected_item:
        
        contact = room_Details_Table.item(selected_item)['values'][0]
        delete_query = "DELETE FROM customer WHERE customer_contact = %s"
        cursor.execute(delete_query, (contact,))
        con.commit()
        room_Details_Table.delete(selected_item)
        print("Record deleted successfully!")
    else:
        print("No record selected for deletion.")
def logout():
    root.destroy()
    import hotelman

def logout_home():
    root.destroy()
    import hello

def store_data():
    customer_contact = entry_contact.get()
    check_in_date = entry_date.get()
    check_out_date = entry_outdate.get()
    room_type = combo_room.get()
    available_room = entry_avroom.get()
    days = entry_day.get()


    valid_rooms = {'100', '101', '102', '103', '104', '105', '106', '107'}
    if available_room not in valid_rooms:
        print("Invalid room number.")
        return


    sql = "INSERT INTO room (customer_contact, check_in_date, check_out_date, room_type,room_no ,days) VALUES (%s, %s, %s, %s, %s,%s)"
    val = (customer_contact, check_in_date, check_out_date, room_type,available_room, days)

    cursor.execute(sql, val)
    con.commit()
    print("Data has been stored successfully!")


root = Tk()
root.title("Room Booking")
root.geometry("1250x900+250+100") 

img5 = Image.open("C:\Softwarica\Python\download (1).jpg")
img5 = img5.resize((1250, 490))
photoimg5 = ImageTk.PhotoImage(img5)
labelimg = Label(root, image=photoimg5, bd=1, relief=RIDGE)
labelimg.place(x=0, y=0, width=1250, height=490)

label_title = Label(root, text="ROOM  BOOKING", font=("times new roman", 40, "bold"), bg="grey", fg="black", bd=3, relief=RIDGE)
label_title.place(x=0, y=0, width=1250, height=50)


labelframeleft = LabelFrame(root, bd=2, relief=RIDGE, text="BOOKING DETAILS", font=("new times roman", 18, "bold"), padx=2)
labelframeleft.place(x=400, y=70, width=450, height=400)


label_contact = Label(labelframeleft, text="Customer Contact", font=("times new roman", 15, "bold"), padx=2, pady=6)
label_contact.grid(row=10, column=0)
entry_contact = ttk.Entry(labelframeleft, width=17, font=('times new roman', 15, "bold"))
entry_contact.grid(row=10, column=1, sticky=W)

label_date = Label(labelframeleft, text="check_in_Date", font=("times new roman", 15, "bold"), padx=2, pady=6)
label_date.grid(row=30, column=0)
entry_date = ttk.Entry(labelframeleft, width=22, font=('times new roman', 15, "bold"))
entry_date.grid(row=30, column=1)

label_outdate = Label(labelframeleft, text="Check_out_Date", font=("times new roman", 15, "bold"), padx=2, pady=6)
label_outdate.grid(row=50, column=0)
entry_outdate = ttk.Entry(labelframeleft, width=22, font=('times new roman', 15, "bold"))
entry_outdate.grid(row=50, column=1)

label_room = Label(labelframeleft, text="Room type", font=("times new roman", 15, "bold"), padx=40, pady=6)
label_room.grid(row=70, column=0, sticky=W)
combo_room = ttk.Combobox(labelframeleft, font=("arial", 15, "bold"), width=18, state="readonly")
combo_room["value"] = ("Single", "Double beded", "Premium Luxury")
combo_room.current(0)
combo_room.grid(row=70, column=1)

label_avroom = Label(labelframeleft, text="Available Room", font=("times new roman", 15, "bold"), padx=2, pady=6)
label_avroom.grid(row=90, column=0)
entry_avroom = ttk.Entry(labelframeleft, width=22, font=('times new roman', 15, "bold"))
entry_avroom.grid(row=90, column=1)

label_day = Label(labelframeleft, text="No of Days", font=("times new roman", 15, "bold"), padx=2, pady=6)
label_day.grid(row=110, column=0)
entry_day = ttk.Entry(labelframeleft, width=22, font=('times new roman', 15, "bold"))
entry_day.grid(row=110, column=1)

# Buttons for Add, Delete, Reset
btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
btn_frame.place(x=150, y=320, width=190, height=40)

butt_add = Button(btn_frame, text="Add", font=('times new roman', 14, 'bold'), bg="black", fg="gold", command=store_data)
butt_add.grid(row=180, column=0, padx=0)

butt_delete = Button(btn_frame, text="Delete", font=('times new roman', 14, 'bold'), bg="black", fg="gold", command=delete_record)
butt_delete.grid(row=180, column=1, padx=2)



room_table = LabelFrame(root, bd=2, relief=RIDGE, text="View Booking Details", font=("new times roman", 18, "bold"), padx=2)
room_table.place(x=10, y=490, width=1230, height=400)

lblsearchBy = Label(room_table, font=("arial", 12, "bold"), text="Booking ", bg="blue", fg="white")
lblsearchBy.grid(row=0, column=0, sticky=W)
logout_button=Button(root,text="LOGOUT",width=15,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=logout)
logout_button.place(x=920,y=100)

logout_button1=Button(root,text="Home Page",width=15,font=("times new roman",20,"bold"),bg="black",fg="gold",bd=1,cursor="hand2",command=logout_home)
logout_button1.place(x=920,y=200)


room_table_frame = Frame(room_table, bd=2, relief=RIDGE)
room_table_frame.place(x=0, y=35, width=1200, height=330)

Scroll_x = ttk.Scrollbar(room_table_frame, orient=HORIZONTAL)
Scroll_y = ttk.Scrollbar(room_table_frame, orient=VERTICAL)

room_Details_Table = ttk.Treeview(room_table_frame, column=("contact", "checkin", "checkout", "roomtype", "availableroom", "nodays", "paidtax", "totcost"), xscrollcommand=Scroll_x.set, yscrollcommand=Scroll_y.set)

Scroll_x.pack(side=BOTTOM, fill=X)
Scroll_y.pack(side=RIGHT, fill=Y)

Scroll_x.config(command=room_Details_Table.xview)
Scroll_y.config(command=room_Details_Table.yview)

room_Details_Table.heading("contact", text="Mobile")
room_Details_Table.heading("checkin", text="Check-in")
room_Details_Table.heading("checkout", text="Check-out")
room_Details_Table.heading("roomtype", text="Room Type")
room_Details_Table.heading("availableroom", text="Available Room")
room_Details_Table.heading("nodays", text="No of days")



room_Details_Table["show"] = "headings"

room_Details_Table.column("contact", width=200)
room_Details_Table.column("checkin", width=200)
room_Details_Table.column("checkout", width=200)
room_Details_Table.column("roomtype", width=200)
room_Details_Table.column("availableroom", width=200)
room_Details_Table.column("nodays", width=200)



room_Details_Table.pack(fill=BOTH, expand=1)


query = "SELECT customer_contact, check_in_date, check_out_date,room_type,room_no, days FROM room"
cursor.execute(query)
customer_data = cursor.fetchall()

for data in customer_data:
    room_Details_Table.insert('', 'end', values=data)


root.mainloop()