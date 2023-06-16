# Let's to prove if a year is a leap-year or not.
# A year is a leap one if it is divisible by 4 but is not a multiple of 100 unless it is a multiple of 400.

year = int(input("Year: "))
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("The year {} is a leap one".format(year))
        else:
            print("The year {} is not a leap one".format(year))
    else:
        print("The year {} is a leap one".format(year))
else:
    print("The year {} is not a leap one".format(year))
