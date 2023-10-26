import fitz
import pyperclip
from PIL import Image
from pdfviewer_helper_functions import show_toast

class PDFImageEditor:
    def __init__(self, root) -> None:
        self.app = root
        # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def extract_text(self, path, page_no, password):
        # text = pytesseract.image_to_string(image)
        pdf = fitz.open(path)
        if password:
            pdf.authenticate(password)
        page = pdf[page_no]
        text = page.get_text()
        pyperclip.copy(text)
        show_toast("!!!Text Copied to Clipboard!!!")

    def extract_page(self, path, page_no, password):
        pdf = fitz.open(path)
        if password:
            pdf.authenticate(password)
        # Load the page you want
        page = pdf.load_page(page_no)

        # Render the page to a pixmap (an image)
        pix = page.get_pixmap()

        # Convert the pixmap to a PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.show()