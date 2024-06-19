from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox

class ForgotPasswordWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Forgot Password")
        self.root.geometry("1550x800+0+0")

        self.bg = ImageTk.PhotoImage(file=r"C:\Users\Mabbi\Desktop\project\images\hotel images\SDT_Zoom-Backgrounds_April-8_Windansea-1-logo-1.jpg")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="black")
        frame.place(x=610, y=170, width=340, height=450)

        get_str = Label(frame, text="Reset Password", font=("times new roman", 20, "bold"), fg="white", bg="black")
        get_str.place(x=70, y=100)

        email_label = Label(frame, text="Email", font=("times new roman", 15, "bold"), fg="white", bg="black")
        email_label.place(x=70, y=155)

        self.email_entry = ttk.Entry(frame, font=("times new roman", 15, "bold"))
        self.email_entry.place(x=40, y=180, width=270)

        reset_btn = Button(frame, command=self.reset_password, text="Reset Password", font=("times new roman", 15, "bold"), bd=3, relief=RIDGE, fg="white", bg="red", activeforeground="white", activebackground="red")
        reset_btn.place(x=110, y=250, width=120, height=35)

    def reset_password(self):
        if self.email_entry.get() == "":
            messagebox.showerror("Error", "Email field is required")
        else:
            messagebox.showinfo("Success", "A password reset link has been sent to your email")

if __name__ == "__main__":
    root = Tk()
    app = ForgotPasswordWindow(root)
    root.mainloop()
