import os
import tkinter as tk
from tkinter import filedialog

def escolher_diretorio():
    # Cria uma instância do Tk
    root = tk.Tk()
    # Esconde a janela principal do Tk
    root.withdraw()
    # Define o diretório inicial como o diretório onde o script está localizado
    initial_dir = os.path.dirname(os.path.realpath(__file__))
    # Abre a caixa de diálogo para escolher um diretório
    directory_path = filedialog.askdirectory(initialdir=initial_dir)
    return directory_path
