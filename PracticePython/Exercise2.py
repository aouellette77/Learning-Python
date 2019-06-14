# Ask the user for a number. Depending on whether the number is even or odd,
# print out an appropriate message to the user.
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
# 1. If the number is a multiple of 4, print out a different message.
# 2. Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

# Adam Ouellette
# Exercise 2 http://www.practicepython.org
# June 13 2019

Number = int(input("Please enter in a number: "))

if Number % 2 == 0:
    if Number % 4 == 0:
        print(f"The number {Number} is a multiple of 4")
    else:
        print(f"The number {Number} is a even number")
elif Number % 2 != 0:
    print(f"The number {Number} is a odd number")

Num = int(input("\n\nPlease enter in a number to check: "))
Check = int(input("Please enter in a number to divide by: "))
if Num % Check == 0:
    print(f"{Num} divides evenly by, {Check}")
else:
    print(f"{Num} does not divide by, {Check}")
