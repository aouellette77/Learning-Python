command = ""
started = False
while True:
    command = input("help >> ").lower()
    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car is now started....")
    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car is now stopped....")
    elif command == "go":
        if started:
            print("Car is moving forward...")
        else:
            print("Car can't move forward without being started!")
    elif command == "help":
        print("""
Commands you can use:
help - Help menu
start - To start the car
stop - To stop the car
go - To move the car forward
quit - To quit the game
        """)
    elif command == "quit":
        print("\nThank you for Playing")
        break
    else:
        print("That command is not allowed")
else:
    print("\nThank you for Playing")
