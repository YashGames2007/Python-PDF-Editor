# from PIL import Image
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
# image = Image.open("D:\\Programming files\\GitHub\\Repositories\\Python-PDF-Editor\\rs\\pyimage13.png")
# text = pytesseract.image_to_string(image)
# print(text)

import customtkinter as ctk
import time

def show_toast(message):
    toast = ctk.CTkToplevel()
    toast.configure(corner_radius=4)
    toast.overrideredirect(1)

    # Position the toast window
    screen_width = toast.winfo_screenwidth()
    screen_height = toast.winfo_screenheight()
    x_coordinate = int((screen_width/2) - (200/2))
    y_coordinate = int((screen_height) - (100))
    toast.geometry("175x30+{}+{}".format(x_coordinate, y_coordinate))

    # Set the background color and message
    ctk.CTkLabel(toast, text=message, corner_radius=10).pack()

    # Show the toast for 1 second then destroy
    toast.after(2500, toast.destroy)

root = ctk.CTk()
button = ctk.CTkButton(root, text="Copy Text", command=lambda: show_toast("Text Copied to Clipboard."))
button.pack()

root.mainloop()

