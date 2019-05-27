import tkinter as tk
from tkinter import filedialog


def assemble(kdmers):
    sequence = ''

    return sequence

def readFile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title = "Selecionar arquivo kdMer",filetypes = (("Arquivos de Texto","*.txt"),("Todos os arquivos","*.*")))

    content = ''
    with open(file_path,"r") as file:
        content = file.readline().strip()
    
    return content

def main():
    content = readFile()
    kdmers = content.replace(' ','').replace('\'','').replace('[','').replace(']','').split(',')
    for kdmer in kdmers:
        print(kdmer)

    sequence = assemble(kdmers)
    # print(sequence)

if __name__ == "__main__":
    main();