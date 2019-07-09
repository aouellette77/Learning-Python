# Ask the user for a string and print out whether this string is a palindrome or not.
# (A palindrome is a string that reads the same forwards and backwards.)

user_word = str(input("Please inter a word: ").lower())
reverse_word = user_word[::-1]
print("User Word: ", user_word)
print("Reverse Word: ", reverse_word, "\n")
if user_word == reverse_word:
    print("This word is a palindrome")
else:
    print("This word is not a palindrome")
