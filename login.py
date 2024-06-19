from tkinter import *
from tkinter import ttk, messagebox
import mysql.connector
from PIL import Image, ImageTk
from hotel import HotelManagementSystem  # Assuming 'hotel' module contains HotelManagementSystem


class LoginWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1550x800+0+0")

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Frame for login content
        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        # Login icon
        img1 = Image.open(r"C:\Users\Mabbi\Desktop\project\images\hotel images\LoginIconAppl.png")
        img1 = img1.resize((100, 100), Image.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lblimg1 = Label(frame, image=self.photoimage1, bg="black", borderwidth=0)
        lblimg1.place(x=40, y=40)

        # Get Started label
        get_str = Label(frame, text="Get Started", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=95, y=150)

        # Username label and entry
        username = Label(frame, text="Username", font=("times new roman", 15, "bold"), fg="white", bg="black")
        username.place(x=70, y=200)
        self.txtuser = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.txtuser.place(x=40, y=230, width=270)

        # Password label and entry
        password = Label(frame, text="Password", font=("times new roman", 15, "bold"), fg="white", bg="black")
        password.place(x=70, y=270)
        self.txtpass = ttk.Entry(frame, font=("times new roman", 15, "bold"), show="*")
        self.txtpass.place(x=40, y=300, width=270)

        # Login button
        loginbtn = Button(frame, command=self.login, text="Login", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=110, y=350, width=120, height=35)

        # Register button
        registerbtn = Button(frame, text="New User Register", command=self.registerwindow, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        registerbtn.place(x=15, y=400, width=160)

        # Forgot button
        forgotbtn = Button(frame, text="Forgot Password?", command=self.forgot_password_Window, font=("times new roman", 10, "bold"), borderwidth=0, fg="white", bg="black", activeforeground="white", activebackground="black")
        forgotbtn.place(x=10, y=420, width=160)

    def registerwindow(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def login(self):
        if self.txtuser.get() == "" or self.txtpass.get() == "":
            messagebox.showerror("Error", "All fields required")
        elif self.txtuser.get() == "kapu" and self.txtpass.get() == "ashu":
            messagebox.showinfo("Success", "Welcome to code with Mabbi")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            my_cursor.execute("SELECT * FROM register WHERE email=%s AND password=%s", (self.txtuser.get(), self.txtpass.get()))
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Invalid username & password")
            else:
                open_main = messagebox.askyesno("YesNo", "Access only admin")
                if open_main:
                    self.new_window = Toplevel(self.root)
                    self.app = HotelManagementSystem(self.new_window)
                else:
                    return
            conn.commit()
            conn.close()

    def forgot_password_Window(self):
        if self.txtuser.get() == "":
            messagebox.showerror("Error", "Please enter the email address to reset password")
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.txtuser.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is None:
                messagebox.showerror("Error", "Please enter the valid user name")
            else:
                conn.close()
                self.root2 = Toplevel()
                self.root2.title("Forget Password")
                self.root2.geometry("340x450+610+170")

                l = Label(self.root2, text="Forget Password", font=("times new roman", 20, "bold"), fg="red", bg="white")
                l.place(x=0, y=10, relwidth=1)

                security_Q_lbl = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg="white")
                security_Q_lbl.place(x=50, y=80)

                self.combo_security_Q = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state='readonly')
                self.combo_security_Q["values"] = ("Select", "Your Birth Place", "Your Father's Name", "Your Pet Name")
                self.combo_security_Q.place(x=50, y=110, width=250)
                self.combo_security_Q.current(0)

                security_A_lbl = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg="white")
                security_A_lbl.place(x=50, y=150)

                self.txt_security = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_security.place(x=50, y=180, width=250)

                new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg="white")
                new_password.place(x=50, y=220)

                self.txt_new_pass_entry = ttk.Entry(self.root2, font=("times new roman", 15, "bold"))
                self.txt_new_pass_entry.place(x=50, y=250, width=250)

                btn = Button(self.root2, text="Reset", font=("times new roman", 15, "bold"), fg="white", bg="green", command=self.reset)
                btn.place(x=100, y=290)

    def reset(self):
        if self.combo_security_Q.get() == "Select":
            messagebox.showerror("Error", "Select the security question", parent=self.root2)
        elif self.txt_security.get() == "":
            messagebox.showerror("Error", "Please enter the answer", parent=self.root2)
        elif self.txt_new_pass_entry.get() == "":
            messagebox.showerror("Error", "Please enter the new password", parent=self.root2)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s and securityQ=%s and securityA=%s"
            value = (self.txtuser.get(), self.combo_security_Q.get(), self.txt_security.get())
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()
            if row is None:
                messagebox.showerror("Error", "Please enter the correct answer")
            else:
                query = "update register set password=%s where email=%s"
                value = (self.txt_new_pass_entry.get(), self.txtuser.get())
                my_cursor.execute(query, value)
                conn.commit()
                conn.close()
                messagebox.showinfo("Info", "Your password has been reset, please login with new password", parent=self.root2)
                self.root2.destroy()


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("New Registration")
        self.root.geometry("1600x900+0+0")

        # Variables
        self.var_fname = StringVar()
        self.var_lname = StringVar()
        self.var_contact = StringVar()
        self.var_email = StringVar()
        self.var_securityQ = StringVar()
        self.var_securityA = StringVar()
        self.var_pass = StringVar()
        self.var_confpass = StringVar()

        # Background image
        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\0-3450_3d-nature-wallpaper-hd-1080p-free-download-new.jpg")
        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        # Left image
        self.left = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\anaya.jpg")
        lbl_left = Label(self.root, image=self.left)
        lbl_left.place(x=80, y=100, width=400, height=550)

        # Registration Frame
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=480, y=100, width=700, height=550)

        title = Label(frame1, text="Registration Here", font=("times new roman", 20, "bold"), bg="white", fg="green")
        title.place(x=50, y=30)

        # First Name
        fname = Label(frame1, text="First Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        fname.place(x=50, y=100)
        self.fname_entry = ttk.Entry(frame1, textvariable=self.var_fname, font=("times new roman", 15, "bold"))
        self.fname_entry.place(x=50, y=130, width=250)

        # Last Name
        lname = Label(frame1, text="Last Name", font=("times new roman", 15, "bold"), bg="white", fg="black")
        lname.place(x=370, y=100)
        self.lname_entry = ttk.Entry(frame1, textvariable=self.var_lname, font=("times new roman", 15, "bold"))
        self.lname_entry.place(x=370, y=130, width=250)

        # Contact
        contact = Label(frame1, text="Contact No.", font=("times new roman", 15, "bold"), bg="white", fg="black")
        contact.place(x=50, y=170)
        self.contact_entry = ttk.Entry(frame1, textvariable=self.var_contact, font=("times new roman", 15, "bold"))
        self.contact_entry.place(x=50, y=200, width=250)

        # Email
        email = Label(frame1, text="Email", font=("times new roman", 15, "bold"), bg="white", fg="black")
        email.place(x=370, y=170)
        self.email_entry = ttk.Entry(frame1, textvariable=self.var_email, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=370, y=200, width=250)

        # Security Question
        securityQ = Label(frame1, text="Security Question", font=("times new roman", 15, "bold"), bg="white", fg="black")
        securityQ.place(x=50, y=240)
        self.combo_securityQ = ttk.Combobox(frame1, textvariable=self.var_securityQ, font=("times new roman", 15, "bold"), state='readonly')
        self.combo_securityQ['values'] = ("Select", "Your Birth Place", "Your Father Name", "Your Pet Name")
        self.combo_securityQ.place(x=50, y=270, width=250)
        self.combo_securityQ.current(0)

        # Security Answer
        securityA = Label(frame1, text="Security Answer", font=("times new roman", 15, "bold"), bg="white", fg="black")
        securityA.place(x=370, y=240)
        self.securityA_entry = ttk.Entry(frame1, textvariable=self.var_securityA, font=("times new roman", 15, "bold"))
        self.securityA_entry.place(x=370, y=270, width=250)

        # Password
        password = Label(frame1, text="Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        password.place(x=50, y=310)
        self.password_entry = ttk.Entry(frame1, textvariable=self.var_pass, font=("times new roman", 15, "bold"))
        self.password_entry.place(x=50, y=340, width=250)

        # Confirm Password
        confpass = Label(frame1, text="Confirm Password", font=("times new roman", 15, "bold"), bg="white", fg="black")
        confpass.place(x=370, y=310)
        self.confpass_entry = ttk.Entry(frame1, textvariable=self.var_confpass, font=("times new roman", 15, "bold"))
        self.confpass_entry.place(x=370, y=340, width=250)

        # Check Box
        self.var_chk = IntVar()
        chk = Checkbutton(frame1, text="I Agree The Terms & Conditions", variable=self.var_chk, onvalue=1, offvalue=0, bg="white", font=("times new roman", 12, "bold"))
        chk.place(x=50, y=380)

        # Register Button
        regbtn = Button(frame1, text="Register", font=("times new roman", 15, "bold"), bg="green", fg="white", bd=0, cursor="hand2", command=self.register_data)
        regbtn.place(x=50, y=420, width=250)

        # Login Button
        loginbtn = Button(self.root, command=self.login_window, text="Sign In", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        loginbtn.place(x=500, y=530, width=150)

    def login_window(self):
        self.root.destroy()

    def register_data(self):
        if self.var_fname.get() == "" or self.var_lname.get() == "" or self.var_contact.get() == "" or self.var_email.get() == "" or self.var_securityQ.get() == "Select" or self.var_securityA.get() == "" or self.var_pass.get() == "" or self.var_confpass.get() == "":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        elif self.var_pass.get() != self.var_confpass.get():
            messagebox.showerror("Error", "Password & Confirm Password should be same", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror("Error", "Please agree to our terms & conditions", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="mabbi515", database="new1")
            my_cursor = conn.cursor()
            query = "select * from register where email=%s"
            value = (self.var_email.get(),)
            my_cursor.execute(query, value)
            row = my_cursor.fetchone()

            if row is not None:
                messagebox.showerror("Error", "User already exists, please try another email", parent=self.root)
            else:
                my_cursor.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)", (
                self.var_fname.get(), self.var_lname.get(), self.var_contact.get(), self.var_email.get(), self.var_securityQ.get(), self.var_securityA.get(), self.var_pass.get()))
                conn.commit()
                conn.close()
                messagebox.showinfo("Success", "Register Successful", parent=self.root)
                self.root.destroy()


root = Tk()
obj = LoginWindow(root)
root.mainloop()
