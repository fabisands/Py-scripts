# Tomar una fecha real y transformarla a una fecha ficticia donde se cuenta desde el 1 de enero del año 1
# y si el año solo tuviera 10 meses y si no exisitieran los meses de julio y agosto.


DAY = int(input("Escribe un día: "))
MONTH = int(input("Escribe un mes: "))
YEAR = int(input("Escribe un año: "))

DAYS_IN_YEAR = (YEAR - 1) * 365 + (YEAR - 1) // 4

DAYS_IN_MONTH = 0
for i in range(0, MONTH - 1):
    if i in (4, 6, 9, 11):
        DAYS_IN_MONTH += 30
    elif i == 2:
        if YEAR % 4 == 0 and (YEAR % 100 != 0 or YEAR % 400 == 0):
            DAYS_IN_MONTH += 29
        else:
            DAYS_IN_MONTH += 28
    else:
        DAYS_IN_MONTH += 31

COUNT_DAYS = DAYS_IN_YEAR + DAYS_IN_MONTH + DAY
print(COUNT_DAYS)

