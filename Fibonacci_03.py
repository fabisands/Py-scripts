# Imprimir los primeros 20 números de la sucesión de Fibonacci
Fib_ant = 1 # término anterior
Fib = 1 # término actual
idx = 3 # como ya tenemos los dos primeros términos, empezamos con el índice 3
print("El término {} ocupa la posición {}".format(Fib_ant, 1))
print("El término {} ocupa la posición {}".format(Fib, 2))
while idx <= 20: # establecemos una cota para que el bucle no sea infinito
    temp = Fib # guardamos temporalmente el valor actual
    Fib += Fib_ant # calculamos el nuevo término de la sucesión
    Fib_ant = temp # modificamos el valor del término anterior
    print("El término {} ocupa la posición {}".format(Fib, idx))
    idx += 1 # incrementamos el valor del índice
