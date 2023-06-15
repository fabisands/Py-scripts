# Vamos a pedirle al usuario la longitud de una lista y haremos que introduzca por teclado tantos números enteros como haya indicado,
# que se guardarán en una lista. Al acabar, imprimiremos la lista.
n = int(input("Introduce el tamaño de la lista: "))
l = [] # crea una lista vacía preparada para introducir los elementos
for i in range(n):
  l.append(int(input()))
print("Tu lista es:", l)

# Dada una lista de caracteres, le pediremos al usuario qué elemento quiere eliminar y lo eliminaremos de la lista.
l = ["m", "a", "r", "j", "b", "g", "i", "s", "f"]
print("Esta es la lista original:", l)
c = input("Introduce el elemento que quieres eliminar ") # ejemplo, la letra g
if c in l: # revisa si la variable c está en la lista l
  l.remove(c) # y si está, la elimina
print("Esta es la lista actualizada", l)
# En caso de que que exista más de una vez la letra que se quiera eliminar pero se quieren eliminar todas ellas, se hace así:
l = ["m", "a", "r", "j", "b", "g", "i", "s", "f", "g"]
print("Esta es la lista original:", l)
c = input("Introduce el elemento que quieres eliminar ") # ejemplo, la letra g
for e in l: # busca e itera los elementos que están en la lista l
  if e == c: # si ese elemento es igual a la variable c
    l.remove(e) # entonces remueve ese elemento
print("Esta es la lista actualizada", l)

# Vamos a pedir al usuario que ingrese 10 números, los guardaremos en una lista y mostraremos la lista ordenada,
# siendo el usuario quien indique el orden: ascendente o descendente.
reversed = bool(input("Si quieres orden descendente, escribe True. De lo contrario, dale a la tecla Enter: "))
# pues si no se indica el True para el reverse más adelante, este queda como False por defecto
l = []
for _ in range(10): # como dentro del bucle no se usa la variable del for, se puede poner solo un guion bajo
# de esa manera no se guarda la variable en ningún momento, pues no está y no se necesita
  l.append(float(input())) # introduce los datos que necesite dentro de la lista n veces según el range()
l.sort(reverse = reversed) # si el usuario quiere orden decendente, habrá guardado el True en la variable reversed
# en caso de que no lo quiera en orden descendente, el método .sort() lo dejará en orden ascendente
print(l) # entonces imprime la lista según lo que se haya indicado, si en orden descendente o ascendente

