# First Python Program using PyCharm and GitHub

print("***** PROGRAM 1 - INPUT *****")

FirstName = input("What is your first name: ")
LastName = input("What is your last name: ")
Age = int(input("What is your age: "))
AgeInMonths = Age * 12
AgeInWeeks = Age * 52
AgeInDays = Age * 365
AgeInHours = Age * 8760

print("Hello, {} {}".format(FirstName, LastName))
print("You are currently {0:d} years old".format(Age))
print("You are currently {0:d} months old".format(AgeInMonths))
print("You are currently {0:d} weeks old".format(AgeInWeeks))
print("You are currently {0:d} days old".format(AgeInDays))
print("You are currently {0:d} hours old".format(AgeInHours))
