from tkinter import *
from PIL import Image, ImageTk  # pip install pillow
from tkinter import ttk
import random
import mysql.connector  # Correct import statement
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root 
        self.root.title("Hotel Management System")
        self.root.geometry("1295x700+230+100")

        # Variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_mother = StringVar()
        self.var_gender = StringVar()
        self.var_post = StringVar()
        self.var_mobile = StringVar()
        self.var_email = StringVar() 
        self.var_nation = StringVar() 
        self.var_address = StringVar() 
        self.var_idproof = StringVar() 
        self.var_idnumber = StringVar()

        # Title
        lbl_title = Label(self.root, text="ADD CUSTOMER DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo image
        img2 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\logohotel.png")
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=40)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer Details", font=("times new roman", 12, "bold"), pady=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Labels and entries

        # Customer reference
        lbl_cust_ref = Label(labelframeleft, text="Customer Ref", font=("arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)
        
        enty_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, font=("arial", 13, "bold"), width=29, state="readonly")
        enty_ref.grid(row=0, column=1)

        # Customer name
        cname = Label(labelframeleft, font=("arial", 12, "bold"), text="Customer Name:", padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)
        
        txtcname = ttk.Entry(labelframeleft, textvariable=self.var_cust_name, width=29, font=("times new roman", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # Mother name
        lblmname = Label(labelframeleft, font=("arial", 12, "bold"), text="Mother Name:", padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)
        
        txtmname = ttk.Entry(labelframeleft, textvariable=self.var_mother, width=29, font=("times new roman", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # Gender combobox
        label_gender = Label(labelframeleft, font=("arial", 12, "bold"), text="Gender:", padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)
        
        gender_combobox = ttk.Combobox(labelframeleft, textvariable=self.var_gender, font=("arial", 12, "bold"), width=27, state="readonly")
        gender_combobox["values"] = ("Male", "Female", "Other")
        gender_combobox.current(0)
        gender_combobox.grid(row=3, column=1)

        # Post code
        lblPostCode = Label(labelframeleft, font=("arial", 12, "bold"), text="Post Code:", padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)
        
        txtPostCode = ttk.Entry(labelframeleft, textvariable=self.var_post, width=29, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        # Mobile number
        lblMobile = Label(labelframeleft, font=("arial", 12, "bold"), text="Mobile:", padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)
        
        txtMobile = ttk.Entry(labelframeleft, textvariable=self.var_mobile, width=29, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # Email
        lblEmail = Label(labelframeleft, font=("arial", 12, "bold"), text="Email:", padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)
        
        txtEmail = ttk.Entry(labelframeleft, textvariable=self.var_email, width=29, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # Nationality
        lblNationality = Label(labelframeleft, font=("arial", 12, "bold"), text="Nationality:", padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)
        
        nationality_combobox = ttk.Combobox(labelframeleft, textvariable=self.var_nation, font=("arial", 12, "bold"), width=27, state="readonly")
        nationality_combobox["values"] = ("Indian", "American", "British", "Other")
        nationality_combobox.grid(row=7, column=1)
        nationality_combobox.current(0)

        # ID Proof Type
        lblIdProof = Label(labelframeleft, font=("arial", 12, "bold"), text="ID Proof type:", padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)
        
        idproof_combobox = ttk.Combobox(labelframeleft, textvariable=self.var_idproof, font=("arial", 12, "bold"), width=27, state="readonly")
        idproof_combobox["values"] = ("Aadhaar Card", "Driving License", "Passport", "Other")
        idproof_combobox.grid(row=8, column=1)
        idproof_combobox.current(0)

        # ID Number
        lblIdNumber = Label(labelframeleft, font=("arial", 12, "bold"), text="ID Number:", padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)
        
        txtIdNumber = ttk.Entry(labelframeleft, textvariable=self.var_idnumber, width=29, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1) 

        # Address
        lblAddress = Label(labelframeleft, font=("arial", 12, "bold"), text="Address:", padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)
        
        txtAddress = ttk.Entry(labelframeleft, textvariable=self.var_address, width=29, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)

        # Button Frame
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=425, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        search_combobox = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=24, state="readonly")
        search_combobox["values"] = ("Mobile", "Ref")
        search_combobox.grid(row=0, column=1, padx=2)
        search_combobox.current(0)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, width=24, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Details Table
        details_table_frame = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table_frame.place(x=0, y=50, width=860, height=350)

        scroll_x = ttk.Scrollbar(details_table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table_frame, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table_frame, column=("ref", "name", "mother", "gender", "post", "mobile", "email", "nationality", "idproof", "idnumber", "address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ref", text="Ref")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("mother", text="Mother Name")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("post", text="PostCode")
        self.Cust_Details_Table.heading("mobile", text="Mobile")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idproof", text="Id Proof")
        self.Cust_Details_Table.heading("idnumber", text="Id Number")
        self.Cust_Details_Table.heading("address", text="Address")

        self.Cust_Details_Table["show"] = "headings"

        self.Cust_Details_Table.column("ref", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("mother", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("post", width=100)
        self.Cust_Details_Table.column("mobile", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idproof", width=100)
        self.Cust_Details_Table.column("idnumber", width=100)
        self.Cust_Details_Table.column("address", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO customer VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nation.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_address.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0])
        self.var_cust_name.set(row[1])
        self.var_mother.set(row[2])
        self.var_gender.set(row[3])
        self.var_post.set(row[4])
        self.var_mobile.set(row[5])
        self.var_email.set(row[6])
        self.var_nation.set(row[7])
        self.var_idproof.set(row[8])
        self.var_idnumber.set(row[9])
        self.var_address.set(row[10])

    def update(self):
        if self.var_mobile.get() == "":
            messagebox.showerror("Error", "Please enter mobile number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                my_cursor.execute("UPDATE customer SET `Name`=%s, `Mother`=%s, `Gender`=%s, `PostCode`=%s, `Mobile`=%s, `Email`=%s, `Nationality`=%s, `IdProof`=%s, `IdNumber`=%s, `Address`=%s WHERE `Ref`=%s", (
                    self.var_cust_name.get(),
                    self.var_mother.get(),
                    self.var_gender.get(),
                    self.var_post.get(),
                    self.var_mobile.get(),
                    self.var_email.get(),
                    self.var_nation.get(),
                    self.var_idproof.get(),
                    self.var_idnumber.get(),
                    self.var_address.get(),
                    self.var_ref.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Update", "Customer details have been updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "DELETE FROM customer WHERE `Ref`=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            conn.close()
            self.fetch_data()
        else:
            if not mDelete:
                return

    def reset(self):
        self.var_ref.set(str(random.randint(1000, 9999)))
        self.var_cust_name.set("")
        self.var_mother.set("")
        self.var_gender.set("")
        self.var_post.set("")
        self.var_mobile.set("")
        self.var_email.set("")
        self.var_nation.set("")
        self.var_idproof.set("")
        self.var_idnumber.set("")
        self.var_address.set("")

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()

        search_by = self.search_var.get()
        search_txt = self.txt_search.get()

        query = f"SELECT * FROM customer WHERE `{search_by}` LIKE %s"
        value = (f"%{search_txt}%",)
        my_cursor.execute(query, value)
        rows = my_cursor.fetchall()

        if len(rows) != 0:
            self.Cust_Details_Table.delete(*self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()



if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
