import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import customtkinter as ctk
import ctkPDFViewer as pdf_viewer
from PIL import ImageTk, Image
# from miner import PDFMiner
import pdfviewer_helper_functions as func

class PDFViewerFunctions:
    def __init__(self, root) -> None:
        self.app = root

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None
        
        pdf_view = pdf_viewer.ShowPdf()
        pdf_frame, max_width = pdf_view.pdf_view(self.app, pdf_location=file_path, width=400)
        pdf_frame.pack()
        cur_width = self.app.winfo_width()
        cur_height = self.app.winfo_height()
        # print(f"Current: {cur_width}, Desired: {max_width}")
        # self.app.geometry(f"{max_width}x{cur_height}")


        # Bind the mouse wheel to scroll the canvas
    def save(self) -> None:
        pass
    def export(self) -> None:
        pass
    def close(self) -> None:
        pass
    def exit(self) -> None:
        pass
