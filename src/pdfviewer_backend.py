import os
from tkinter import *
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
        self.tab_control = CustomNotebook(root)
        self.image_editor = image_editor.PDFImageEditor(self.app)
        self.dropdown = {
            "Extract Text  ": self.image_editor.extract_text,
            "Extract Page  ": self.image_editor.extract_page,
            "Other Option  ": self.image_editor.extract_text,
            "Another One   ": self.image_editor.extract_page,
        }
        # self.file_dropdown_menu.pack()

    def set_pdfviewer(self, pdf_viewer):
        self.pdf_viewer = pdf_viewer

    def create_new_tab(self, tab_name:str) -> ttk.Frame:
        new_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(new_tab, text=tab_name)
        self.tab_control.select(new_tab)
        self.tab_control.pack(expand=1, fill='both')  # pack the tab control here
        return new_tab, self.tab_control.select()
        # except Exception:
        #     pass


    def show_menu(self, event):
        # Create a menu

        try:
            self.file_dropdown_menu.menu.withdraw()
            self.file_dropdown_menu.place_forget()
        except Exception:
            pass
        self.file_dropdown_menu = func.DropdownMenu(self.tab_control, text='Edit', width=50, fg_color="black", bg_color="transparent", command=self.pdf_viewer.select_dropdown_menu, options=self.dropdown.keys())
        self.file_dropdown_menu.place(x=event.x, y=event.y)
        # popup = Menu(self.app, tearoff=0)
        # popup.add_command(label='Option 1')
        # popup.add_command(label='Option 2')
        # popup.add_command(label='Option 3')

        # Show the menu
        # try:
        #     popup.tk_popup(event.x_root, event.y_root)
        # finally:
        #     # make sure to release the grab (Tk 8.0a1 only)
        #     popup.grab_release()


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

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None
        
        
        pdf_tab, tab_id = self.tab_layout.create_new_tab(os.path.basename(file_path))
        pdf_frame, pdf_text = self.pdf_view.pdf_view(self.app, frame=pdf_tab, pdf_location=file_path, width=400)
        pdf_frame.pack()
        
        pdf_text.bind("<Button-1>", self.tab_layout.show_menu)
        self.text_map[tab_id] = pdf_text


    def save(self) -> None:
        pass
    def export(self) -> None:
        pass
    def close(self) -> None:
        pass
    def exit(self) -> None:
        pass
