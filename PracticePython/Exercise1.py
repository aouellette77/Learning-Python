# Create a program that asks the user to enter their name and their age.
# Print out a message addressed to them that tells the year that they will turn 100 years old.

# Extras:
# Add on to the previous program by asking the user for another number and printing out
#     that many copies of the previous message.  (Hint: order of operations exists in Python)
# Print out that many copies of the previous message on separate lines.
#     (Hint: the string "\n is the same as pressing the ENTER button)

# Adam Ouellette
# Exercise 1 http://www.practicepython.org
# June 13 2019

import datetime
Date = datetime.datetime.now()

# Input from user for Name and Age
Name = input("What is your full name: ")
Age = int(input("What is your current age: "))

# Extra on how many copies of the message do you want
Copies = int(input("How many copies of the message do you want to see: "))

FutureYear = (Date.year - Age) + 100

print(f"\nHello, {Name}.  You will be 100 years old in {FutureYear}!\n" * Copies)
