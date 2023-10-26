try:
    from tkinter import *
    from tkinter import simpledialog
    import tkinter as tk
    from customtkinter import *
    import fitz
    from tkinter import ttk
    from tkinter.ttk import Progressbar
    from threading import Thread
    import math
    import time
except Exception as e:
    print(f"This error occured while importing neccesary modules or library {e}")

class ShowPdf():
    img_object_li = []
    image_object_li = []
    max_width = 0
    pdf_objects = {}

    def pdf_view(self, master, frame=None, width=1200, height=600, pdf_location="", bar=True, load="after"):
        self.master = master
        frame = master if frame is None else frame
        new_frame = ttk.Frame(frame,width= width,height= height) # bd_color="transparent"
        new_frame.grid(column=0, row=0)

        scroll_y = CTkScrollbar(new_frame,orientation="vertical")
        scroll_x = CTkScrollbar(new_frame,orientation="horizontal")

        scroll_x.pack(fill="x",side="bottom")
        scroll_y.pack(fill="y",side="right")

        percentage_view = 0
        percentage_load = StringVar()

        if bar==True and load=="after":
            self.display_msg = CTkLabel(master=new_frame, textvariable=percentage_load)
            self.display_msg.pack(pady=10)

            loading = Progressbar(new_frame,orient= HORIZONTAL,length=100,mode='determinate')
            loading.pack(side = TOP,fill=X)

        page_text = Text(new_frame,yscrollcommand=scroll_y.set,xscrollcommand= scroll_x.set,width= width,height= height, bg=master.cget("bg"))
        page_text.pack()

        scroll_x.configure(command=page_text.xview)
        scroll_y.configure(command=page_text.yview)

        def add_img():
            precentage_dicide = 0
            open_pdf = fitz.open(pdf_location)
            password = None
            while open_pdf.isEncrypted:
                messagebox = CTkInputDialog(text="Enter Password to open PDF", title="Decrypt PDF")
                password = messagebox.get_input()
                if password is None:
                    return None
                open_pdf.authenticate(password)
                if not open_pdf.isEncrypted:
                    break
                tk.messagebox.showerror("Error", str("!WRONG PASSWORD!"))
            
            self.img_object_li = []
            self.image_object_li = []
            self.max_width = master.winfo_width()
            for page in open_pdf:
                pix = page.get_pixmap()
                pix1 = fitz.pixmap(pix,0) if pix.alpha else pix
                img = pix1.tobytes("ppm")
                timg = PhotoImage(data = img)
                original_width = timg.width()
                self.max_width = max(self.max_width, original_width)
                self.img_object_li.append(timg)
                self.image_object_li.append(img)

                if bar==True and load=="after":
                    precentage_dicide = precentage_dicide + 1
                    percentage_view = (float(precentage_dicide)/float(len(open_pdf))*float(100))
                    loading['value'] = percentage_view
                    percentage_load.set(f"Please wait!, your pdf is loading {int(math.floor(percentage_view))}%")
            if bar==True and load=="after":
                loading.pack_forget()
                self.display_msg.pack_forget()

            _index = 0
            for page in self.img_object_li:
                page_text.image_create(END,image=page, name=f"{_index}")
                page_text.insert(END,"\n\n")
                _index += 1
            page_text.configure(state="disabled")
            self.pdf_objects[page_text] = (self.img_object_li[:], pdf_location, password)
            master.geometry(f"{self.max_width}x{master.winfo_height()}")

        def start_pack():
            t1 = Thread(target=add_img)
            t1.start()

        if load=="after":
            new_frame.after(250,start_pack)
        else:
            start_pack()

        return new_frame, page_text



def main():
    root = CTk()
    root.geometry("700x780")
    d = ShowPdf().pdf_view(root,width=50,height=200)
    d.pack()
    root.mainloop()

if __name__ == '__main__':
    main()
