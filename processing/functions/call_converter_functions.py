import number_system_converter as nsc

def run2():
    variable = int(input(print("Please enter an int number:")))
    print(f"The Binary representation of {variable} is: {nsc.to_binary(variable)}")
    print(f"The Hexadecimal representation of {variable} is: {nsc.to_hexadecimal(variable)}")
    print(f"The Octadecimal representation of {variable} is: {nsc.to_octal(variable)}")

if __name__ == '__main__':
    run2()





