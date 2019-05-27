import tkinter as tk
from tkinter import filedialog

def assemble(k,d,kdmers):
    sequence = ''

    return sequence

def saveinfile(content):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title = "Selecionar pasta para salvar arquivo de saida",filetypes = (("Arquivo Fasta","*.fasta"),("all files","*.*")))
    print (root.filename)

    if ".fasta" not in root.filename:
        root.filename += '.fasta'

    with open(root.filename,"w") as file:
        file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title = "Selecionar arquivo kdMer",filetypes = (("Arquivo de Texto","*.txt"),("Todos os arquivos","*.*")))

    k,d = file_path.split('/')[-1].replace('mer.txt','').replace('k','').split('d')
        
    content = ''
    if ".txt" in file_path:
        with open(file_path,"r") as file:
            content = file.readline().strip()
    
    return int(k),int(d),content

def main():
    k,d,content = readfile()
    if content != '':
        kdmers = content.replace(' ','').replace('\'','').replace('[','').replace(']','').split(',')
        for kdmer in kdmers:
            print(kdmer)
        
        sequence = assemble(k,d,kdmers)
        # sequence = 'teste'
        saveinfile(sequence)

if __name__ == "__main__":
    main()