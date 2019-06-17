# Take two lists, say for example these two:
#
#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
# and write a program that returns a list that contains only the elements that are common between the
# lists (without duplicates). Make sure your program works on two lists of different sizes.
#
# Extras:
#
# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

# Adam Ouellette
# Exercise 4 http://www.practicepython.org
# June 13 2019

List1 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
List2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
DupList = []

# Single line not working.  Need to check more into this.
# print([number for number in List1 if List2])

for number in List1:
    if number in List2:
        # print("yes", number)
        DupList.append(number)
    # else:
        # print("no", number)
print(DupList)

