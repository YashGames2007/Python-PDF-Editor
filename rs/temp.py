import tkinter as tk
import customtkinter as ctk
from tkinter import filedialog
import ctkPDFViewer as pdf

def open_pdf():
    file_path = filedialog.askopenfilename()
    pdf_view = pdf.ShowPdf()
    pdf_frame = pdf_view.pdf_view(root, pdf_location=file_path)
    pdf_frame.pack()

root = ctk.CTk()

button = ctk.CTkButton(root, text="Open PDF", command=open_pdf)
button.pack()

root.mainloop()