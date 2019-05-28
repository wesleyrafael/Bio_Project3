import tkinter as tk
from tkinter import filedialog

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
    
    if str(file_path) and "mer.txt" in str(file_path):
        k,d = file_path.split('/')[-1].replace('mer.txt','').replace('k','').split('d')
        with open(file_path,"r") as file:
            content = file.readline().strip()
        return int(k),int(d),content
    return 0,0,''

def main():
    k,d,content = readfile()
    if content != '':
        kmers = content.replace(' ','').replace('\'','').replace('[','').replace(']','').split(',')
        # for kmer in kmers:
        #     print(kmer)
        
        sequence = assemble(k,d,kmers)
        filename="k"+str(k)+"d"+str(d)+"seq.fasta"
        saveinfile(sequence,filename)

if __name__ == "__main__":
    main()