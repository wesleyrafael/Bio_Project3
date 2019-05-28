import tkinter as tk
from tkinter import filedialog

def sortkmer(list):
    for kmer in list:
        kmer.replace('|','1')
    
    list.sort()

    for kmer in list:
        kmer.replace('1','|')


def generatekmer(k,d,sequence):
    kmer = []

    i = 0    
    while True:
        if i+(k*2)+d > len(sequence):
            break
        s = ''

        for j in range(i,i+k):
            s+= sequence[j]
        s += '|'

        for j in range(i+k+d,i+2*k+d):
            s+= sequence[j]

        kmer.append(s)
        i+=1

        sortkmer(kmer)
    return str(kmer)

def saveinfile(content,filename):
    root = tk.Tk()
    root.filename = filedialog.asksaveasfilename(title="Selecionar pasta para salvar arquivo de saida",initialfile=filename,defaultextension=".txt",filetypes=(("Arquivo de Texto","*.txt"),("all files","*.*")))
    
    if root.filename:
        with open(root.filename,"w") as file:
            file.write(content)

def readfile():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Selecionar arquivo fasta",filetypes=(("Arquivo Fasta","*.fasta"),("Todos os arquivos","*.*")))

    content = ''
    k = 0
    d = 0
    
    if str(file_path) and ".fasta" in str(file_path):
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
    return 0,0,''

def main():
    k,d,content = readfile()
    
    if content != '' and k != 0 and d != 0:
        kmer = generatekmer(k,d,content)
        filename = "k"+str(k)+"d"+str(d)+"mer.txt"
        saveinfile(kmer,filename)
        
if __name__ == "__main__":
    main()