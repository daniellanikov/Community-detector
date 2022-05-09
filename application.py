import tkinter as tk
from tkinter import filedialog, ttk
from community_detector_api import *


class Application:

    def __init__(self):
        self.window = tk.Tk()
        self.fileName = tk.StringVar()
        self.back = tk.Frame(master=self.window, width=750, height=500, bg='gray')
        self.textbox = tk.Text(master=self.back, width=75, height=2)
        self.textbox.place(x=100, y=10)
        self.delimiter = tk.ttk.Combobox(master=self.back)
        self.delimiter['values'] = ('space', 'semicolon')
        self.delimiter.place(x=200, y=50)

    def openfiledialog(self):
        self.fileName.set(filedialog.askopenfilename())
        self.textbox.insert('end', self.fileName.get())

    def initialize_buttons(self):
        tk.Button(master=self.back, text="open file", command=lambda: self.openfiledialog()).place(x=10, y=10)
        tk.Button(master=self.back, text="Newman-Girvan", command=lambda: coloring_newman(self.fileName.get(), self.delimiter.get())).place(x=10, y=55)
        tk.Button(master=self.back, text="Markov", command=lambda: coloring_markov(self.fileName.get(), self.delimiter.get())).place(x=10, y=80)
        tk.Button(master=self.back, text="Coloring cliques", command=lambda: coloring_cliques(self.fileName.get(), self.delimiter.get())).place(x=10, y=105)
        tk.Button(master=self.back, text="Maximum Modularity", command=lambda: coloring_greedy_modularity(self.fileName.get(), self.delimiter.get())).place(x=10, y=130)
        tk.Button(master=self.back, text="Induced H-avoiding coloring", command=lambda: coloring_h_avoiding_clusters(self.fileName.get(), self.delimiter.get())).place(x=10, y=155)
        tk.Button(master=self.back, text="Modularity", command=lambda: utils_modularity(self.fileName.get(), self.delimiter.get())).place(x=10, y=180)
        tk.Button(master=self.back, text="Condensate", command=lambda: utils_condense(self.fileName.get(), self.delimiter.get())).place(x=10, y=205)


    def close_app(self):
        self.back.pack_propagate(0)
        self.back.pack(fill=tk.BOTH, expand=1)
        self.window.mainloop()

