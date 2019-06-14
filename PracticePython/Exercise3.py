# Take a list, say for example this one:
#       a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#       and write a program that prints out all the elements of the list that are less than 5.
#
# Extras:
# 1. Instead of printing the elements one by one, make a new list that has all the
#       elements less than 5 from this list in it and print out this new list.
# 2. Write this in one line of Python.
# 3. Ask the user for a number and return a list that contains only elements from the original
#       list a that are smaller than that number given by the user.

# Adam Ouellette
# Exercise 2 http://www.practicepython.org
# June 13 2019

# List of number to check in program
List = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
ListLess = []
CheckNum = int(input("What numbers do you want to check from list to be smaller than: "))


# For loop that will check each number in the list for less than 5 and print the resolute
# print([element for element in List if element < CheckNum])

for element in List:
    if element < CheckNum:
        ListLess.append(element)

for element in ListLess:
    print(element)

print(f"\n\nList Print: {List}")
print(f"ListLess Print: {ListLess}")
