import tkinter as tk
from tkinter import filedialog
import re

class Composition:
    def __init__(self, kmer, prefix, suffix):
        self.kmer = kmer
        self.prefix = prefix
        self.suffix = suffix

def create_suffix_prefix(kmer, k):
    prefix = []
    suffix = []

    for arrange in kmer:
        prefix.append(arrange[:k-1])

    for arrange in kmer:
        suffix.append(arrange[-(k-1):])

    return [prefix, suffix]

def find_initial_node(nodes):
    initial_node = -1

    for n in nodes:
        found = False

        for m in nodes:
            if (nodes.index(m) != nodes.index(n)):
                if (m.suffix == n.prefix):
                    found = True

        if(found == False):
            initial_node = n
            nodes.pop(nodes.index(n))
            break

    return [initial_node, nodes]

def find_path(initial_node, remaining_nodes):
    current_node = initial_node
    path = [initial_node]

    while(len(remaining_nodes) > 0):
        for n in remaining_nodes:
            if(current_node.suffix == n.prefix):
                current_node = n
                path.append(current_node)
                remaining_nodes.pop(remaining_nodes.index(n))

    return path

def assemble(kmers, k):
    sequence = ''

    nodes = []
    for kmer in kmers:
        prefix_suffix = create_suffix_prefix(kmer.split("|"), k)
        nodes.append(Composition(kmer.split("|"), prefix_suffix[0], prefix_suffix[1]))

    temp = find_initial_node(nodes)
    initial_node = temp[0]
    remaining_nodes = temp[1]

    path = find_path(initial_node, remaining_nodes)

    first_half = [p.kmer[0] for p in path]
    second_half = [p.kmer[1] for p in path]

    i=0
    last_suffix = ''
    for km in first_half:
        if i == 0:
            sequence += km
        else:
            sequence += km[-1]
            last_suffix = km
        i+=1
    
    remaining_aminoacids = False
    for km in second_half:
        if remaining_aminoacids:
            sequence += km[-1]
        elif km != last_suffix:
            continue
        else:
            remaining_aminoacids = True

    return sequence

def saveinfile(content, filename):
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

        header = '>k='+str(k)+'d='+str(d)+'\n'
        sequence = assemble(kmers, k)

        filename="k"+str(k)+"d"+str(d)+"seq.fasta"
        saveinfile(header + sequence,filename)

if __name__ == "__main__":
    main()
