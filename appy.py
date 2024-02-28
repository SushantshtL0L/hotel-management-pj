from tkinter import *
 
class win:
    def __init__(self,root):
        self.root=root
        self.root.title("CUSTOMER PAGE")
        self.root.geometry("1250x900+250+100")
 
        label_title=Label(self.root,text="ENTER  CUSTOMER  DETAILS",font=("times new roman",40,"bold"),bg="black",fg="gold",bd=3,relief=RIDGE)
        label_title.place(x=0,y=0,width=1250,height=50)
 
 
 
if __name__ == "__main__":
    root=Tk()
    obj=win(root)
    root.mainloop()