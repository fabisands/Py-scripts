# Pyratilla hizo un formulario para que los interesados en formar parte de su tripulación rellenaran y así poder evitarse más de una entrevista innecesaria.

# Ahora es momento de filtrar las convocatorias:

# El nombre debe empezar por mayúscula. Si es un nombre compuesto, entonces todos deben empezar por mayúscula.
# La edad debe ser mayor o igual a 16 y menor o igual a 40.
# El hobby indicado debe tener más de 10 caracteres.
# La casilla del sueño no puede haber sido dejada en blanco.

# Ayuda a Pyratilla a crear este filtro para descartar solicitudes que no cumplan estos requisitos.

interview = False
name = False
age = False
hobby = False
dream = False

if name.find(" ") == -1:
    if name[0].isupper():
        name = True
else:
    if name.istitle():
        name = True

if (age >= 16 and age <= 40):
    age = True

if len(hobby) > 10:
    hobby = True

if dream != "" or dream != " ":
    dram = True

if name and age and hobby and dream:
    interview = True
    print("Se le concede una entrevista a este solicitante")
else:
    print("No cumple los requisitos mínimos para pertenecer a la tripulación de Pyratilla")


# De tantas solicitudes que ha recibido, Pyratilla no cabe en sí de la emoción y se pone a cantar

# "99 bottles of rum on the wall, 99 bottles of rum.
# Take one down, pass it around, 98 bottles of rum on the wall.
# 98 bottles of rum on the wall, 98 bottles of rum.
# Take one down, pass it around, 97 bottles of rum on the wall..."

# Ayuda a Pyratilla a cantar la canción al completo con un bucle while y luego lo mismo con un bucle for.

# Con bucle while:
b = 99
while b > 0:
    print("{} bottles of rum on the wall, {} bottles of rum.".format(b, b))
    b -= 1
    if b > 1:
        print("Take one down, pass it around, {} bottles of rum on the wall.".format(b))
    if b == 1:
        print("Take one down, pass it around, {} bottle of rum on the wall.".format(b))
        print("{} bottle of rum on the wall, {} bottle of rum.".format(b, b))
        print("Take one down, pass it around, no more bottles of rum on the wall.")
        break

# Con bucle for:
b = 99
for i in range(99, 1, -1):
    print("{} bottles of rum on the wall, {} bottles of rum.".format(b, b))
    b -= 1
    if b > 1:
        print("Take one down, pass it around, {} bottles of rum on the wall.".format(b))
    if b == 1:
        print("Take one down, pass it around, {} bottle of rum on the wall.".format(b))
        print("{} bottle of rum on the wall, {} bottle of rum.".format(b, b))
        print("Take one down, pass it around, no more bottles of rum on the wall.")
