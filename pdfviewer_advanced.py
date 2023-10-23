import os
from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
import customtkinter as ctk
from CTkMenuBar import menu_bar, CustomDropdownMenu
from PIL import ImageTk, Image
from miner import PDFMiner
import pdfviewer_backend as backend

ctk.set_appearance_mode("System")  # Modes: system (default), light, dark
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


    def select_option_file_menu(self, option):
        print(f'Option selected: {option}')
        self.menubar["File"][option]()
    
    def build_layout(self):
        # Create a Frame for the menubar
        self.menubar_frame = menu_bar.CTkMenuBar(self.app, bg_color="#2c2c2e")

        # Create a DropdownMenu for menu in menubar frame
        for menu, dropdown in self.menubar.items():
            menu_button = self.menubar_frame.add_cascade(text=menu)
            menu_dropdown = CustomDropdownMenu(widget=menu_button, hover_color="#144870", width=100, border_color="black", border_width=0.2, corner_radius=0,font=ctk.CTkFont(family="sans-serif", size=12))
            for item, runner in dropdown.items():
                menu_dropdown.add_option(option=item, command=runner)

        # file_dropdown_menu = DropdownMenu(menubar_frame, text='File', width=40, fg_color="transparent", command=self.select_option_file_menu, options=self.menubar["File"].keys())
        # file_dropdown_menu.pack(side='left')
    
    def map_functions(self):
        self.menubar = {}
        self.menubar["File"] = {
            "Open": self.backend.open,
            "Save": self.backend.save,
            "Export": self.backend.export,
            "Close": self.backend.close,
            "Exit": self.backend.exit,
        }
        self.menubar["Other"] = {
            "Open": self.backend.open,
            "Save": self.backend.save,
            "Export": self.backend.export,
            "Close": self.backend.close,
            "Exit": self.backend.exit,
        }
        self.menubar_commands = {
            "File": self.select_option_file_menu,
            "Other": self.select_option_file_menu
        }

    def launch(self):
        self.app.mainloop()





def button_function():
    print("button pressed")

# Use CTkButton instead of tkinter Button
# button = ctk.CTkButton(master=app, text="CTkButton", command=button_function)
# button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

if __name__ == "__main__":
    pdfViewer = PDFViewer()
    pdfViewer.launch()