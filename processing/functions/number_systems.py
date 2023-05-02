def number_systems(number):
    print(f"The decimal number is {number}.")
    print(f"The binary representation of this is: {bin(number)}")
    print(f"The octal representation of this is: {oct(number)}")
    print(f"The hexadecimal representation of this is: {hex(number)}")

def run():
    number_systems(5)

if __name__ == "__main__":
    run()
