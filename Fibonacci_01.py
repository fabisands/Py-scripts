# Imprimir los primeros 20 números de la sucesión de Fibonacci
Fib_a = 1 # aquí se va a guardar el valor anterior de la sucesión
Fib_b = 1 # aquí se va a guardar el valor actual de la sucesión
Fib_c = 1 # aquí se va a guardar la suma de los valores
pos = 1 # aquí se indica la posición donde inicia y sigue la sucesión
count = int(input("Introduce la posición hasta donde quieres que llegue la sucesión: "))
while pos <= count: # seguirá buscando los valores de las posiciones determinadas por count
    print("La sucesión de Fibonacci en la posición", pos, "es", Fib_b)
    pos += 1 # se aumenta en 1 el valor de la posición para seguir buscando e imprimiendo hasta el valor dado en count
    Fib_a = Fib_b # cada vez que aumenta la posición, el valor anterior toma el valor actual (se desplaza)
    Fib_b = Fib_c # igualmente, el valor actual toma el valor de la suma (se desplaza)
    Fib_c = Fib_a + Fib_b # mientras que el valor de la suma sigue sumando para seguir asignando su valor al actual
