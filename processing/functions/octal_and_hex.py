def run():
    print("Please enter a number: ")
    number = int(input())
    print("Would you like to display it on octal or hexadecimal?")
    display = input()

    if display.lower() == "octal":
        print(f"The display of the number {number} in octal is {oct(number)}")
    elif display.lower() == "hexadecimal":
        print(f"The display of the number {number} in hexadecimal is {hex(number)}")
    else:
        print("Error: Option not available!!")

if __name__ == "__main__":
  run()