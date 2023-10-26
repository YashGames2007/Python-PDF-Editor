import tkinter as tk
from tkinter import filedialog

def save_as():
    root = tk.Tk()
    root.withdraw()  # to hide the main window

    # open save file dialog
    file_path = filedialog.asksaveasfilename(defaultextension=".pdf", initialfile='Merged.pdf', filetypes=(("PDF files", "*.pdf"), ("All files", "*.*")))

    if file_path:
        print(f"File will be saved at: {file_path}")
        # Here you can add the code to write the PDF file to `file_path`

save_as()
