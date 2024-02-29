import tkinter as tk
import mysql.connector

def submit_comment():
   
    comment_text = comment_entry.get()

   
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rojan7722",
        database="hotel"
    )
    mycursor = mydb.cursor()

    sql = "INSERT INTO comm (comment) VALUES (%s)"
    val = (comment_text,)

    mycursor.execute(sql, val)

    
    mydb.commit()

    
    mydb.close()

    comment_entry.delete(0, tk.END)


root = tk.Tk()
root.title("Comment Box")
root.geometry("500x500")


comment_label = tk.Label(root, text="Enter your comment:")
comment_label.pack()
comment_entry = tk.Entry(root, font=('Helvetica', 14), width=50)
comment_entry.pack(pady=30)


submit_button = tk.Button(root, text="Submit", command=submit_comment)
submit_button.pack()

root.mainloop()
