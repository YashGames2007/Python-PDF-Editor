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
        self.app = root
        self.canvas = Canvas(self.app, borderwidth=0)
        self.frame = ctk.CTkFrame(self.canvas)
        self.canvas.configure(background=self.app.cget("bg"), highlightbackground=self.app.cget("bg"))
        self.frame.configure(width=self.canvas.winfo_width(), height=self.canvas.winfo_height())
        self.frame.pack()
        self.tab_control = CustomNotebook(self.frame)
        self.tab_control.bind("<MouseWheel>", self.on_mousewheel)
        self.tab_scroller = Scrollbar(self.app, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.tab_scroller.set)

        self.canvas.pack(side="bottom", fill="both", expand=True)
        # self.vsb.grid(row=0, column=0, sticky="ew")

        self.canvas.create_window((3,2), window=self.frame, anchor="nw", tags="self.frame")
        self.frame.bind("<Configure>", self.frame_configure)



    def create_new_tab(self, tab_name:str) -> ttk.Frame:
        new_tab = ctk.CTkFrame(self.tab_control)
        new_tab.pack(side=TOP, fill="both")
        self.tab_control.add(new_tab, text=tab_name)
        self.tab_control.select(new_tab)
        self.tab_control.pack(expand=1, fill='both')  # pack the tab control here
        return new_tab
    
    def frame_configure(self, event):
        x1, y1, _, y2 = self.canvas.bbox("all")
        max_width = max(self.frame.winfo_width(), self.canvas.winfo_width())
        self.canvas.configure(scrollregion=(x1, y1, max_width, y2))

    def on_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")




class PDFViewerFunctions:
    def __init__(self, root) -> None:
        self.app = root
        self.tab_layout = TabLayout(self.app)
        self.pdf_frames = []
        self.pdf_view = pdf_viewer.ShowPdf()

    def open(self) -> None:
        # Get a PDF from User Input
        file_path = func.get_pdf_file_dialog()
        if not file_path:
            return None

        pdf_tab = self.tab_layout.create_new_tab(os.path.basename(file_path))
        pdf_frame, pdf = self.pdf_view.pdf_view(self.app, frame=pdf_tab, pdf_location=file_path, width=400)
        self.pdf_frames.append(pdf)
        pdf_frame.pack()
        # pdf.pack()


    def save(self) -> None:
        pass
    def export(self) -> None:
        pass
    def close(self) -> None:
        pass
    def exit(self) -> None:
        pass
