def ascii_to_number_system(character, number_system):
    number = ord(character)
    print(f"The character is m (ASCII: {number})")

    if number_system == "binary":
        print(f"The binary representation of {number} is: {bin(number)}")
    elif number_system == "octal":
        print(f"The octal representation of {number} is: {oct(number)}")
    elif number_system == "hexadecimal":
        print(f"The hexadecimal representation of {number} is: {hex(number)}")
    else:
        print("Invalid number system.")



ascii_to_number_system("t", "hexadecimal")

