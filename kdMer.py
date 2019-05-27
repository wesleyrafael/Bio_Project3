import tkinter as tk
from tkinter import filedialog

def generatekdmer(k,d,sequence):
    kmer = ''

    return kmer

def saveinfile(content,filename):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title="Selecionar pasta para salvar arquivo de saida",initialfile=filename,defaultextension=".txt",filetypes=(("Arquivo de Texto","*.txt"),("all files","*.*")))
    
    with open(root.filename,"w") as file:
        file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecionar arquivo fasta",filetypes =(("Arquivo Fasta","*.fasta"),("Todos os arquivos","*.*")))

    content = ''
    k = ''
    d = ''
    
    if ".fasta" in file_path:
        with open(file_path,"r") as file:
            while True:
                line = file.readline().strip()
                if line == '':
                    break
                elif '>' in line:
                    k,d = line.replace('>','').replace('=','').replace('k','').split('d')
                else:
                    content += line + '\n'
            
    return int(k),int(d),content.strip()

def main():
    k,d,content = readfile()
    if content != '':
        # print(content)
        # print(k,d)
        kmer = generatekdmer(k,d,content)
        filename = "k"+str(k)+"d"+str(d)+"mer.txt"
        saveinfile(kmer,filename)
        
if __name__ == "__main__":
    main()