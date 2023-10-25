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
        return new_tab



class PDFViewerFunctions:
    def __init__(self, root) -> None:
        self.app = root
        self.tab_layout = TabLayout(self.app)
        self.pdf_view = pdf_viewer.ShowPdf()

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None
        
        
        pdf_tab = self.tab_layout.create_new_tab(os.path.basename(file_path))
        pdf_frame = self.pdf_view.pdf_view(self.app, frame=pdf_tab, pdf_location=file_path, width=400)
        pdf_frame.pack()


    def save(self) -> None:
        pass
    def export(self) -> None:
        pass
    def close(self) -> None:
        pass
    def exit(self) -> None:
        pass
