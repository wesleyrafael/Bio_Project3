import tkinter as tk
from tkinter import filedialog
import re

def assemble(k,d,kmers):
    sequence = ''

    return sequence

def saveinfile(content,filename):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title="Selecionar pasta para salvar arquivo de saida",initialfile=filename,defaultextension=".fasta",filetypes=(("Arquivo Fasta","*.fasta"),("all files","*.*")))

    if root.filename:
        with open(root.filename,"w") as file:
            file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecionar arquivo kdMer",filetypes=(("Arquivo de Texto","*.txt"),("Todos os arquivos","*.*")))
    
    content = ''
    k = 0
    d = 0        
    
    if str(file_path) and re.search(r'k\d+d\d+mer.txt',file_path):
        k,d = file_path.split('/')[-1].replace('mer.txt','').replace('k','').split('d')
        with open(file_path,"r") as file:
            content = file.readline().strip()
        return int(k),int(d),content
    return 0,0,''

def main():
    k,d,content = readfile()
    if content != '' and k != 0 and d != 0:
        kmers = content.replace(' ','').replace('\'','').replace('[','').replace(']','').split(',')
        # for kmer in kmers:
        #     print(kmer)
        header = '>k='+str(k)+'d='+str(d)+'\n'
        sequence = assemble(k,d,kmers)
        filename="k"+str(k)+"d"+str(d)+"seq.fasta"
        saveinfile(header + sequence,filename)

if __name__ == "__main__":
    main()