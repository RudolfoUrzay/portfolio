def to_binary(number):
    print(f"The binary representation of {number} is: {bin(number)}")

def to_octal(number):
    print(f"The Octal representation of {number} is: {oct(number)}")

def to_hexadecimal(number):
    print(f"The Hexadecimal representation of {number} is: {hex(number)}")

print("Please enter a character")
character = input()
character_2 = ord(character)
print(f"The ASCII value of {character} is: {character_2}")
to_octal(character_2)
to_hexadecimal(character_2)
to_binary(character_2)

