import os
import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk
# import fitz  # PyMuPDF
from PIL import Image, ImageTk
from pdf2image import convert_from_path
import fitz  # this is pymupdf
import tkinter as tk
from tkinter import simpledialog



def print_selected_pages(input_pdf, password):
    pages_string = get_pages()
    doc = fitz.open(input_pdf)
    if password:
        doc.authenticate(password)
    new_doc = fitz.open()
    pages = extract_pages(pages_string)
    for i in pages:
        new_doc.insert_pdf(doc, from_page=i, to_page=i)

    name = os.path.basename(input_pdf)[:-4] + "_splitted.pdf"
    storage_path = fd.asksaveasfilename(title="Save the Splitted File.", defaultextension=".pdf", initialfile=name, filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
    if not storage_path:
        return
    new_doc.save(storage_path)

def extract_pages(input_string):
    pages = []
    for part in input_string.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            pages.extend(range(start, end+1))
        else:
            pages.append(int(part))
    return [page-1 for page in pages]

def get_pages():
    # Create a simple dialog to get user input
    # root = tk.Tk()
    # root.withdraw()  # Hide the main window
    dialog = ctk.CTkInputDialog(text="Enter the page numbers (comma-separated or range):", title="Split PDF")
    pages = dialog.get_input()  # waits for input
    return pages

def pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

def get_pdf_file_dialog():
    filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))
    return filepath


def show_toast(message):
    toast = ctk.CTkToplevel()
    toast.configure(corner_radius=4)
    toast.overrideredirect(1)

    # Position the toast window
    screen_width = toast.winfo_screenwidth()
    screen_height = toast.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (200/2))
    y_coordinate = int((screen_height) - (100))
    toast.geometry("225x30+{}+{}".format(x_coordinate, y_coordinate))

    # Set the background color and message
    ctk.CTkLabel(toast, text=message, corner_radius=10).pack()

    # Show the toast for 1 second then destroy
    toast.after(2500, toast.destroy)

class DropdownMenu(ctk.CTkButton):
    def __init__(self, master=None, options=None, command=None,**kwargs):
        ctk.CTkButton.__init__(self, master, **kwargs)
        self.menu = ctk.CTkToplevel(self)
        self.menu.withdraw()
        self.menu.overrideredirect(True)
        if options is not None:
            for option in options:
                ctk.CTkButton(self.menu, text=f"  {option}", width=75, fg_color="#2c2c2e", border_color="#202024", border_width=0,corner_radius=0, anchor="w",command=lambda opt=option: self.select_option_trigger(opt, command)).pack(fill='x')
        self.bind('<Button-1>', self.show_menu)

    def select_option_trigger(self, option:str, command=None):
        command(option)
        self.menu.withdraw()

    def show_menu(self, event=None):
        x = self.winfo_rootx()
        y = self.winfo_rooty() + self.winfo_height()
        self.menu.geometry(f'+{x}+{y}')
        self.menu.deiconify()