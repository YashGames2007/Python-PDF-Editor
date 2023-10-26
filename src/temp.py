import tkinter as tk
from tkinter import messagebox
import fitz  # PyMuPDF

def open_pdf():
    password = password_entry.get()
    password_window.destroy()
    try:
        pdf_file = fitz.open('your_pdf_file.pdf')
        if pdf_file.is_encrypted:
            pdf_file.authenticate(password)
            messagebox.showinfo("Success", "PDF file opened successfully!")
        else:
            messagebox.showinfo("Info", "PDF file is not encrypted.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

root = tk.Tk()
root.title('PDF Reader')

open_button = tk.Button(root, text="Open PDF", command=lambda: password_window.deiconify())
open_button.pack()

password_window = tk.Toplevel(root)
password_window.title('Enter Password')
password_window.withdraw()

password_label = tk.Label(password_window, text="Enter Password:")
password_label.pack()

password_entry = tk.Entry(password_window, show="*")
password_entry.pack()

submit_button = tk.Button(password_window, text="Submit", command=open_pdf)
submit_button.pack()

root.mainloop()
