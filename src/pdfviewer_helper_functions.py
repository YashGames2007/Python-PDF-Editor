import os
import tkinter as tk
from tkinter import filedialog as fd
import fitz  # PyMuPDF
from PIL import Image, ImageTk
from pdf2image import convert_from_path

def pdf_to_images(pdf_path):
    return convert_from_path(pdf_path)

def get_pdf_file_dialog():
    filepath = fd.askopenfilename(title='Select a PDF file', initialdir=os.getcwd(), filetypes=(('PDF', '*.pdf'), ))
    return filepath
