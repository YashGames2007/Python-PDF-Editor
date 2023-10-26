import pytesseract
import pyperclip
from pdfviewer_helper_functions import show_toast


class PDFImageEditor:
    def __init__(self, root) -> None:
        self.app = root
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

    
    def extract_text(self, image):
        text = pytesseract.image_to_string(image)
        pyperclip.copy(text)
        show_toast("!!!Text Copied to Clipboard!!!")

    def extract_page(self, image):
        image.show()