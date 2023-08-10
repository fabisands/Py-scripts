# Compare and tell the percentage of coincidence of the first 810 nucleotides from 2 species of bacteria: Bacteroides fragilis & Bacteroides melaninogenicus
# FASTA sequencies taken from NCBI

from Bio import SeqIO

# Methods for reading FASTA files:
    # variable.read() --> puts the file data into one string variable
    # readline() --> one line + incremental reading of the file
    # readlines() --> returns the lines a list of strings
# Method to use: variable.read()

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

# find and print the shortest one

if C_perfingens_size <= C_septicum_size:
    short_one = C_perfingens_size
else:
    short_one = C_septicum_size

print("Se tomarán los primeros", short_one, "nucleótidos de cada cadena ya que esa es la cantidad a comparar del genoma más corto")

# Do the counting

count = 0
for i in range(C_perfingens_size):
    if Clostridium_perfringens[i] == Clostridium_septicum[i]:
        count += 1

# find and print the percentage of similarity

result = round(((count/short_one)*100), 2)

print("El porcentaje de similitud de los genomas de las especies Clostridium perfringens y Clostridium septicum es", str(result) + "%")

