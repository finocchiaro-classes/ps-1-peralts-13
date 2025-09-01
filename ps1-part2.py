# Write a function that takes two variables and does all the computations asked
def number_fun(a,b):
    print(f"You entered {a} and {b}")
    addition = a + b
    multiply = a * b
    power = a ** b
    remainder = a % b
    print(f"{a} + {b} = {addition}")
    print(f"{a} * {b} = {multiply}")
    print(f"{a} ** {b} = {power}")
    print(f"{a} % {b} = {remainder}")

# Ask the user for the first number, store the value in a variable

firstnum = int(input("Enter an integer between 10 and 100: "))

# Ask the user for the second number, store the value in a variable
secondnum = int(input("Enter an integer less than 4: "))

# Repeat back the numbers
number_fun(firstnum, secondnum)

# Perform calculations. Be careful about string formatting for autograders.
