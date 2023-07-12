BASE = int(input("Introduce the amount of money you want to invest: "))
TY = int(input("Introduce the time in years: "))
RENT = float(input("Introduce the rentability you will get in a year: "))
SAVE_M = float(input("Introduce the payment to the monthly capital: "))
SAVE_Y = SAVE_M * 12

for i in range(TY):
    BASE += BASE * (RENT / 100) + SAVE_Y
    print(round(BASE, 2))

# comment