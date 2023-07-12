print("Find x in the ecuation Ax+B=0")
A=float(input("Coeficient A = "))
B=float(input("Coeficient B = "))
if A != 0:
    sol = -B/A
    print("The solution is x =", sol)
else:
    print("There is no ecuation to solve because A = 0")

# comment