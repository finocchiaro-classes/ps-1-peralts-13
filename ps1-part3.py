
def heart_rate(age, goal):
    max_HR = 220 - age
    print(f"Your maximum heart rate is: {max_HR}")
    
    if goal == 'S':
        target_low = max_HR * .8
        print(f"Your target heart rate is between {target_low} and {max_HR}")
    elif goal == 'E':
        target_high = max_HR * .8
        target_low = max_HR * .6
        print(f"Your target heart rate is between {target_low} and {target_high}")

user_age = int(input("What is your age? "))
user_goal = input("Is your goal speed (S) or endurance (E)? ")

heart_rate(user_age, user_goal)
