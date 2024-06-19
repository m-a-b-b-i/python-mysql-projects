from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector

class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New Registration")
        self.root.geometry("1600x900+0+0")

        # variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # bg image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        bg_lbl = Label(self.root, image=self.bg)
        bg_lbl.place(x=0, y=0, relwidth=1, relheight=1)

        # left image
        self.bg1 = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\thought-good-morning-messages-LoveSove.jpg")
        left_lbl = Label(self.root, image=self.bg1)
        left_lbl.place(x=50, y=100, width=470, height=550)

        # main frame
        frame = Frame(self.root, bg="white")
        frame.place(x=520, y=100, width=800, height=550)

        register_lbl = Label(frame, text="REGISTER HERE", font=("times new roman", 20, "bold"), fg="dark green", bg="white")
        register_lbl.place(x=20, y=20)

        # label and entry
        # row 1
        fname_lbl = Label(frame, text="First Name", font=("times new roman", 15, "bold"), bg="white")
        fname_lbl.place(x=50, y=100)

        fname_entry = ttk.Entry(frame, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        fname_entry.place(x=50, y=130, width=250)

        lname_lbl = Label(frame, text="Last Name", font=("times new roman", 15, "bold"), bg="white")
        lname_lbl.place(x=370, y=100)

        lname_entry = ttk.Entry(frame, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        lname_entry.place(x=370, y=130, width=250)

        # row 2
        contact_lbl = Label(frame, text="Contact No", font=("times new roman", 15, "bold"), bg="white")
        contact_lbl.place(x=50, y=170)

        contact_entry = ttk.Entry(frame, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        contact_entry.place(x=50, y=200, width=250)

        email_lbl = Label(frame, text="Email", font=("times new roman", 15, "bold"), bg="white")
        email_lbl.place(x=370, y=170)

        email_entry = ttk.Entry(frame, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        email_entry.place(x=370, y=200, width=250)

        # row 3
        security_Q_lbl = Label(frame, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
        security_Q_lbl.place(x=50, y=240)

        self.combo_security_Q = ttk.Combobox(frame, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state='readonly')
        self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
        self.combo_security_Q.place(x=50, y=270, width=250)
        self.combo_security_Q.current(0)

        security_A_lbl = Label(frame, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
        security_A_lbl.place(x=370, y=240)

        security_A_entry = ttk.Entry(frame, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        security_A_entry.place(x=370, y=270, width=250)

        # row 4
        pswd_lbl = Label(frame, text="Password", font=("times new roman", 15, "bold"), bg="white")
        pswd_lbl.place(x=50, y=310)

        pswd_entry = ttk.Entry(frame, textvariable=self.var_pass, font=("times new roman", 15, "bold"), show="*")
        pswd_entry.place(x=50, y=340, width=250)

        confirm_pswd_lbl = Label(frame, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white")
        confirm_pswd_lbl.place(x=370, y=310)

        confirm_pswd_entry = ttk.Entry(frame, textvariable=self.var_confpass, font=("times new roman", 15, "bold"), show="*")
        confirm_pswd_entry.place(x=370, y=340, width=250)

        # check button
        self.var_check = IntVar()
        self.checkbtn = Checkbutton(frame, variable=self.var_check, text="I agree to the terms and conditions", font=("times new roman", 15, "bold"), onvalue=1, offvalue=0)
        self.checkbtn.place(x=50, y=380)

        # buttons
        img = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\register-now-button1.jpg")
        img = img.resize((200, 50), Image.LANCZOS)
        
        
        
        
        self.photoimage = ImageTk.PhotoImage(img)
        b1 = Button(frame, command=self.register_data, image=self.photoimage, borderwidth=0, cursor="hand2")
        b1.place(x=10, y=420, width=200)

        img1 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\loginpng.png")
        img1 = img1.resize((200, 50), Image.LANCZOS)

      
        self.photoimage1 = ImageTk.PhotoImage(img1)
        b2 = Button(frame, image=self.photoimage1, borderwidth=0, cursor="hand2")
        b2.place(x=330, y=420, width=200)

    # function declaration
    def register_data(self):
        if self.var_fname.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select":
            messagebox.showerror("Error", "All fields are required")
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password and confirm password must be the same")
        elif self.var_check.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms and conditions")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "SELECT * FROM register WHERE email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email")
            else:
                my_cursor.execute("INSERT INTO register (fname, lname, contact, email, securityQ, securityA, password) VALUES (%s, %s, %s, %s, %s, %s, %s)", (
    self.var_fname.get(),
    self.var_lname.get(),
    self.var_contact.get(),
    self.var_email.get(),
    self.var_securityQ.get(),
    self.var_securityA.get(),
    self.var_pass.get()
))

               

               
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Registered Successfully")

if __name__ == "__main__":
    root = Tk()
    app = Register(root)
    root.mainloop()
