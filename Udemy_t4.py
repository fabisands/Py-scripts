# Ejercicio 1:
# Haz que el usuario introduzca números enteros por teclado.
# Mientras el usuario no introduzca el 0, muestra si el número introducido es par o impar.
print("Recuerda: para finalizar el programa, introduce el 0 (cero)")
n = int(input("Introduce un número entero: "))
while n != 0:
    if n % 2 == 0:
        print("El número es par")
    else:
        print("El número es impar")
    n = int(input("Introduce un número entero: "))
print("El programa ha finalizado")

# Ejercicio 2:
# Haz que el usuario introduzca una palabra y una letra por teclado. Comprueba si la palabra contiene la
# letra o no e indícaselo al usuario por pantalla.
word1 = input("Introduce una palabra: ")
word2 = word1.lower()
letter1 = input("Introduce una letra: ")
letter2 = letter1.lower()
x = False
for c in word2:
    if c == letter2:
        x = True
if x:
    print("La palabra", word1, "contiene la letra", letter1)
else:
    print("La palabra", word1, "NO contiene la letra", letter1)

# Ejercicio 3:
# Haz que el usuario introduzca precios por teclado (si introduce 0, entonces es que ha finalizado). Si el usuario
# pasa de 200€, entonces ya no debe poder introducir más precios pues se ha pasado de presupuesto. Sea cual
# sea el resultado (o bien el precio final o bien que no tiene más presupuesto), indícaselo por pantalla al usuario.
print("Para dar finalización, introduzca el 0 (cero)")
price = float(input("Introduce un precio (si son céntimos, utiliza los decimales con punto): "))
sum = 0
while price != 0:
    sum += price
    if sum > 200:
        print("Has excedido el presupuesto con un total de", str(round(sum, 2)) + "€")
        break
    else:
        price = float(input("Introduce un precio (si son céntimos, utiliza los decimales con punto): "))
if price == 0:
    print("El precio total es de", str(round(sum, 2)) + "€")

# Ejercicio 4:
# Haz que el usuario introduzca números enteros por teclado. Mientras el usuario no introduzca el 0, calcula
# cuántos números positivos y cuántos negativos ha introducido y muéstraselo al final.
print("Para dar finalización, introduzca el 0 (cero)")
num = int(input("Introduce un número entero positivo o negativo: "))
count1 = 0
count2 = 0
while num != 0:
    if num > 0:
        count1 += 1
        num = int(input("Introduce un número entero positivo o negativo: "))
    if num < 0:
        count2 += 1
        num = int(input("Introduce un número entero positivo o negativo: "))
if num == 0:
    print("La cantidad de números positivos que haz introducido es de", count1)
    print("La cantidad de números negativos que haz introducido es de", count2)

# Ejercicio 5:
# Haz que el usuario introduzca números por teclado. Mientras el usuario no introduzca el 0, pídele otro
# número. Cuando el usuario introduzca el 0, muéstrale la media aritmética de los números que ha introducido.
print("Para dar finalización, introduzca el 0 (cero)")
num = int(input("Introduce un número cualquiera: "))
sum = 0
count = 0
while num != 0:
    sum += num
    count += 1
    num = int(input("Introduce otro número cualquiera: "))  
if num == 0:
    med = sum/count
    print(med)

# Ejercicio 6:
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime todos los números que se encuentren entre los dos
# números introducidos por el usuario (los extremos incluidos).
n1 = int(input("Introduce un número entero: "))
n2 = int(input("Introduce otro número entero MAYOR al anterior: "))
for i in range(n1, n2 + 1):
    print(i)

# Ejercicio 7:
# Haz que el usuario introduzca dos números enteros por teclado. El primero será el extremo izquierdo del
# intervalo y, el segundo, el extremo derecho. Imprime la suma de todos los múltiplos de 3 que se encuentren
# entre los dos números introducidos por el usuario (los extremos incluidos). Finalmente, muestra por pantalla
# el resultado de la suma.
n1 = int(input("Introduce un número entero: "))
n2 = int(input("Introduce otro número entero MAYOR al anterior: "))
for i in range(n1, n2 + 1):
    if i % 3 == 0:
        print (i)

# Ejercicio 8:
# Pídele al usuario cuántos números va a introducir. Con un bucle for, solicítale esa cantidad de números y
# calcula su producto.
c = int(input("¿Cuántos números quieres introducir?: "))
n = int(input("Introduce un número: "))
for i in range(1, c):
    if i <= c:
        n0 = int(input("Introduce otro número: "))
        n = n * n0
print("El producto de los números introducidos es", n)

# Ejercicio 9:
# Haz que el usuario introduzca su edad y el año actual. Imprime todos los años que han pasado desde su año
# de nacimiento hasta el año actual (ambos incluidos).
age = int(input("Introduzca su edad en años: "))
year1 = int(input("Introduzca el año actual: "))
year0 = year1 - age # se obtiene el año de nacimiento
for i in range(year0, year1 + 1):
    print(i)

# Ejercicio 10:
# Haz que el usuario introduzca un número entero. Muestra un cuadrado y luego un triángulo rectángulo de
# lado y altura, respectivamente, el número entero introducido. Por ejemplo, si el usuario introduce como
# número 5, se deberá mostrar:
#   *          * * * * *
#   * *        * * * * *
#   * * *      * * * * *
#   * * * *    * * * * *
#   * * * * *  * * * * *
n0 = int(input("Introduce un número entero: "))
n = int((n0 ** 2) ** 0.5) # en caso de que se introduzca un número entero negativo
c = 0 # cantidad de asteriscos que se agregan al triángulo rectángulo conforme se va iterando
for i in range(1, n + 1):
    if i <= n:
        as_t = (n - (n-1) + c) # asteriscos del triángulo rectángulo
        esp = n - as_t + 1 # espacios entre triángulo rectángulo y cuadrado
        as_c = n # asteríscos del cuadrado
        c += 1 # se agrega un asterisco más por cada iteración
        print("* " * as_t + "  " * esp + "* " * as_c)
