import fitz
import tkinter as tk
from tkinter import filedialog

class PDFZoomApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PDF Zoom App")

        self.zoom_factor = 1.0  # Initial zoom factor
        self.pdf_document = None

        self.load_button = tk.Button(root, text="Load PDF", command=self.load_pdf)
        self.load_button.pack()

        self.zoom_in_button = tk.Button(root, text="Zoom In", command=self.zoom_in)
        self.zoom_in_button.pack()

        self.zoom_out_button = tk.Button(root, text="Zoom Out", command=self.zoom_out)
        self.zoom_out_button.pack()

    def load_pdf(self):
        file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])

        if file_path:
            self.pdf_document = fitz.open(file_path)

    def zoom_in(self):
        if self.pdf_document:
            self.zoom_factor *= 1.2  # Adjust the zoom factor as needed
            self.update_pdf_display()

    def zoom_out(self):
        if self.pdf_document:
            self.zoom_factor /= 1.2  # Adjust the zoom factor as needed
            self.update_pdf_display()

    def update_pdf_display(self):
        if self.pdf_document:
            for page in self.pdf_document:
                page.set_zoom(self.zoom_factor)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = PDFZoomApp(root)
    app.run()