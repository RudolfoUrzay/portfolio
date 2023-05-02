print("Program Started")

print("Please enter a standard character:")

character = input()

if len(character) == 1:
    print(f"The ASCII code for {character} is {ord(character)}")
else:
    print("Not a single character")

print("Program ended")


