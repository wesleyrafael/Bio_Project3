import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = "Selecionar arquivo kdMer",filetypes = (("Arquivos de Texto","*.txt"),("Todos os arquivos","*.*")))

