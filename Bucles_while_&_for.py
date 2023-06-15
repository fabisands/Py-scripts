# Contar la cantidad de vocales que hay en una oración.
s = "El pato hace quack"
s = s.lower()
i = 0
count = 0
while i < len(s):
    if s[i] == "a" or s[i] == "e" or s[i] == "i" or s[i] == "o" or s[i] == "u":
        count += 1
    i += 1
print("En total hay", count, "vocales")

# Con un bucle while, dados dos números enteros proporcionados por el ususario,  vamos a encontrar el primer número divisible entre 2, 3 y 5 siempre que sea posible,
# que se encuentre dentro del intérvalo formado por los dos números dados por el usuario (ambos extremos también incluidos).
a = int(input("Introduce el extremo izquierdo del intervalo: "))
b = int(input("Introduce el extremo derecho del intervalo: "))
n = a
while n <= b:
    if n % 2 == 0 and n % 3 == 0 and n % 5 == 0:
        print("Dentro del intérvalo,", n, "es divisible entre 2, 3 y 5.")
        break
    n += 1
if n == b + 1:
    print("Dentro del intervalo que has proporcionado no hay números enteros divisibles entre 2, 3 y 5.")

# Realizar una cuenta regresiva
i = 10
print("Preparados para despegue. Empieza la cuenta atrás.")
while i >= 0:
    print(i)
    i -= 1
else:
    print("La cuenta atrás ha finalizado.")

# Vamos a hacer que el usuario introduzca números por teclado e ir sumándolos. Cuando el usuario introduzca 0 saldremos del bucle while.
# Al salid el bucle, con un else mostraremos la suma
n = float(input("Introduce un número: "))
print("Para dar finalización, introduzca el 0 (cero)")
sum = 0
while n != 0:
    sum += n
    n = float(input("Introduce un número: "))
else:
    print("La suma total es", sum)

# Imaginemos las letras del abecedario ordenadas y dispuestas en círculo. Es decir, a la derecha de la A está la B, luego la C,
# y así sucesivamente hasta la Z. A la derecha de la Z, se encuentra de nuevo la letra A.
# Vamos a hacer que el usuario introduzca un valor entero n, que se corresponderá con la rotación que llevará a una determinada
# letra n posiciones a su derecha. Por ejemplo, si la rotación es 4, entonces la A pasará a la E, la B a la F, ..., la Y a la C y la Z a la D.
# Con un bucle while, vamos a construir el programa que desplazará las letras n posiciones a la derecha.
# PISTA: Investiga las funciones chr() y ord() para pasar del valor ASCII de un caracter al caracter y viceversa.
# Ver código ASCII en https://elcodigoascii.com.ar/
n = int(input("Introduce una rotación: "))
i = 65
while i <= 90:
    if i + n <= 90:
        print(chr(i) + ": " + chr(i + n))
    else:
        print(chr(i) + ": " + chr((i - 26) + n))
    i += 1

# Recorrer todos los caracteres de un string
s = "Me gusta el chocolate"
for c in s:
    print(c)

# Vamos a recorrer un string dado con un bucle for y lo vamos a devolver impreso del revés.
s = "se van sus naves"
s_inv = ""
for c in s:
  s_inv = c + s_inv # lo que hace esto es concatenar cada caracter hacia la izquierda de s_inv
print(s_inv)

# Conteo de números
for i in range(1, 11, 1): # los 3 números indican: el inicio, el final, y el salto
  print(i)

for x in range(5): # el número indica: el final
    print(x)

for i in range(1, 11): # el número indica: el inicio, y el final
  print(i)

# Con un bucle for, dada una progresión aritmética de números enteros indicada por el usuario (nos dará el primer término, la diferencia y la cota),
# vamos a calcular la suma de los elementos incluyendo la cota.
# Un ejemplo de progresión aritmética es: 0, 2, 4, 6, 8, ... donde el primer término es 0 y la diferencia entre sus términos es 2.
a0 = int(input("Introduce el término inicial de una progresión aritmética: ")) # número inicial
d = int(input("Introduce la diferencia de dicha progresión aritmética: ")) # salto de número
af = int(input("Indica la cota para finalizar: ")) # número final
sum_an = 0
for an in range(a0, af + 1, d):
  sum_an += an # an contiene todos los números del rango según criterios
print("La suma de los términos de la sucesión que has indicado es", sum_an)

 # Supongamos que queremos que se nos impriman todos los números entre 0 y 100 que no son ni divisibles entre 2 ni entre 5.
for i in range(101):
    if i % 2 == 0 or i % 5 == 0:
        continue
    print(i)

# Con un bucle for, vamos a recorrer un string dado y vamos a imprimir todas las letras salvo por la letra indicada por el usuario.
s = "Predecir el futuro resulta ser un negocio muy difícil en sí"
print("El string original es:", s)
letter = input("Introduce la letra que quieras eliminar del string original: ")
s = s.lower()
letter = letter.lower()
for c in s:
  if c == letter:
    continue
  else:
    print(c, end = "")

# Dado un string, con un bucle for vamos a imprimirlo sin vocales y vamos a salir del bucle si la letra que indique el usuario aparece más de n veces,
# número que también nos proporcionará el usuario.
s = "Pensamos demasiado y sentimos muy poco"
letter = input("Introduce una letra: ")
n = int(input("Indica el máximo número de veces que quieres que aparezca la letra anterior: "))
count = 0
letter = letter.lower()
s = s.lower()
for c in s:
    if count >= n:
        print("\nSe ha superado el número de apariciones")
        break
    if c == letter:
        count += 1
    elif c == "a" or c == "e" or c == "i" or c == "o" or c == "u":
        continue
    print(c, end = "")

# Vamos a calcular las tablas de multiplicar de los números del 1 al 10 anidando dos bucles for:
for i in range(1, 11):
  print("\nTabla de multiplicar del {}".format(i))
  for j in range(1, 21):
    print("{} x {} = {}".format(i, j, i * j))
