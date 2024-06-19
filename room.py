from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
from tkinter.constants import RIDGE
import mysql.connector
from time  import strftime 
from datetime import datetime

class Roombooking:
    def __init__(self, root):
        self.root = root    
        self.root.title("Hotel Management System")
        self.root.geometry("1295x700+230+100")

        # Variables 
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_roomavailable = StringVar()
        self.var_meal = StringVar()
        self.var_noofdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # Title
        lbl_title = Label(self.root, text="ROOMBOOKING DETAILS", font=("times new roman", 18, "bold"), bg="black", fg="gold")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # Logo image
        img2 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\logohotel.png")  # Adjust the path accordingly
        img2 = img2.resize((100, 40), Image.LANCZOS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg.place(x=0, y=0, width=100, height=40)

        # Label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Roombooking Details", font=("times new roman", 12, "bold"), pady=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        # Labels and entries

        # Customer contact
        lbl_cust_contact = Label(labelframeleft, text="Customer Contact:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        enty_contact = ttk.Entry(labelframeleft, textvariable=self.var_contact, font=("Arial", 13, "bold"), width=29)
        enty_contact.grid(row=0, column=1, sticky=W)

        # Button Frame
        btn_frame1 = Frame(self.root, bd=4, relief=RIDGE)
        btn_frame1.place(x=5, y=540, width=425, height=50)

        # Fetch Data Button
        btnFetchData = Button(btn_frame1, command=self.fetch_contact, text="Fetch Data", font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnFetchData.grid(row=0, column=0, padx=10)

        # Check-in Date
        check_in_date = Label(labelframeleft, text="Check-in Date:", font=("Arial", 12, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in_date = ttk.Entry(labelframeleft, textvariable=self.var_checkin, font=("Arial", 13, "bold"), width=29)
        txtcheck_in_date.grid(row=1, column=1)

        # Check-out Date
        lbl_Check_out = Label(labelframeleft, text="Check-out Date:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_Check_out.grid(row=2, column=0, sticky=W)

        txt_Check_out = ttk.Entry(labelframeleft, textvariable=self.var_checkout, font=("Arial", 13, "bold"), width=29)
        txt_Check_out.grid(row=2, column=1)

        # Room type (should be Combobox)
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=3, column=0, sticky=W)

        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT `Room Type` FROM details")
        ide = my_cursor.fetchall()

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, font=("Arial", 13, "bold"), width=27, state="readonly")
        combo_RoomType['values'] = ide
        combo_RoomType.current(0)
        combo_RoomType.grid(row=3, column=1)

        # Available Room
        lblRoomAvailable = Label(labelframeleft, text="Available Room:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=4, column=0, sticky=W)

       # txtRoomAvailable = ttk.Entry(labelframeleft, textvariable=self.var_roomavailable, font=("Arial", 13, "bold"), width=29)
        #txtRoomAvailable.grid(row=4, column=1)

        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT `Room No` FROM details")
        rows = my_cursor.fetchall()


        combo_RoomNo = ttk.Combobox(labelframeleft, textvariable=self.var_roomavailable, font=("Arial", 13, "bold"), width=27, state="readonly")
        combo_RoomNo['values'] = rows
        combo_RoomNo.current(0)
        combo_RoomNo.grid(row=4, column=1)

        # Meal
        lblMeal = Label(labelframeleft, text="Meal:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblMeal.grid(row=5, column=0, sticky=W)

        txtMeal = ttk.Entry(labelframeleft, textvariable=self.var_meal, font=("Arial", 13, "bold"), width=29)
        txtMeal.grid(row=5, column=1)

        # No of Days
        lblNoOfDays = Label(labelframeleft, text="No of Days:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(labelframeleft, textvariable=self.var_noofdays, font=("Arial", 13, "bold"), width=29)
        txtNoOfDays.grid(row=6, column=1)

        # Paid Tax
        lblPaidTax = Label(labelframeleft, text="Paid Tax:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblPaidTax.grid(row=7, column=0, sticky=W)

        txtPaidTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax, font=("Arial", 13, "bold"), width=29)
        txtPaidTax.grid(row=7, column=1)

        # Sub Total
        lblSubTotal = Label(labelframeleft, text="Sub Total:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(labelframeleft, textvariable=self.var_actualtotal, font=("Arial", 13, "bold"), width=29)
        txtSubTotal.grid(row=8, column=1)

        # Total Cost
        lblTotalCost = Label(labelframeleft, text="Total Cost:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lblTotalCost.grid(row=9, column=0, sticky=W)

        txtTotalCost = ttk.Entry(labelframeleft, textvariable=self.var_total, font=("Arial", 13, "bold"), width=29)
        txtTotalCost.grid(row=9, column=1)

        # ==== BILL BUTTON ====
        btnBill = Button(labelframeleft, text="Bill",command=self.total, font=("Arial", 12, "bold"), bg="black", fg="gold", width=10)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # Button Frame inside Label Frame
        btn_frame2 = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame2.place(x=0, y=400, width=425, height=40)

        btnAdd = Button(btn_frame2, text="Add", command=self.add_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame2, text="Update", command=self.update, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame2, text="Delete", command=self.mDelete, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame2, text="Reset", command=self.reset, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # Right side image
        img3 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\b.jpg")  # Adjust the path accordingly
        img3 = img3.resize((400, 300), Image.LANCZOS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        lblimg = Label(self.root, image=self.photoimg3, bd=0, relief=RIDGE)
        lblimg.place(x=760, y=55, width=400, height=300)

        # Table Frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View Details and Search System", font=("Arial", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, font=("Arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lblSearchBy.grid(row=0, column=0, sticky=W, padx=2)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, font=("Arial", 12, "bold"), width=24, state="readonly")
        combo_Search['values'] = ("Contact", "Room")
        combo_Search.current(0)
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(Table_Frame, textvariable=self.txt_search, font=("Arial", 13, "bold"), width=24)
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show All", command=self.fetch_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # Show data table
        Details_Table = Frame(Table_Frame, bd=2, relief=RIDGE)
        Details_Table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(Details_Table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Details_Table, orient=VERTICAL)

        self.room_table = ttk.Treeview(Details_Table, column=("contact", "checkin", "checkout", "roomtype", "roomavailable", "meal", "noofdays"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("contact", text="Contact")
        self.room_table.heading("checkin", text="Check-in")
        self.room_table.heading("checkout", text="Check-out")
        self.room_table.heading("roomtype", text="Room Type")
        self.room_table.heading("roomavailable", text="Room Available")
        self.room_table.heading("meal", text="Meal")
        self.room_table.heading("noofdays", text="NoOfDays")

        self.room_table["show"] = "headings"

        self.room_table.column("contact", width=100)
        self.room_table.column("checkin", width=100)
        self.room_table.column("checkout", width=100)
        self.room_table.column("roomtype", width=100)
        self.room_table.column("roomavailable", width=100)
        self.room_table.column("meal", width=100)
        self.room_table.column("noofdays", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All fields are required")
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO room VALUES (%s, %s, %s, %s, %s, %s, %s)",
                                  (self.var_contact.get(), self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(),
                                   self.var_roomavailable.get(), self.var_meal.get(), self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room Booked", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM room")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.room_table.focus()
        content = self.room_table.item(cursor_row)
        row = content["values"]
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            my_cursor.execute("UPDATE room SET check_in=%s, check_out=%s, roomtype=%s, roomavailable=%s, meal=%s, noOfdays=%s WHERE contact=%s",
                              (self.var_checkin.get(), self.var_checkout.get(), self.var_roomtype.get(), self.var_roomavailable.get(),
                               self.var_meal.get(), self.var_noofdays.get(), self.var_contact.get()))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated successfully", parent=self.root)

    def mDelete(self):
        mDelete = messagebox.askyesno("Hotel Management System", "Do you want to delete this room?", parent=self.root)
        if mDelete > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "DELETE FROM room WHERE contact=%s"
            value = (self.var_contact.get(),)
            my_cursor.execute(query, value)
            conn.commit()
            self.fetch_data()
            conn.close()
        else:
            if not mDelete:
                return

    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")
# all data fetch
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror("Error", "Please enter Contact Number", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                query = "SELECT Name, Gender, Email, Nationality, Address FROM customer WHERE Mobile=%s"
                value = (self.var_contact.get(),)
                my_cursor.execute(query, value)
                row = my_cursor.fetchone()
                if row is None:
                    messagebox.showerror("Error", "This number not found", parent=self.root)
                else:
                    showDataframe = Frame(self.root, bd=4, relief=RIDGE, padx=2)
                    showDataframe.place(x=450, y=55, width=300, height=180)

                    lblName = Label(showDataframe, text="Name:", font=("Arial", 12, "bold"))
                    lblName.place(x=0, y=0)

                    lbl = Label(showDataframe, text=row[0], font=("Arial", 12, "bold"))
                    lbl.place(x=90, y=0)

                    lblGender = Label(showDataframe, text="Gender:", font=("Arial", 12, "bold"))
                    lblGender.place(x=0, y=30)

                    lbl2 = Label(showDataframe, text=row[1], font=("Arial", 12, "bold"))
                    lbl2.place(x=90, y=30)

                    lblEmail = Label(showDataframe, text="Email:", font=("Arial", 12, "bold"))
                    lblEmail.place(x=0, y=60)

                    lbl3 = Label(showDataframe, text=row[2], font=("Arial", 12, "bold"))
                    lbl3.place(x=90, y=60)

                    lblNationality = Label(showDataframe, text="Nationality:", font=("Arial", 12, "bold"))
                    lblNationality.place(x=0, y=90)

                    lbl4 = Label(showDataframe, text=row[3], font=("Arial", 12, "bold"))
                    lbl4.place(x=90, y=90)

                    lblAddress = Label(showDataframe, text="Address:", font=("Arial", 12, "bold"))
                    lblAddress.place(x=0, y=120)

                    lbl5 = Label(showDataframe, text=row[4], font=("Arial", 12, "bold"))
                    lbl5.place(x=90, y=120)

                conn.commit()
                conn.close()
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def search(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()

        search_by = self.search_var.get()
        search_text = self.txt_search.get()

        if search_by == "Contact":
            my_cursor.execute("SELECT * FROM room WHERE contact LIKE %s", ('%' + search_text + '%',))
        elif search_by == "Room":
            my_cursor.execute("SELECT * FROM room WHERE roomavailable LIKE %s", ('%' + search_text + '%',))

        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.room_table.delete(*self.room_table.get_children())
            for i in rows:
                self.room_table.insert("", END, values=i)
            conn.commit()
        conn.close()


    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")
        self.var_noofdays.set(abs(outDate - inDate).days)

        if (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Luxury"):
            q1 = 300
            q2 = 700
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "BreakFast" and self.var_roomtype.get() == "Double"):
            q1 = 200
            q2 = 500
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Single"):
            q1 = 100
            q2 = 300
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Single"):
            q1 = 100
            q2 = 300
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Double"):
            q1 = 200
            q2 = 500
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Lunch" and self.var_roomtype.get() == "Luxury"):
            q1 = 300
            q2 = 700
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Single"):
            q1 = 150
            q2 = 300
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Double"):
            q1 = 250
            q2 = 500
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)

        elif (self.var_meal.get() == "Dinner" and self.var_roomtype.get() == "Luxury"):
            q1 = 350
            q2 = 700
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)


        elif (self.var_meal.get() == "Breakfast" and self.var_roomtype.get() == "Duplex"):
            q1 = 500
            q2 = 1000
            q3 = q1 + q2
            Tax = "Rs." + str("%.2f" % (q3 * 0.09))
            ST = "Rs." + str("%.2f" % (q3 * 0.1))
            TT = "Rs." + str(q3 + (q3 * 0.1) + (q3 * 0.09))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
                  
                  
               

           
           

            
            
       

        

          

           
          
       


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
