import os
import tkinter as tk
from tkinter import filedialog as fd
import customtkinter as ctk
import fitz  # PyMuPDF
from PIL import Image, ImageTk
from pdf2image import convert_from_path

def pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

def get_pdf_file_dialog():
    filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))
    return filepath

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