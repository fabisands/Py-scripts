# Print the first 20 numbers of the Fibonacci succession
Fib_a = 1 # The previous value of the sequence will be stored here
Fib_b = 1 # The current value of the sequence will be stored here
Fib_c = 1 # The sum of the values will be stored
pos = 1 # The position where the sequence begins and continues is indicated here
count = int(input("Introduce the position up to where you want the sequence go to: "))
while pos <= count: # will continue to search for the values of the positions determined by count
    print("Fibonacci's succession in position", pos, "is", Fib_b)
    pos += 1 # the value of the position is increased by 1 to continue searching and printing up to the value given in count
    Fib_a = Fib_b # each time the position increases, the previous value takes the current value (scrolls)
    Fib_b = Fib_c # likewise, the current value takes the value of the sum (scrolls)
    Fib_c = Fib_a + Fib_b # while the value of the sum keeps adding to keep assigning its value to the current one
