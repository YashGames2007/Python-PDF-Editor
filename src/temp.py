import tkinter as tk
from tkinter import ttk

# Create instance
win = tk.Tk()   

# Add a title       
win.title("Python GUI with Notebook")

# Create Tab Control
tabControl = ttk.Notebook(win)         

tab1 = ttk.Frame(tabControl)            
tabControl.add(tab1, text='Tab 1')    

tab2 = ttk.Frame(tabControl)            
tabControl.add(tab2, text='Tab 2')   

tabControl.pack(expand=1, fill="both")  

# Create a frame and text box for each tab
frame1 = ttk.Frame(tab1)
frame1.grid(column=0, row=0)
text1 = tk.Text(frame1, width=20, height=5)
text1.pack()

frame2 = ttk.Frame(tab2)
frame2.grid(column=0, row=0)
text2 = tk.Text(frame2, width=20, height=5)
text2.pack()

win.mainloop()
