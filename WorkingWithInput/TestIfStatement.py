Data = int(input("Input a number greater than 3 and less than 50: "))
# print(len(Data))
if Data < 3:
    print(f"Value {Data} is less than 3")
elif Data > 50:
    print(f"Value {Data} is greater than 50")
else:
    print(f"Your value {Data} is perfect!!")

print("END OF PROGRAM")
