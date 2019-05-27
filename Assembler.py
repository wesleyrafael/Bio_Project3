import tkinter as tk
from tkinter import filedialog

def assemble(k,d,kdmers):
    sequence = ''

    return sequence

def saveinfile(content,filename):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title="Selecionar pasta para salvar arquivo de saida",initialfile=filename,defaultextension=".fasta",filetypes=(("Arquivo Fasta","*.fasta"),("all files","*.*")))

    with open(root.filename,"w") as file:
        file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecionar arquivo kdMer",filetypes=(("Arquivo de Texto","*.txt"),("Todos os arquivos","*.*")))

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
        filename="k"+str(k)+"d"+str(d)+"mer.fasta"
        saveinfile(sequence,filename)

if __name__ == "__main__":
    main()