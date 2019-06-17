# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

# Adam Ouellette
# Exercise 4 http://www.practicepython.org
# June 13 2019

UserNumber = int(input("Pick a number to see the divisors of that number: "))

# list needs to start with number 1 and need to have 1 added to the the number inputted so we will use the number ent
ListRange = list(range(1, UserNumber+1))

# print list of numbers to test
# print(ListRange)

# stored list of numbers that divide with no remainders
DivisorList = []

for number in ListRange:
    if UserNumber % number == 0:    # Checking user input number to the numbers in ListRange for no remainder
        DivisorList.append(number)  # Append the DivisorList with numbers that divide with no remainder
print(DivisorList)
