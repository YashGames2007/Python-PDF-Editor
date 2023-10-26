import os
from tkinter import *
from tkinter import ttk
from ctknotebook import CustomNotebook
from tkinter import filedialog as fd
import customtkinter as ctk
import ctkPDFViewer as pdf_viewer
from PIL import ImageTk, Image
# from miner import PDFMiner
import pdfviewer_helper_functions as func

class TabLayout:
    def __init__(self, root) -> None:
        self.tab_control = CustomNotebook(root)

    def create_new_tab(self, tab_name:str) -> ttk.Frame:
        new_tab = ttk.Frame(self.tab_control)
        self.tab_control.add(new_tab, text=tab_name)
        self.tab_control.select(new_tab)
        self.tab_control.pack(expand=1, fill='both')  # pack the tab control here
        return new_tab, self.tab_control.select()



class PDFViewerFunctions:
    def __init__(self, root) -> None:
        self.app = root
        self.tab_layout = TabLayout(self.app)
        self.text_map = {}
        self.pdf_view = pdf_viewer.ShowPdf()

    def get_page(self, event):
        try:
            id = self.tab_layout.tab_control.select()
            text_widget = self.text_map[id]
            pages = self.pdf_view.pdf_objects[text_widget]

            # Get the name of the image under the cursor
            index = int(text_widget.image_cget("current", "name"))
            print(f"Selected image: '{index}', {len(pages)}")
            current_page = pages[index]

            # width, height = current_page.width(), current_page.height()
            # img = Image.frombytes("RGBA", (width, height), data)
            # img.show()


        except Exception as e:
            # No image under the cursor
            print(e)
            pass

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None
        
        
        pdf_tab, tab_id = self.tab_layout.create_new_tab(os.path.basename(file_path))
        pdf_frame, pdf_text = self.pdf_view.pdf_view(self.app, frame=pdf_tab, pdf_location=file_path, width=400)
        pdf_frame.pack()
        
        pdf_text.bind("<Button-1>", self.get_page)
        self.text_map[tab_id] = pdf_text


    def save(self) -> None:
        pass
    def export(self) -> None:
        pass
    def close(self) -> None:
        pass
    def exit(self) -> None:
        pass
