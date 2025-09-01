
# Ask the user for the first number, store the value in a variable
firstnum = int(input("Enter an integer between 10 and 100: "))
        
# Ask the user for the second number, store the value in a variable
secondnum = int(input("Enter an integer less than 4: "))

# Repeat back the numbers
print(f"You entered {firstnum} and {secondnum}")

# Perform calculations. Be careful about string formatting for autograders.    
addition = firstnum + secondnum
multiply = firstnum * secondnum
power = firstnum ** secondnum
remainder = firstnum % secondnum
          
print(f"{firstnum} + {secondnum} = {addition}")
print(f"{firstnum} * {secondnum} = {multiply}")
print(f"{firstnum} ** {secondnum} = {power}")
print(f"{firstnum} % {secondnum} = {remainder}")
