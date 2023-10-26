import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import customtkinter as ctk
from CTkMenuBar import menu_bar, CustomDropdownMenu
# from PIL import ImageTk, Image
# from miner import PDFMiner
import pdfviewer_backend as backend

ctk.set_appearance_mode("dark")  # Modes: system (default), light, dark
ctk.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green

class PDFViewer():
    width = 500
    height = 500

    def __init__(self):
        
        self.app = ctk.CTk()
        self.backend = backend.PDFViewerFunctions(self.app)
        self.app.geometry(f"{self.width}x{self.height}")
        self.map_functions()
        self.build_layout()

    def build_layout(self):
        # Create a Frame for the menubar
        self.drop_down = {}
        self.menubar_frame = menu_bar.CTkMenuBar(self.app, bg_color="#2c2c2e")

        # Create a DropdownMenu for menu in menubar frame
        for menu, dropdown in self.menubar.items():
            menu_button = self.menubar_frame.add_cascade(text=menu)
            menu_dropdown = CustomDropdownMenu(widget=menu_button, hover_color="#144870", width=100, border_color="black", border_width=0.2, corner_radius=0,font=ctk.CTkFont(family="sans-serif", size=12))
            self.drop_down[menu] = menu_dropdown
            for item, runner in dropdown.items():
                if type(runner) == dict:
                    sub_menu = menu_dropdown.add_submenu("Export As", hover_color="#144870", border_color="black", border_width=0.2, corner_radius=0,font=ctk.CTkFont(family="sans-serif", size=12))
                    for sub_item, sub_runner in runner.items():
                        sub_menu.add_option(option=sub_item, command=sub_runner)
                else:
                    menu_dropdown.add_option(option=item, command=runner)

    
    def map_functions(self):
        self.menubar = {}
        self.menubar["File"] = {
            "Open": self.backend.open,
            "Save": self.backend.save,
            "Export": {
                ".HTML": self.backend.export_to_html,
                ".JPG/JPEG": self.backend.export_to_jpg,
            },
            "Close": self.backend.close,
            "Exit": self.backend.exit,
            "Close Menu": self.close_menu,
        }
        self.menubar["Edit"] = {
            "Encrypt": self.backend.encrypt,
            "Rename": self.backend.rename,
            "Merge": self.backend.merge,
            "Split": self.backend.split,
            "Close Menu": self.close_menu,
        }

    def close_menu(self, event=None):
        for menu, dropdown in self.drop_down.items():
            dropdown.hide_everything()

    def launch(self):
        self.app.mainloop()


if __name__ == "__main__":
    
    pdfViewer = PDFViewer()
    pdfViewer.launch()