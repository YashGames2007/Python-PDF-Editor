import tkinter as tk

def get_line_number(text_widget):
    try:
        selected_text = text_widget.selection_get()
        print("Selected text:", selected_text)
    except Exception as e:
        pass
    return text_widget.index('insert linestart').split('.')[0]

# root = tk.Tk()
root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()

def on_touch(event):
    # Action to perform when the screen is touched
    # print("Screen touched!")
    get_line_number(text_widget)

root.geometry("800x600")
root.bind("<Button-1>", on_touch)

root.mainloop()
