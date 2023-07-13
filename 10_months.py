# Take a real date and turn it into a dummy date where it is count from January 1, year 1; and if every year would have 10 months (without July nor August).

DAY = int(input("Write a day: "))
MONTH = int(input("Write a month: "))
YEAR = int(input("Write a year: "))

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

