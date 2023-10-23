import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def create_new_tab():
    new_tab = ttk.Frame(tab_control)
    tab_control.add(new_tab)

    # Create a custom tab with a label and a button
    tab_label = tk.Frame(tab_control.tab(new_tab, 'underline'), background='white')
    label = tk.Label(tab_label, text='New Tab', background='white')
    close_button = tk.Button(tab_label, text='x', command=lambda: close_tab(new_tab), background='white', padx=2, pady=2)
    
    label.pack(side='left')
    close_button.pack(side='right')
    tab_control.tab(new_tab, underline=tab_label)

def close_tab(tab):
    tab_control.forget(tab)

def open_file():
    filedialog.askopenfilename()
    create_new_tab()
    tab_control.pack(expand=1, fill='both')  # pack the tab control here

root = tk.Tk()
root.title("Menu Bar and Tab View")

# Create a menu bar
menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
menu_bar.add_cascade(label="File", menu=file_menu)

# Add Open option to File menu
file_menu.add_command(label="Open", command=open_file)

# Create a Tab Control
tab_control = ttk.Notebook(root)

root.mainloop()
