import os
import tkinter as tk
from tkinter import filedialog

def escolher_arquivo():
    root = tk.Tk()
    root.withdraw()
    initial_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = filedialog.askopenfilename(initialdir=initial_dir, filetypes=[("PDF files", "*.pdf")])
  
    return file_path
