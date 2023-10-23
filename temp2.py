import tkinter as tk

def increase_size():
    current_font_size = label.cget("font").split(" ")[-1]
    new_font_size = int(current_font_size) + 2  # Increase font size by 2 points
    label.config(font=("Arial", new_font_size))

def decrease_size():
    current_font_size = label.cget("font").split(" ")[-1]
    new_font_size = int(current_font_size) - 2  # Decrease font size by 2 points
    label.config(font=("Arial", new_font_size))

root = tk.Tk()
root.title("Change Text Image Size")

frame = tk.Frame(root)
frame.pack()

label = tk.Label(frame, text="Resize me")
label.pack()

increase_button = tk.Button(frame, text="Increase Size", command=increase_size)
increase_button.pack()

decrease_button = tk.Button(frame, text="Decrease Size", command=decrease_size)
decrease_button.pack()

root.mainloop()