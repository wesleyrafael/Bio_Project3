import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(title = "Selecionar arquivo kdMer",filetypes = (("Arquivos de Texto","*.txt"),("Todos os arquivos","*.*")))

content = ''
with open(file_path,"r") as file:
    content = file.readline().strip()


kdmers = content.replace(' ','').replace('\'','').replace('[','').replace(']','').split(',')
for kdmer in kdmers:
    print(kdmer)
