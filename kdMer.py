import tkinter as tk
from tkinter import filedialog

def generatekdmer(sequence):
    sequence = ''

    return sequence

def saveinfile(content):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title = "Selecionar pasta para salvar arquivo de saida",filetypes = (("Arquivo de Texto","*.txt"),("all files","*.*")))
    print (root.filename)

    if ".txt" not in root.filename:
        root.filename += '.txt'

    with open(root.filename,"w") as file:
        file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title = "Selecionar arquivo fasta",filetypes = (("Arquivo Fasta","*.fasta"),("Todos os arquivos","*.*")))

    content = ''
    if ".fasta" in file_path:
        with open(file_path,"r") as file:
            while True:
                content += file.readline().strip()
                if content == '':
                    break
                else:
                    content += '\n'
    
    return content

def main():
    content = readfile()
    if content != '':
        print(content)
    

if __name__ == "__main__":
    main()