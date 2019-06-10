# First Python Program using PyCharm and GitHub

print("***** PROGRAM 1 - INPUT *****")

FirstName = input("What is your first name: ")
LastName = input("What is your last name: ")

if len(FirstName) < 3 or len(LastName) < 3:
    print("First or Last name must have more then three charters each")

elif len(FirstName) > 50 or len(LastName) > 50:
    print("First or Last name can't have more then fifty charters each")
else:
    Age = int(input("What is your age: "))
    AgeInMonths = Age * 12
    AgeInWeeks = Age * 52
    AgeInDays = Age * 365
    AgeInHours = Age * 8760
    print("Hello, {} {}".format(FirstName, LastName))
    print(f"Hello, {FirstName} {LastName}")

    print("You are currently {0:d} years old".format(Age))
    print(f"You are currently {Age} years old")

    print("You are currently {0:d} months old".format(AgeInMonths))
    print(f"You are currently {AgeInMonths} months old")

    print("You are currently {0:d} weeks old".format(AgeInWeeks))
    print(f"You are currently {AgeInWeeks} weeks old")

    print("You are currently {0:d} days old".format(AgeInDays))
    print(f"You are currently {AgeInDays} days old")

print("\nEND OF PROGRAM")
