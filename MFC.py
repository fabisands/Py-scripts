print("-" * 130)
print("Tenga en cuenta que para estos cálculos se usará el Sistema Internacional, por lo que los volúmenes estarán")
print("en metros cúbicos (m3), las masas en kilogramos (Kg) y las densidades en kilogramos por metro cúbico (Kg/m3).")
print("Igualmente, para los decimales se empleará el punto (.) mas no la coma (,).")
print()
print("NOTA: para dar finalización al programa, introduzca el número cero (0) cuando le pida ingresar algún dato.")
print("Para introducir números en notación científica, introduzca el número reducido seguido de *10** seguido del número exponente correspondiente; ejemplos:")
print("12310.258 = 12.31*10**3")
print("0.0001231 = 12.31*10**-5")
print("-" * 130)
om = float(input("¿Qué tipo de material orgánico va a emplear? Si es ácido acético introduzca el número 1, y si es glucosa introduzca el 2: "))
# "om" es "organic material" o "material orgánico"
while om != 0:
    if om == 1:
        vol_aa = float(input("Introduzca el volumen de ácido acético a utilizar (m3): ")) # "vol_aa" es "volume of acetic acid" o "volumen de ácido acético"
        molar_aa = float(input("Introduzca la concentración molar del ácido acético a utilizar (M): ")) # M = moles de soluto / Litros de solución
        mol_aa = molar_aa * vol_aa
        Ac = 6.02214076*10**23 # "Ac" es "Avogadro's constant" o "Constante de Avogadro"
        # 1 mol es igual a 6.02214076x10^23 unidades
        mq_aa = mol_aa * Ac # "mq_aa" es "molecules quantity of acetic acid" o "cantidad de moléculas de ácido acético"
        # 1 molécula de ácido acético + 2 de agua producen 2 moléculas de CO2 + 8 protones (H+) + 8 electrones (e-)
        mq_w = mq_aa * 2 # "mq_w" es "molecules quantity of water" o "cantidad de moléculas de agua" que se necesitan.
        mol_w = mq_w / Ac # "mol_w" es "moles of water" o "moles de agua"
        # 1 mol de agua pesa 1 gramo, y 1 gramo es equivalente a 1 mL
        vol_w = mol_w * 1000 * 1000 # "vol_w" es "volumen of water" o "volumen de agua" que se necesita
        # Ya que las mol_w se multiplica por 1 gramo y se divide por 1 mol, obteniéndose los gramos, y esos gramos son iguales a los mL
        # Así que para obtener los litros, se multiplican esos mL por 1000, y luego se multiplica de nuevo por 1000 para obtener los m3.
        print("Cantidad de H2O que se necesita para {} litros de ácido acético: {} litros.".format(vol_aa, vol_w))
        mq_CO2 = mq_aa * 2 # "mq_CO2" es "molecules quantity of CO2" o "cantidad de moléculas de CO2"
        mol_CO2 = mq_CO2 / Ac # "mol_CO2" es " moles of CO2" o "moles de CO2"
        break
    elif om == 2:
        mass = float(input("Introduzca la masa de glucosa a utilizar: "))
        break
    else:
        print("El valor ingresado no es ni 1 ni 2. Por favor introduzca solamente alguno de esos dos números correspondiendo a la materia orgánica a utilizar.")
        om = float(input("¿Qué tipo de material orgánico va a emplear? Si es ácido acético introduzca el número 1, y si es glucosa introduzca el 2: "))
