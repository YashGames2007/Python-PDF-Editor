import fitz
import pyperclip
from PIL import Image
from pdfviewer_helper_functions import show_toast

class PDFImageEditor:
    def __init__(self, root) -> None:
        self.app = root
        # pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    def extract_text(self, path, page_no):
        # text = pytesseract.image_to_string(image)
        pdf = fitz.open(path)
        page = pdf[page_no]
        text = page.get_text()
        pyperclip.copy(text)
        show_toast("!!!Text Copied to Clipboard!!!")

    def extract_page(self, path, page_no):
        pdf = fitz.open(path)
        # Load the page you want
        page = pdf.loadPage(0)  # 0 is the page number

        # Render the page to a pixmap (an image)
        pix = page.getPixmap()

        # Convert the pixmap to a PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        img.show()