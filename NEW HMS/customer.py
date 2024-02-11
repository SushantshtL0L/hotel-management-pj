from tkinter import *
from tkinter import ttk

class Customerwin:
    def __init__(self,root):
        self.root=root
        self.root.title("CUSTOMER PAGE")
        self.root.geometry("1250x900+250+100")

        label_title=Label(self.root,text="ENTER  CUSTOMER  DETAILS",font=("times new roman",40,"bold"),bg="green",fg="white",bd=3,relief=RIDGE)
        label_title.place(x=0,y=0,width=1250,height=50)

        labelframeleft=LabelFrame(self.root,bd=2,relief=RIDGE,text="CUSTOMER DETAILS",font=("new times roman",18,"bold"),padx=2)
        labelframeleft.place(x=3,y=50,width=425,height=490)
        


        label_cust_name=Label(labelframeleft,text="Customer Name",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=10,column=0)
         
        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=10,column=1)

        label_cust_name=Label(labelframeleft,text="Email",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=30,column=0)
        
        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=30,column=1)

        label_cust_name=Label(labelframeleft,text="Phone number",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=50,column=0)
    

        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=50,column=1)

        label_gender=Label(labelframeleft,text="Gender",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=70,column=0)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),widt=18)
        combo_gender["value"]=("Male","Female","other")
        combo_gender.grid(row=70,column=1)
       
        label_cust_name=Label(labelframeleft,text="Address",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=90,column=0)
    

        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=90,column=1)

        label_cust_name=Label(labelframeleft,text="Nationality",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=110,column=0)
    

        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=110,column=1)

        label_gender=Label(labelframeleft,text="Id card proof ",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_gender.grid(row=130,column=0)

        combo_gender=ttk.Combobox(labelframeleft,font=("arial",12,"bold"),widt=18)
        combo_gender["value"]=("Citizenship","License card","Password")
        combo_gender.grid(row=130,column=1)
        label_cust_name=Label(labelframeleft,text="Id number",font=("times new roman",12,"bold"),padx=2,pady=6)
        label_cust_name.grid(row=150,column=0)
    

        entry_ref=ttk.Entry(labelframeleft,width=22,font=('times new roman',12,"bold"))
        entry_ref.grid(row=150,column=1)

        butt=Button(labelframeleft,text="Add",font=('times new roman',14,'bold'))
        butt.grid(row=170,column=1)





                

if __name__ == "__main__":
    root=Tk()
    obj=Customerwin(root)
    root.mainloop()

        