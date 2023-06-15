# Vamos a comprobar si un año es bisiesto o no.
# Un año es bisiesto si es divisible entre 4 pero no es múltiplo de 100 a no ser que lo sea de 400.

year = int(input("Año: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("El año {} es bisiesto".format(year))
        else:
            print("El año {} no es bisiesto".format(year))
    else:
        print("El año {} es bisiesto".format(year))
else:
    print("El año {} no es bisiesto".format(year))
