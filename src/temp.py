import tkinter as tk

def get_selected_text():
    selected_text = text_widget.selection_get()
    print("Selected text:", selected_text)

root = tk.Tk()
text_widget = tk.Text(root)
text_widget.pack()
text_widget.insert('1.0', "This is some sample text.")
button = tk.Button(root, text="Get Selected Text", command=get_selected_text)
button.pack()

root.mainloop()