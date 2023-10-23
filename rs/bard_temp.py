from tkinter import * 
from tkinter import filedialog as fd 
from tkinter import messagebox as mb
from tkinter import ttk 
from PIL import Image, ImageTk 
from PyPDF2 import PdfReader 
import os

root = Tk()
root.title("PDF Viewer")
# root.iconbitmap(“icon.ico”)

class App: 
    def __init__(self, master): 
        # Initializing the master window and some variables 
        self.master = master 
        self.pdf_file = None 
        self.pdf_reader = None 
        self.num_pages = 0 
        self.current_page = 0 
        self.images = [] 
        self.image_labels = []
        # Creating the menu bar and adding commands
        self.menu_bar = Menu(self.master)
        self.file_menu = Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open", command=self.open_pdf)
        self.file_menu.add_command(label="Save", command=self.save_pdf)
        self.file_menu.add_command(label="Close", command=self.close_pdf)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.destroy)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.master.config(menu=self.menu_bar)

        # Creating the top frame for displaying the PDF
        self.top_frame = Frame(self.master)
        self.top_frame.pack(fill=BOTH, expand=1)

        # Creating the canvas and the scrollbars for the top frame
        self.canvas = Canvas(self.top_frame, bg="grey")
        self.canvas.pack(side=LEFT, fill=BOTH, expand=1)
        self.v_scrollbar = Scrollbar(self.top_frame, orient=VERTICAL, command=self.canvas.yview)
        self.v_scrollbar.pack(side=RIGHT, fill=Y)
        self.h_scrollbar = Scrollbar(self.top_frame, orient=HORIZONTAL, command=self.canvas.xview)
        self.h_scrollbar.pack(side=BOTTOM, fill=X)
        self.canvas.config(xscrollcommand=self.h_scrollbar.set, yscrollcommand=self.v_scrollbar.set)

        # Creating the bottom frame for navigation
        self.bottom_frame = Frame(self.master)
        self.bottom_frame.pack(fill=X)

        # Creating the buttons and the entry for the bottom frame
        self.prev_button = ttk.Button(self.bottom_frame, text="<<", command=self.prev_page)
        self.prev_button.pack(side=LEFT)
        self.next_button = ttk.Button(self.bottom_frame, text=">>", command=self.next_page)
        self.next_button.pack(side=RIGHT)
        self.page_label = Label(self.bottom_frame, text="Page 0 of 0")
        self.page_label.pack(side=LEFT, padx=10)
        self.page_entry = Entry(self.bottom_frame, width=5)
        self.page_entry.pack(side=LEFT)
        self.go_button = ttk.Button(self.bottom_frame, text="Go", command=self.go_page)
        self.go_button.pack(side=LEFT)

    # Defining the function to open a PDF file
    def open_pdf(self):
        # Asking the user to select a PDF file
        pdf_file = fd.askopenfilename(title="Select a PDF file", filetypes=[("PDF files", "*.pdf")])

        # Checking if a file is selected
        if pdf_file:
            # Closing any previous PDF file
            if self.pdf_file:
                self.close_pdf()

            # Opening the PDF file and creating a reader object
            # try:
            self.pdf_file = open(pdf_file, "rb")
            self.pdf_reader = PdfReader(self.pdf_file)

            # Getting the number of pages and setting the current page to 1
            self.num_pages = len(self.pdf_reader.pages)
            print(f"Number of pages: {self.num_pages}")
            print(f"Current page: {self.current_page}")
            print(f"PDF file: {pdf_file}")
            print(f"PDF reader: {self.pdf_reader}")
            print(f"Images: {self.images}")
            print(f"Image labels: {self.image_labels}")
            print("-"*50)

            if not (self.current_page == 1):
                print("Current page is not 1")
                print(f"Current page: {self.current_page}")
                print("-"*50)

                if (self.current_page == 0):
                    print("Current page is 0")
                    print(f"Current page: {self.current_page}")
                    print("-"*50)

                else:
                    print("Current page is not 0")
                    print(f"Current page: {self.current_page}")
                    print("-"*50)

                if (self.current_page > 0):
                    print("Current page is greater than 0")
                    print(f"Current page: {self.current_page}")
                    print("-"*50)

                else:
                    print("Current page is not greater than 0")
                    print(f"Current page: {self.current_page}")
                    print("-"*50)

            self.current_page = 1

            # Updating the page label and the entry
            self.page_label.config(text=f"Page {self.current_page} of {self.num_pages}")
            self.page_entry.delete(0, END)
            self.page_entry.insert(0, str(self.current_page))

            # Converting each page to an image and storing it in a list
            self.images = []
            for i in range(self.num_pages):
                page = self.pdf_reader.pages[i]
                zoom = 1.5 # zoom factor
                width = int(float(page.mediabox[2]) * zoom)
                height = int(float(page.mediabox[3]) * zoom)
                # image = Image.open(page.images)
                self.images.append(page)

            # Creating a label for each image and adding it to the canvas
            self.image_labels = []
            for i in range(self.num_pages):
                x = 20 # x position of the image
                y = (height + 20) * i + 20 # y position of the image
                label = Label(self.canvas, image=self.images[i])
                label.image = self.images[i] # keeping a reference to avoid garbage collection
                self.canvas.create_window(x, y, anchor=NW, window=label)
                self.image_labels.append(label)

            # Configuring the canvas scrollregion
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

            # except Exception as e:
            #     # Showing an error message if the file is not valid
            #     print(e)
            #     mb.showerror(title="Error", message="The file you selected is not a valid PDF file.")

    # Defining the function to save and rename a PDF file
    def save_pdf(self):
        # Checking if a PDF file is opened
        if self.pdf_file:
            # Asking the user to select a folder and enter a file name
            folder = fd.askdirectory(title="Select a folder")
            file_name = fd.askstring(title="Enter a file name", prompt="Enter a file name without extension:")

            # Checking if a folder and a file name are given
            if folder and file_name:
                # Creating the full path of the new file
                new_file = os.path.join(folder, file_name + ".pdf")

                # Copying the content of the old file to the new file
                try:
                    with open(new_file, "wb") as f:
                        f.write(self.pdf_file.read())
                        fd.showinfo(title="Success", message=f"The file has been saved as {new_file}")
                except Exception as e:
                    # Showing an error message if the file cannot be saved
                    print(e)
                    fd.showerror(title="Error", message="The file cannot be saved. Please try again.")

    # Defining the function to close a PDF file
    def close_pdf(self):
        # Checking if a PDF file is opened
        if self.pdf_file:
            # Closing the file object and resetting the variables
            self.pdf_file.close()
            self.pdf_file = None
            self.pdf_reader = None
            self.num_pages = 0
            self.current_page = 0

            # Updating the page label and the entry
            self.page_label.config(text="Page 0 of 0")
            self.page_entry.delete(0, END)

            # Deleting all the images and labels from the canvas
            for label in self.image_labels:
                label.destroy()
            self.images = []
            self.image_labels = []

            # Configuring the canvas scrollregion
            self.canvas.config(scrollregion=self.canvas.bbox("all"))

    # Defining the function to go to the next page
    def next_page(self):
        # Checking if the current page is not the last page
        if self.current_page < self.num_pages:
            # Incrementing the current page by 1
            self.current_page += 1

            # Updating the page label and the entry
            self.page_label.config(text=f"Page {self.current_page} of {self.num_pages}")
            self.page_entry.delete(0, END)
            self.page_entry.insert(0, str(self.current_page))

    # Defining the function to go to the previous page
    def prev_page(self):
        # Checking if the current page is not the first page
        if self.current_page > 1:
            # Decrementing the current page by 1
            self.current_page -= 1

            # Updating the page label and the entry
            self.page_label.config(text=f"Page {self.current_page} of {self.num_pages}")
            self.page_entry.delete(0, END)
            self.page_entry.insert(0, str(self.current_page))

    # Defining the function to
    def go_page(self):
        # Getting the page number from the entry
        page = self.page_entry.get()

        # Checking if the page number is valid
        if page.isdigit() and 1 <= int(page) <= self.num_pages:
            # Setting the current page to the entered page
            self.current_page = int(page)

            # Updating the page label and the entry
            self.page_label.config(text=f"Page {self.current_page} of {self.num_pages}")
            self.page_entry.delete(0, END)
            self.page_entry.insert(0, str(self.current_page))

app = App(root)
root.mainloop()