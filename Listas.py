# Una lista es un compendio de elementos ordenados dentro de una variable
# Para acceder a los elementos se utiliza la sintaxis del corchete

list = ["elmento 1", "elemento 2", "elemento 3", "elemento 4", "elemento 5"]
# El elemento 1 está en la posición 0, el elemento 2 está en la posición 1, el elemento 3 está en la posición 2...
# LAS POSICIONES SON LOS ÍNDICES
print(list[0]) # imprime el elemento de la posición 0, es decir, el primer elemento de la lista
print(list[-1]) # imprime el último elemento de la lista
print(list[-2]) # imprime el penúltimo elemento de la lista
print(list[-3]) # imprime el antepenúltimo elemento de la lista
print(list[2:4]) # imprime la colección de la lista desde la posición 2 hasta la posición 3
# Es decir, imprime desde el tercer hasta el cuarto elemento
print(list[:3]) # imprime desde el primer elemento de la lista hasta el elemento en la posición 2
print(list[3:]) # imprime desde el elemento en la posición 2 hasta el último de la lista
list[0] = "elemento 6" # cambia el elemento de la posición 0 por lo que se indique
# En este caso, se cambia "elemento 1" por "elemento 6"
list[3] = "elemento 7" # lo mismo: cambia el elemento de la posición 3 por lo que se indique
# En este caso, se cambia "elemento 4" por "elemento 7"

# Añadir elementos al final de una lista con .append()
names = ["Maria", "Cristina", "Juana"]
names.append("Andrea")
names.append("Ana")
print(names) # entonces se imprime la lista ["María", "Cristina", "Juana", "Andrea", Ana]

# Añadir elementos a una lista en una posición específica con .insert()
names = ["Mario", "Cristian", "Juan"]
names.insert(1, "Andres")
names.insert(3, "Miguel")
print(names) # entonces se imprime la lsita ["Mario", "Andrés", Cristian", "Miguel", "Juan"]

# Bucles con listas:
# Si quisiéramos imprimir por pantalla todos los elementos de una lista, lo podríamos hacer mediante los índices
for i in range(len(names)):
  print(names[i])
# o mucho más fácilmente iterando la lista con un for con la siguiente sintaxis:
for name in names:
  print(name)

# Concatenación de listas:
# Dadas dos o más listas, podemos concatenarlas haciendo uso de la función +
l1 = [True, 21, "Marta"]
l2 = [22.5, False, 22, "Rafa"]
print(l1 + l2) # entonces imprime [True, 21, 'Marta', 22.5, False, 22, 'Rafa']

# Repetición de listas:
# Podemos repetir una misma lista tantas veces como queramos con la función *
abc = ["A", "B", "C"]
print(abc * 5) # entonces imprime ['A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C', 'A', 'B', 'C']
# O de otra manera, igualmente se puede hacer así:
print(["A", "B", "C"] * 5) # entonces imprime lo mismo que en el caso anterior
# O se puede iterar números dentro de una lista, así:
print([0] * 5) # entonces imprime cinco ceros en lista: [0, 0, 0, 0, 0]

# Para crear una lista vacía simplemente no se mete nada en su interior, así:
empty_list = [] # entonces se crea la lista vacía preparada para que se le introduzcan elementos
print(len(empty_list)) # imprime un 0, pues como no hay nada en la lista, la longitud de sus elementos es cero.

# El método .count() recibe un elemento como argumento y cuenta la cantidad de veces que aparece en la lista
numbers = [0, 1, 1, 2, 2, 2, 3, 3, 3, 3]
counted = []
for element in numbers:
  if element not in counted:
    counted.append(element)
    print("El elemento {} aparece {} veces".format(element, numbers.count(element)))

# El método .extend() extiende la lista agregando al final el iterable indicado por parámetro.
numbers = [1, 2, 3, 4, 5]
print(numbers)
numbers.extend([6]) # agrega el 6
print(numbers)
numbers.extend([7, 8]) # agrega el 7 y el 8
print(numbers)
numbers.extend(range(9, 16)) # agrega el rango entre 9 y 15
print(numbers)

# El método index() recibe un elemento como argumento y devuelve el índice de la primera aparición en la lista.
numbers = [0, 1, 1, 2, 2, 2, 3, 4, 3, 4]
print(numbers.index(2)) # devuelve el 3, es decir que el número 2 está en la posición 3
print(numbers.index(4)) # devuelve el 7, es decir que el número 4 está en la posición 7

# El método .pop() devuelve el último elemento de la lista y lo borra de la misma. Es decir, es lo contrario de .append()
print(numbers) # imprime la lista con el último número incluído
print(numbers.pop()) # imprime el último número el cual borrará de la lista
print(numbers) # imprime la lista sin el último número el cual fue borrado por .pop()
# Una forma de hacerlo de manera iterativa es así:
print(numbers)
for i in range(5): # el range(5) es la cantidad de veces que se va a iterar el .pop(), es decir, 5 en este caso
    print(numbers.pop())
    print(numbers)

# El método .remove() recibe como argumento un elemento y borra su primera aparición de la lista.
numbers = [0, 1, 2, 4, 3, 4, 5, 6, 7]
numbers.remove(4) # entonces borra el primer 4 que aparece en la lista
print(numbers) # entonces imprime [0, 1, 2, 3, 4, 5, 6, 7]

# El método .reverse() devuelve la lista en orden inverso.
numbers = [1, -1, 2, -2, 3, -3]
numbers.reverse()
print(numbers) # imrpime [-3, 3, -2, 2, -1, 1]

# El método .sort() devuelve la lista en orden.
numbers = [1, 3, 5, 2, 4]
numbers.sort()
print(numbers) # imprime [1, 2, 3, 4, 5]

# Si quisiésemos ordenar los elementos en orden decreciente, podríamos hacer uso del parámetro reverse del método .sort():
numbers = [1, 3, 5, 2, 4]
numbers.sort(reverse = True)
print(numbers) # imprime [5, 4, 3, 2, 1]
# Otra manera podría ser:
numbers = [1, 3, 5, 2, 4]
numbers.sort()
numbers.reverse()
print(numbers) # imprime [5, 4, 3, 2, 1]

# Conversión a listas
# Para convertir un objeto iterable de Python a lista, hay que usar la función list()
print(range(0, 100, 10))
# Imprime "range(0, 100, 10)"
print(type(range(0, 100, 10)))
# Imprime "<class 'range'>"
print(list(range(0, 100, 10)))
# Imprime "[0, 10, 20, 30, 40, 50, 60, 70, 80, 90]"
print(type(list(range(0, 100, 10))))
# Imprime "<class 'list'>"

