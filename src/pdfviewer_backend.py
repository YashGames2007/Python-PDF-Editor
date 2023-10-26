import os
import sys
import pikepdf
from tkinter import *
import tkinter as tk
from tkinter import ttk
from ctknotebook import CustomNotebook
from tkinter import filedialog as fd
import customtkinter as ctk
import ctkPDFViewer as pdf_viewer
import fitz  # PyMuPDF
from CTkMenuBar import dropdown_menu
from PIL import ImageTk, Image
# from miner import PDFMiner
import pdfviewer_helper_functions as func
import image_editor

class TabLayout:
    def __init__(self, root) -> None:
        self.app = root
        self.tab_control = CustomNotebook(master=root, on__close=self.delete_tab)
        self.image_editor = image_editor.PDFImageEditor(self.app)
        self.dropdown = {
            "Extract Text  ": self.image_editor.extract_text,
            "Extract Page  ": self.image_editor.extract_page,
            "Other Option  ": self.image_editor.extract_text,
            "Another One   ": self.image_editor.extract_page,
        }

    def set_pdfviewer(self, pdf_viewer):
        self.pdf_viewer = pdf_viewer

    def delete_tab(self, tab_id):
        self.pdf_viewer.close(tab_id)

    def create_new_tab(self, tab_name:str) -> ttk.Frame:
        new_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(new_tab, text=tab_name)
        self.tab_control.select(new_tab)
        self.tab_control.pack(expand=1, fill='both')  # pack the tab control here
        return new_tab, self.tab_control.index(self.tab_control.select())



    def show_menu(self, event):

        try:
            self.file_dropdown_menu.menu.withdraw()
            self.file_dropdown_menu.place_forget()
        except Exception:
            pass
        self.file_dropdown_menu = func.DropdownMenu(self.tab_control, text='Edit', width=50, fg_color="black", bg_color="transparent", command=self.pdf_viewer.select_dropdown_menu, options=self.dropdown.keys())
        self.file_dropdown_menu.place(x=event.x, y=event.y)


class PDFViewerFunctions:
    def __init__(self, root) -> None:
        self.app = root
        self.tab_layout = TabLayout(self.app)
        self.text_map = {}
        self.pdf_view = pdf_viewer.ShowPdf()
        self.tab_layout.set_pdfviewer(self)
        # self.tab_layout.set_widget(self.)


    def select_dropdown_menu(self, option):
        pdf_path, page_no, password = self.get_pdf()
        self.tab_layout.dropdown[option](pdf_path, page_no, password)
        self.tab_layout.file_dropdown_menu.place_forget()

    def get_pdf(self):
        try:
            id = self.tab_layout.tab_control.select()
            text_widget = self.text_map[id]
            photo_image_pages, path, password = self.pdf_view.pdf_objects[text_widget]

            # Get the name of the image under the cursor
            index = int(text_widget.image_cget("current", "name"))
            return path, index, password
        except Exception as e:
            pass

    def save(self) -> None:
        current_tab_id = self.tab_layout.tab_control.index(self.tab_layout.tab_control.select())
        _, path, password = self.pdf_view.pdf_objects[self.text_map[current_tab_id]]
        pdf = pikepdf.Pdf.open(path) if password is None else pikepdf.Pdf.open(path, password=password, allow_overwriting_input=True)
        default_name = os.path.basename(path)[:-4] + "_copy.pdf"
        storage_path = fd.asksaveasfilename(title="Save Copy of PDF as", defaultextension=".pdf", initialfile=default_name, filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
        if not storage_path:
            return
        pdf.save(storage_path)
        pdf.close()

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None
        
        
        pdf_tab, tab_id = self.tab_layout.create_new_tab(os.path.basename(file_path))
        output = self.pdf_view.pdf_view(self.app, frame=pdf_tab, pdf_location=file_path, width=400)
        if not output:
            self.close()
            return
        pdf_frame, pdf_text = output
        pdf_frame.pack()
        
        pdf_text.bind("<Button-1>", self.tab_layout.show_menu)
        self.text_map[tab_id] = pdf_text


    def encrypt(self) -> None:
        current_tab_id = self.tab_layout.tab_control.index(self.tab_layout.tab_control.select())
        _, path, password = self.pdf_view.pdf_objects[self.text_map[current_tab_id]]
        pdf = pikepdf.Pdf.open(path) if password is None else pikepdf.Pdf.open(path, password=password)
        default_name = os.path.basename(path)[:-4] + "_encrypted.pdf"
        password_window = ctk.CTkInputDialog(text="Enter password for PDF Encryption", title="Encrypt PDF")
        password = password_window.get_input()
        if not password:
            return
        storage_path = fd.asksaveasfilename(title="Save Encrypted PDF as", defaultextension=".pdf", initialfile=default_name, filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
        if not storage_path:
            return
        pdf.save(storage_path, encryption=pikepdf.Encryption(owner=password, user=password, R=4))
        pdf.close()

    def merge(self) -> None:
        merged_pdf = fitz.open()

        if len(self.pdf_view.pdf_objects.items()) < 2:
            tk.messagebox.showerror("Error", str("Open at least 2 PDFs to merge them.!"))
            return

        for text, value in self.pdf_view.pdf_objects.items():
            _, path, password = value
            pdf = fitz.open(path)
            if password:
                pdf.authenticate(password)
            merged_pdf.insert_pdf(pdf)
        
        storage_path = fd.asksaveasfilename(title="Save the Merged File.", defaultextension=".pdf", initialfile='Merged.pdf', filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))
        merged_pdf.save(storage_path)

    def split(self) -> None:
        current_tab_id = self.tab_layout.tab_control.index(self.tab_layout.tab_control.select())
        _, path, password = self.pdf_view.pdf_objects[self.text_map[current_tab_id]]
        func.print_selected_pages(path, password)

    def export(self) -> None:
        print("Pressed export")

    def close(self, tab_id=None) -> None:
        if tab_id is None:
            try:
                tab_id = self.tab_layout.tab_control.index(self.tab_layout.tab_control.select())
                self.tab_layout.tab_control.forget(tab_id)
            except:
                pass
        # tab_id = self.tab_layout.tab_control.index(tab_id)
        try:
            del self.pdf_view.pdf_objects[self.text_map[tab_id]]
        except:
            pass
        try:
            del self.text_map[tab_id]
        except:
            pass

    def exit(self) -> None:
        self.app.destroy()
        sys.exit()