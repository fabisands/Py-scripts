BASE = int(input("Intoduce el dinero que quieres invertir: "))
TY = int(input("Introduzca el timepo en años: "))
RENT = float(input("Introduzca la rentabilidad que recibirá al año: "))
SAVE_M = float(input("Introduce el abono al capital mensual: "))
SAVE_Y = SAVE_M * 12

for i in range(TY):
    BASE += BASE * (RENT / 100) + SAVE_Y
    print(round(BASE, 2))
