# Compare and tell the percentage of coincidence of the first 810 nucleotides from 2 species of bacteria: Bacteroides fragilis & Bacteroides melaninogenicus
# FASTA sequencies taken from NCBI

# import modules
from Bio import SeqIO

# Methods:
# variable.read() --> puts your the file data into one string variable
# readline() --> one line + incremental reading of your file
# readlines() --> returns the lines a list of strings

# read the FASTA files

x = open(r'C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\VSCode files\Py-scripts\Genomes\Clostridium_perfringens.fna', 'r')
a = x.read()
x.close()
b = a[66:]
Clostridium_perfringens = b.replace("\n", "")
C_perfingens_size = len(Clostridium_perfringens)
print("La cantidad de nucleótidos del genoma de Clostridium perfringens es", C_perfingens_size)

y = open(r'C:\Users\faren\OneDrive - Universidad de la Amazonia\Documents\VSCode files\Py-scripts\Genomes\Clostridium_septicum.fna', 'r')
c = y.read()
y.close()
d = c[80:]
Clostridium_septicum = d.replace("\n", "")
C_septicum_size = len(Clostridium_septicum)
print("La cantidad de nucleótidos del genoma de Clostridium septicum es", C_septicum_size)

# print(Clostridium_perfringens) --> imprime toda la cadena
# print(Clostridium_perfringens[0:10]) --> imprime los caracteres del índice 0 al índice 9

count = 0
for i in range(len(Clostridium_perfringens)):
    if Clostridium_perfringens[i] == Clostridium_septicum[i]:
        count += 1

result = round(((count/3275499)*100), 2)

print("El porcentaje de similitud de los genomas de las especies Clostridium perfringens y Clostridium septicum es", str(result) + "%")

