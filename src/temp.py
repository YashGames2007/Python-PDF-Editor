import tkinter as tk
import tkinter.ttk as ttk
from ctknotebook import CustomNotebook

class Example(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.canvas = tk.Canvas(self, borderwidth=0)
        self.frame = tk.Frame(self.canvas)

        self.vsb = tk.Scrollbar(self, command=self.canvas.xview)
        self.canvas.configure(xscrollcommand=self.vsb.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.frame.pack(side="top", fill="both", expand=True)
        # self.vsb.grid(row=0, column=0, sticky="ew")

        self.canvas.create_window((3,2), window=self.frame, anchor="center", tags="self.frame")

        self.frame.bind("<Configure>", self.frame_configure)
        self.populate()

    def populate(self):
        tabs = CustomNotebook(self.frame, width=100, height=100)
        tabs.bind("<MouseWheel>", self.on_mousewheel)
        for tab in range(5):
            tab_frame = ttk.Frame(tabs)
            tabs.add(tab_frame, text=" Tab {}  ".format(tab))
            scroller = ttk.Scrollbar(tab_frame, orient="vertical")
            scroller.pack(fill="y", side="right")
            # tab_frame.pack(fill="both", side="top", expand=True)

        tabs.pack(fill="both", side="top", expand=True)

    def frame_configure(self, event):
        x1, y1, _, y2 = self.canvas.bbox("all")
        max_width = max(self.frame.winfo_width(), self.canvas.winfo_width())
        self.canvas.configure(scrollregion=(x1, y1, max_width, y2))

    def on_mousewheel(self, event):
        self.canvas.xview_scroll(int(-1*(event.delta/120)), "units")

if __name__ == "__main__":
    app = Example()
    app.mainloop()

# import tkinter as tk

# def on_mousewheel(event):
#     canvas.xview_scroll(int(-1*(event.delta/120)), "units")

# root = tk.Tk()
# canvas = tk.Canvas(root)
# scrollbar = tk.Scrollbar(root, orient="horizontal", command=canvas.xview)
# canvas.configure(xscrollcommand=scrollbar.set, scrollregion=(0, 0, 100, 0))

# # Add some items to the canvas
# for i in range(100):
#     canvas.create_text(50 + i*10, 10, text=f"Item {i+1}", anchor="w")

# canvas.pack(side="left", fill="both", expand=True)
# scrollbar.pack(side="bottom", fill="x")

# # Bind the mouse wheel event to the on_mousewheel function
# root.bind("<MouseWheel>", on_mousewheel)

# root.mainloop()
