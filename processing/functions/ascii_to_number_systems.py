def ascii_to_number_systems(quantity):
    for count in range(quantity):
        print("Please enter a character:")
        character = input()
        number = ord(character)
        print(f"The ASCII value is {number}.")
        print(f"The binary representation of {number} is: {bin(number)}")
        print(f"The octal representation of {number} is: {oct(number)}")
        print(f"The hexadecimal representation of {number} is: {hex(number)}")

ascii_to_number_systems(2)
