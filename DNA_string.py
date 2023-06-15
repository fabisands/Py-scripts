print("Generador de cadenas de ADN")
print("Escriba una serie de letras de bases nitrogenadas (CGTA): ")
S53 = input().upper()

for e in S53:
    if e == "C":
        S35_1 = S53.replace("C", "1")
for e in S35_1:
    if e == "G":
        S35_2 = S35_1.replace("G", "2")
for e in S35_2:
    if e == "T":
        S35_3 = S35_2.replace("T", "3")
for e in S35_3:
    if e == "A":
        S35_4 = S35_3.replace("A", "4")

for e in S35_4:
    if e == "1":
        S35_5 = S35_4.replace("1", "G")
for e in S35_5:
    if e == "2":
        S35_6 = S35_5.replace("2", "C")
for e in S35_6:
    if e == "3":
        S35_7 = S35_6.replace("3", "A")
for e in S35_7:
    if e == "4":
        S35 = S35_7.replace("4", "T")

print()

print("La doble hélice de ADN es:")
print("5'- " + S53 + " -3'")
print("3'- " + S35 + " -5'")

if "C" in S53:
    count_C1 = S53.count("C")
if "G" in S53:
    count_G1 = S53.count("G")
if "T" in S53:
    count_T1 = S53.count("T")
if "A" in S53:
    count_A1 = S53.count("A")

print()

print("En la cadena dada por el usuario hay un total de:")
print(count_C1, "citocinas")
print(count_G1, "guaninas")
print(count_T1, "timinas")
print(count_A1, "adeninas")

if "C" in S35:
    count_C2 = S35.count("C")
if "G" in S35:
    count_G2 = S35.count("G")
if "T" in S35:
    count_T2 = S35.count("T")
if "A" in S35:
    count_A2 = S35.count("A")

print()

print("En la cadena complementaria hay un total de:")
print(count_C2, "citocinas")
print(count_G2, "guaninas")
print(count_T2, "timinas")
print(count_A2, "adeninas")

count_C = count_C1 + count_C2
count_G = count_G1 + count_G2
count_T = count_T1 + count_T2
count_A = count_A1 + count_A2

print()

print("En la doble hélice de ADN hay un total de:")
print(count_C, "citocinas")
print(count_G, "guaninas")
print(count_T, "timinas")
print(count_A, "adeninas")
