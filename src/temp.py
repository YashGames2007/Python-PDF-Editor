import fitz  # this is pymupdf
import tkinter as tk
from tkinter import simpledialog

def print_selected_pages(input_pdf, output_pdf, pages_string):
    doc = fitz.open(input_pdf)
    new_doc = fitz.open()
    pages = extract_pages(pages_string)
    for i in pages:
        new_doc.insert_pdf(doc, from_page=i, to_page=i)

    new_doc.save(output_pdf)

def extract_pages(input_string):
    pages = []
    for part in input_string.split(','):
        if '-' in part:
            start, end = map(int, part.split('-'))
            pages.extend(range(start, end+1))
        else:
            pages.append(int(part))
    return [page-1 for page in pages]

def get_pages():
    # Create a simple dialog to get user input
    root = tk.Tk()
    root.withdraw()  # Hide the main window
    pages_str = simpledialog.askstring("Page Numbers", "Enter the page numbers (comma-separated or range):")
    return pages_str

# Call the function with the input PDF file and the output file
pages_to_print = get_pages()
# print(pages_to_print)



# Test the function
# print(extract_pages("1,3,5-7, 13, 2-4"))

print_selected_pages('D:\\Programming files\\GitHub\\Repositories\\Python-PDF-Editor\\MML Formulae-1.pdf', 'output.pdf', pages_to_print)
