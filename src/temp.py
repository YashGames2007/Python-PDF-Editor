import fitz  # PyMuPDF
from PIL import Image

# Open the PDF file
pdf_document = "D:\\Programming files\\GitHub\\Repositories\\Python-PDF-Editor\\storytelling-with-data-cole-nussbaumer-knaflic.pdf"
pdf = fitz.open(pdf_document)

# Define the page number you want to extract (e.g., page 1)
page_number = 0  # Note: Pages are 0-based.

# Get the specific page
page = pdf.load_page(page_number)

# Convert the page to a Pillow image
image = page.get_pixmap()
pillow_image = Image.frombytes("RGB", [image.width, image.height], image.samples)
pillow_image.show()
# Save or process the extracted image as needed
# pillow_image.save("extracted_page.png")

# Close the PDF document
pdf.close()