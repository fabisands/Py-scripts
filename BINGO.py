# Write a script to generate an aleatoric code with a letter and a number (like a BINGO code)

import random

# Ask the user to enter the letters
letters_user = input("Put the letters to use (no spaces nor commas): ").upper()

# Verify if entered values are letters
if not letters_user.isalpha():
    print("Please, enter only letters.")
else:
    # Erase duplicated ones and convert to a list of unique letters
    letters_user = list(set(letters_user))
    
    if not letters_user:
        print("No letters were entered.")
    else:
        # Generate a random letter from the alphabet from the group of entered letters
        random_letter = random.choice(letters_user)

# Ask the user to enter the numbers
print("Let's to establish the range of numbers to use.")
initial = int(input("Enter the first number: "))
last = 1 + int(input("Enter the last number: "))
numbers_range = range(initial, last)

# Check if numbers were entered
if not numbers_range:
    print("No numbers were entered.")
else:
    try:
        # Convert entered numbers to a list of integers
        numbers_integers = [int(num) for num in numbers_range]
        
        # Generate a random number from the set of numbers entered
        number_random = random.choice(numbers_integers)
    except ValueError:
        print("Please, enter only valid numbers.")

number_random_2 = str(number_random)
print(random_letter + number_random_2)
