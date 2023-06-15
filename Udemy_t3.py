# 1. Haz que un usuario introduzca un número real y evalúa si dicho número es positivo, negativo o cero. Devuelve por pantalla el resultado en cada caso.
num = float(input("Introduzca un número real: "))
if (num <= 0 or num > 0):
    if num < 0:
        print("{} es un número negativo".format(num))
    else:
        if num > 0:
            print("{} es un número positivo".format(num))
        else:
            print("{} es igual a cero".format(num))
else:
    print ("{} no es un número real".format(num))

# 2. Haz que un usuario introduzca su nombre y evalúa con operadores if y else si dicho nombre tiene una longitud mayor a 10 caracteres o no.
#    Devuelve por pantalla el resultado en cada caso.
name = input("Introduzca su nombre (sin apellidos): ")
char = len(name)
if char > 10:
    print("Tu nombre tiene más de 10 caracteres")
else:
    print("Tu nombre tiene 10 o menos caracteres")

# 3. Realiza el ejercicio anterior con el uso del operador ternario.
name = input("Introduzca su nombre (sin apellidos): ")
char = len(name)
print("Tu nombre tiene más de 10 caracteres") if char > 10 else print("Tu nombre tiene 10 o menos caracteres")

# 4. Haz que un usuario introduzca dos números enteros positivos. Comprueba si el primer número introducido
#    por el usuario es mayor o igual que el segundo número introducido por el usuario. Devuelve por pantalla el
#    resultado en cada caso.
#    PISTA: Asegúrate de hacer uso de la función int() donde pertoque.
fn = int(input("Introduce el primer número entero positivo: "))
sn = int(input("Introduce el segundo número entero positivo: "))
if fn >= sn:
    print("El primer número es mayor o igual que el segundo")
else:
    print("El primer número es menor que el segundo")

# 5. Haz que un usuario introduzca dos números enteros positivos. Suponiendo que el primer número introducido
#    por el usuario es mayor o igual al segundo número introducido por el usuario, comprueba que la división del
#    primer número entre el segundo número es exacta.
#    En caso de la división ser exacta, devuelve el cociente por pantalla e indica que la división en efecto es exacta.
#    En caso de la división no ser exacta, devuelve el cociente y el resto por pantalla e indica que la división entre
#    los dos números no es exacta
fn = int(input("Introduce el primer número entero positivo: "))
sn = int(input("Introduce el segundo número entero positivo: "))
if (fn % sn == 0):
    print("{} dividido en {} es igual a {} y no tiene resto alguno, por lo que es una división exacta".format(fn, sn, fn//sn))
else:
    print("{} dividido en {} es igual a {} y su resto es igual a {}, por lo que no es una división exacta".format(fn, sn, fn//sn, fn%sn))

# 6. Fusiona lo hecho en los ejercicios 4 y 5 para que:
#       1. Un usuario introduzca dos números enteros por pantalla.
#       2. Comprobar si el primer número es mayor o igual al segundo número introducido por el usuario. Devolver
#          por pantalla en que caso nos encontramos.
#       3. Hacer la división entera pertinente en cada caso.
#       4. Si la división es exacta, entonces devolver por pantalla el cociente e indicar que la división es exacta.
#          Si la división no es exacta, entonces devolver por pantalla el cociente y el resto e indicar que la división
#          realizada no es exacta.
fn = int(input("Introduce el primer número entero: "))
sn = int(input("Introduce el segundo número entero: "))
if fn >= sn:
    print("El primer número es mayor o igual que el segundo")
    print("Por lo tanto, vamos a dividir {} entre {}".format(fn, sn))
    if fn % sn == 0:
        print("La división es exacta y el cociente es {}".format(fn//sn))
    else:
        print("La división no es exacta. El cociente es {} y el resto es {}".format(fn//sn, fn%sn))
else:
    print("El segundo número es mayor que el primero")
    print("Por lo tanto, vamos a dividir {} entre {}".format(sn, fn))
    if sn % fn == 0:
        print("La división es exacta y el cociente es {}".format(sn//fn))
    else:
        print("La división no es exacta. El ciciente es {} y el resto es {}".format(sn//fn, sn%fn))

# 7. Haz que un usuario introduzca dos números enteros positivos. Comprueba si el mayor es múltiplo del menor.
#    Devuelve por pantalla el resultado en cada caso.
fn = int(input("Introduce el primer número entero positivo: "))
sn = int(input("Introduce el segundo número entero positivo: "))
if fn >= sn:
    if (fn % sn == 0):
        print("{} es múltiplo de {}".format(fn, sn))
    else:
        print("{} no es múltiplo de {}".format(fn, sn))
else:
    if (sn % fn == 0):
        print("{} es múltiplo de {}".format(sn, fn))
    else:
        print("{} no es múltiplo de {}".format(sn, fn))

# 8. Haz que un usuario introduzca una palabra y comprueba si dicha palabra empieza por mayúscula. Devuelve
#    por pantalla el resultado en cada caso.
word = input("Introduce una palabra: ")
if word[0] == word[0].upper():
    print("La primera letra de tu palabra es una mayúscula")
else:
    print("La primera letra de tu palabra es una minúscula")

# 9. Haz un usuario introduza una letra y comprueba si se trata de una vocal. Si el usuario introduce un string
#    de más de un carácter, infórmale de que no se puede procesar el dato, pues debe tener como máximo tamaño 1.
#    PISTA: Convierte la letra introducida a minúsculas para tener que realizar menos comprobaciones
letter = input("Introduce una letra: ").lower()
if len(letter) == 1 and letter.isalpha():
    if (letter == "a" or letter == "e" or letter == "i" or letter == "o" or letter == "u"):
        print("Tu letra es una vocal")
    else:
        print("Tu letra es una consonante")
else:
    print("No se puede procesar el dato, pues este tiene que tener como máximo 1 caracter y tiene que ser alfabético")

# 10. Ver PDF tarea 3.
import math
print('Dada la ecuación de segundo grado "ax^2 + bx + c = 0"')
print('Y teniendo en cuenta la fórmula cuadrática "(x = -b +/- (√b^2 - 4ac))/(2a)"')
a = float(input('Introduce el valor del coeficiente "a": '))
b = float(input('Introduce el valor del coeficiente "b": '))
c = float(input('Introduce el valor del coeficiente "c": '))
if (a != 0):
    delta = b ** 2 - 4 * a * c
    if (delta > 0):
        sr = math.sqrt(delta)
        x1 = ((-b) + sr)/(2 * a)
        x2 = ((-b) - sr)/(2 * a)
        print('Hay 2 soluciones las cuales son "x = {}" y "x = {}"'.format(x1, x2))
    elif delta == 0:
        x = (-b)/(2* a)
        print('Hay 1 solución la cual es "x = {}"'.format(x))
    else:
        print("No existe solución dentro del conjunto de los números reales para esta ecuación de segundo grado")
else:
    print('El valor del coeficiente "a" es cero, y no se puede dividir entre cero teniendo en cuenta la fórmula cuadrática')
