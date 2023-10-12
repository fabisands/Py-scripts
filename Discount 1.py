# Write a script to know what's the discount in percentage of a product or service if you change your percentage of earning

cost = float(input("Introduce the cost of the product or service: "))
max_earning = float(input("Introduce the earning of the product or service (only the number, e.g.: 40% = 40): "))
min_earning = float(input("Introduce the new earning smaller than the previous one (only the number, e.g.: 40% = 40): "))

discount = round(((((cost + (cost * (max_earning / 100))) - (cost + (cost * (min_earning / 100)))) / (cost + (cost * (max_earning / 100)))) * 100), 2)
discount_str = str(discount)

print("The percentage of discount of your product or service will be of", discount_str + "%")
