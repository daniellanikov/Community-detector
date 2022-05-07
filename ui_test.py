import tkinter as tk
from tkinter import filedialog

window = tk.Tk()


def openfiledialog():
    filename = filedialog.askopenfilename()
    text = tk.Label(window, text=filename)


def u_interface():
    button = tk.Button(window, text="open file", command=openfiledialog)
    button.pack()
    #tk.Button(text="open file", command=filedialog.askopenfilename())
    window.mainloop()

