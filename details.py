from tkinter import *
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import mysql.connector

class RoomDetails:
    def __init__(self, root):
        self.root = root    
        self.root.title("Hotel Management System")
        self.root.geometry("1295x700+230+100")

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
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="New Room Add", font=("times new roman", 12, "bold"), pady=2)
        labelframeleft.place(x=5, y=50, width=540, height=350)

        # Labels and entries

        # Floor
        lbl_floor = Label(labelframeleft, text="Floor:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_floor.grid(row=0, column=0, sticky=W)

        self.var_floor = StringVar()

        enty_floor = ttk.Entry(labelframeleft, textvariable=self.var_floor, font=("Arial", 13, "bold"), width=29)
        enty_floor.grid(row=0, column=1, sticky=W)

        # Room no
        lbl_RoomNo = Label(labelframeleft, text="Room No:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomNo.grid(row=1, column=0, sticky=W)

        self.var_RoomNo = StringVar()

        enty_RoomNo = ttk.Entry(labelframeleft, textvariable=self.var_RoomNo, font=("Arial", 13, "bold"), width=29)
        enty_RoomNo.grid(row=1, column=1, sticky=W)

        # Room type
        lbl_RoomType = Label(labelframeleft, text="Room Type:", font=("Arial", 12, "bold"), padx=2, pady=6)
        lbl_RoomType.grid(row=2, column=0, sticky=W)

        self.var_RoomType = StringVar()

        enty_RoomType = ttk.Entry(labelframeleft, textvariable=self.var_RoomType, font=("Arial", 13, "bold"), width=29)
        enty_RoomType.grid(row=2, column=1, sticky=W)

        # Button Frame inside Label Frame
        btn_frame3 = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame3.place(x=0, y=200, width=412, height=40)

        btnAdd = Button(btn_frame3, text="Add", command=self.add_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame3, text="Update", command=self.update_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame3, text="Delete", command=self.delete_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame3, text="Reset", command=self.reset_data, font=("Arial", 12, "bold"), bg="black", fg="gold", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # Table Frame search system
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="Show Room Details", font=("Arial", 12, "bold"), padx=2)
        Table_Frame.place(x=600, y=55, width=600, height=350)

        scroll_x = ttk.Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(Table_Frame, orient=VERTICAL)

        self.room_table = ttk.Treeview(Table_Frame, column=("Floor", "Room No", "Room Type"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.room_table.xview)
        scroll_y.config(command=self.room_table.yview)

        self.room_table.heading("Floor", text="Floor")
        self.room_table.heading("Room No", text="Room No")
        self.room_table.heading("Room Type", text="Room Type")

        self.room_table["show"] = "headings"

        self.room_table.column("Floor", width=100)
        self.room_table.column("Room No", width=100)
        self.room_table.column("Room Type", width=100)

        self.room_table.pack(fill=BOTH, expand=1)
        self.room_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_floor.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                my_cursor.execute("INSERT INTO details (Floor, `Room No`, `Room Type`) VALUES (%s, %s, %s)", (
                    self.var_floor.get(),
                    self.var_RoomNo.get(),
                    self.var_RoomType.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room details added successfully", parent=self.root)
            except Exception as e:
                messagebox.showwarning("Warning", f"Something went wrong: {str(e)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
        my_cursor = conn.cursor()
        my_cursor.execute("SELECT * FROM details")
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
        if row:
            self.var_floor.set(row[0])
            self.var_RoomNo.set(row[1])
            self.var_RoomType.set(row[2])

    def update_data(self):
        if self.var_floor.get() == "" or self.var_RoomNo.get() == "" or self.var_RoomType.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
                my_cursor = conn.cursor()
                query = "UPDATE details SET Floor=%s, `Room Type`=%s WHERE `Room No`=%s"
                my_cursor.execute(query, (
                    self.var_floor.get(),
                    self.var_RoomType.get(),
                    self.var_RoomNo.get(),
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Room details updated successfully", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def delete_data(self):
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "DELETE FROM details WHERE `Room No` = %s"
            my_cursor.execute(query, (self.var_RoomNo.get(),))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Room details deleted successfully", parent=self.root)
        except Exception as err:
            messagebox.showerror("Error", f"Error occurred: {err}", parent=self.root)

    def reset_data(self):
        self.var_floor.set("")
        self.var_RoomNo.set("")
        self.var_RoomType.set("")

if __name__ == "__main__":
    root = Tk()
    obj = RoomDetails(root)
    root.mainloop()
