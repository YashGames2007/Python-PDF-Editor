import tkinter as tk

class YourClass:
    def __init__(self, master):
        self.master = master
        self.password = ""
        self.password_window = None
        self.password_entry = None

    def open_pdf(self):
        password = self.password_entry.get()
        self.password_window.destroy()
        # pdf_file = fitz.open('your_pdf_file.pdf')
        # if pdf_file.is_encrypted:
        #     pdf_file.authenticate(password)
        #     # ttk.messagebox.showinfo("Success", "PDF file opened successfully!")
        self.password = password

    def get_password(self):
        self.password_window = tk.Toplevel(self.master)
        self.password_window.title('Enter Password')

        password_label = tk.Label(self.password_window, text="Enter Password:")
        password_label.pack()

        self.password_entry = tk.Entry(self.password_window, show="*")
        self.password_entry.pack()

        submit_button = tk.Button(self.password_window, text="Submit", command=self.open_pdf)
        submit_button.pack()
