from tkinter import *
from tkinter import ttk
import mysql.connector


class Customerwin:
    def __init__(self,root):
        self.root=root
        self.root.title("CUSTOMER PAGE")
        self.root.geometry("1250x900+250+100")


       

        label_title=Label(self.root,text="ENTER  CUSTOMER  DETAILS",font=("times new roman",40,"bold"),bg="green",fg="white",bd=3,relief=RIDGE)
        label_title.place(x=0,y=0,width=1250,height=50)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("new times roman",18,"bold"),padx=2)
        labelframeleft.place(x=430,y=50,width=450,height=400)
        


        label1=Label(labelframeleft,text="Customer Name",font=("times new roman",15,"bold"),padx=2,pady=6)
        label1.grid(row=10,column=0)
         
        entry1=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry1.grid(row=10,column=1)



        label2=Label(labelframeleft,text="Email",font=("times new roman",15,"bold"),padx=2,pady=6)
        label2.grid(row=30,column=0)
        
        entry2=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry2.grid(row=30,column=1)




        label3=Label(labelframeleft,text="Phone number",font=("times new roman",15,"bold"),padx=2,pady=6)
        label3.grid(row=50,column=0)
    

        entry3=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry3.grid(row=50,column=1)




        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",15,"bold"),padx=40,pady=6)
        label_gender.grid(row=70,column=0,sticky=W)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",15,"bold"),width=18,state="readonly")
        combo_gender["value"]=("Male","Female","other")
        combo_gender.current(0)
        combo_gender.grid(row=70,column=1)
       




        label4=Label(labelframeleft,text="Address",font=("times new roman",15,"bold"),padx=2,pady=6)
        label4.grid(row=90,column=0)
    

        entry4=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry4.grid(row=90,column=1)





        label5=Label(labelframeleft,text="Nationality",font=("times new roman",15,"bold"),padx=2,pady=6)
        label5.grid(row=110,column=0)
    

        entry5=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry5.grid(row=110,column=1)





        label6=Label(labelframeleft,text="Id card proof ",font=("times new roman",15,"bold"),padx=2,pady=6)
        label6.grid(row=130,column=0,sticky=W)

        combo_ID=ttk.Combobox(labelframeleft,font=("arial",15,"bold"),width=18,state="readonly")
        combo_ID["value"]=("Citizenship","License card","Passport")
        combo_ID.grid(row=130,column=1)
        label7=Label(labelframeleft,text="Id number",font=("times new roman",15,"bold"),padx=2,pady=6)
        label7.grid(row=150,column=0)
    
        entry6=ttk.Entry(labelframeleft,width=22,font=('times new roman',15,"bold"))
        entry6.grid(row=150,column=1)



        
        btn_frame=Frame(labelframeleft,bd=2,relief=RIDGE)
        btn_frame.place(x=150,y=320,width=190,height=40)


        butt=Button(btn_frame,text="Add",font=('times new roman',14,'bold'),bg="brown",fg="white")
        butt.grid(row=180,column=0,padx=0)

        butt=Button(btn_frame,text="Delete",font=('times new roman',14,'bold'),bg="brown",fg="white")
        butt.grid(row=180,column=1,padx=2)

        butt=Button(btn_frame,text="Reset",font=('times new roman',14,'bold'),bg="brown",fg="white")
        butt.grid(row=180,column=3,padx=1)



      #*****************************NOTE*************************************

        Note_frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="NOTE",font=("new times roman",25,"bold"),fg="red")
        Note_frame.place(x=20,y=150,width=390,height=150)

        label_note_name=Label(Note_frame,text="If  you are  foreigner  please mention your passport and  ",font=("times new roman",12,"bold"))
        label_note_name.grid(row=1,column=0)

        label_note_name=Label(Note_frame,text="don't forget to choose the identification type to passport ",font=("times new roman",12,"bold"))
        label_note_name.grid(row=3,column=0)

        label_note_name=Label(Note_frame,text="and do mention  your  passport  number  on Id number . ",font=("times new roman",12,"bold"))
        label_note_name.grid(row=5,column=0)

        label_note_name=Label(Note_frame,text="THANK YOU. ",font=("times new roman",18,"bold"),fg="blue")
        label_note_name.grid(row=10,column=0)

        


      #___________________DOWN TABLE___________________


        details_table=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details",font=("new times roman",18,"bold"),padx=2)
        details_table.place(x=10,y=450,width=1220,height=430)
        
        lblsearchBy=Label(details_table,font=("arial",12,"bold"),text="Check your Details",bg="blue",fg="white")
        lblsearchBy.grid(row=0,column=0,sticky=W)


#______________________________________SCROLL__________________________________________
        
        details_table=Frame(details_table,bd=2,relief=RIDGE)
        details_table.place(x=0,y=35,width=1200,height=350)

        Scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        Scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)

        self.Cust_Details_Table=ttk.Treeview(details_table,column=("name","email","phone number","gender","Address","Nationality","Id type","Id number"),xscrollcommand=Scroll_x,yscrollcommand=Scroll_y.set)
        
        Scroll_x.pack(side=BOTTOM,fill=X)
        Scroll_y.pack(side=RIGHT,fill=Y)

        Scroll_x.config(command=self.Cust_Details_Table.xview)
        Scroll_y.config(command=self.Cust_Details_Table.yview)

        #+++++++++++++++++++++HEADINGS++++++++++++++++++++++++++++++++++++++++++++++++++

        self.Cust_Details_Table.heading("name",text="Name")
        self.Cust_Details_Table.heading("email",text="Email")
        self.Cust_Details_Table.heading("phone number",text="Phone Number")
        self.Cust_Details_Table.heading("gender",text="Gender")
        self.Cust_Details_Table.heading("Address",text="Address")
        self.Cust_Details_Table.heading("Nationality",text="Nationality")
        self.Cust_Details_Table.heading("Id type",text="ID type")
        self.Cust_Details_Table.heading("Id number",text="ID Number")

        self.Cust_Details_Table["show"]="headings"

        self.Cust_Details_Table.column("name",width=100)
        self.Cust_Details_Table.column("email",width=100)
        self.Cust_Details_Table.column("phone number",width=100)
        self.Cust_Details_Table.column("gender",width=100)
        self.Cust_Details_Table.column("Address",width=100)
        self.Cust_Details_Table.column("Nationality",width=100)
        self.Cust_Details_Table.column("Id type",width=100)
        self.Cust_Details_Table.column("Id number",width=100)

        self.Cust_Details_Table.pack(fill=BOTH,expand=1)


    #def add_data(self):    


        




                

if __name__ == "__main__":
    root=Tk()
    obj=Customerwin(root)
    root.mainloop()

        