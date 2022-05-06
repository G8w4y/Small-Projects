import sys
import ASCIIArt

def add(a, b):
    return int(a) + int(b)

def subtract(a,b):
    return int(a) - int(b)

def multiply(a, b):
    return int(a) * int(b)

def divide(a, b):
    return int(a) / int(b)

def calculation(starting_number, operator, second_number):
    '''Takes inputs as string. First number, operator +, -, *, / and second number'''

    if operator == "+":
        try:
            calculation_results = add(starting_number, second_number)
            print(f"{starting_number} {operator} {second_number} = {calculation_results}")
        except TypeError:
            print("Oops! Thats not a valid calculation!")
        return calculation_results
    elif operator == "-":
        try:
            calculation_results = subtract(starting_number, second_number)
            print(f"{starting_number} {operator} {second_number} = {calculation_results}")
        except TypeError:
            print("Oops! Thats not a valid calculation!")
        return calculation_results
    elif operator == "*":
        try:
            calculation_results = multiply(starting_number, second_number)
            print(f"{starting_number} {operator} {second_number} = {calculation_results}")
        except TypeError:
            print("Oops! Thats not a valid calculation!")
        return calculation_results
    elif operator == "/":
        try:
            calculation_results = divide(starting_number, second_number)
            print(f"{starting_number} {operator} {second_number} = {calculation_results}")
        except TypeError:
            print("Oops! Thats not a valid calculation!")
        return calculation_results

def operatorValid(operator):
    if len(operator) == 1:
        try:
            if type(int(operator)) == int:
                return False
        except:
            if operator == "+":
                return True
            elif operator == "-":
                return True
            elif operator == "*":
                return True
            elif operator == "/":
                return True
    else: return False

keep_calculating = True

while keep_calculating:
    print(ASCIIArt.calcArt())
    print("Welcome to the calculator. Type -e at any time to exit the program.")
    starting_number = str(input("Please choose your starting number:\n"))
    if starting_number == "-e":
        sys.exit()
    
    operator = input("Please choose an operator:\n+\n-\n*\n/\n")
    if operator == "-e":
        sys.exit()
    while operatorValid(operator) != True:
        operator = input("Please choose a valid operator:\n+\n-\n*\n/")
        continue
    
    second_number = str(input("Please choose your second number:\n"))
    if second_number == "-e":
        sys.exit()
    calculation_results = calculation(starting_number, operator, second_number)

    another_calculation = input("Would you like to keep calculating with this number?\npress 'y' for yes, and 'n' for no or -e to exit: ").lower()
    if another_calculation == "-e":
        sys.exit()

    while another_calculation == "y":
        print(f"{calculation_results}")
        starting_number = calculation_results
        
        operator = input("Please choose a valid operator:\n+\n-\n*\n/")
        if operator == "-e":
            sys.exit()
        while operatorValid(operator) != True:
            operator = input("Please choose a valid operator:\n+\n-\n*\n/")
            continue
        
        second_number = str(input("Please choose your second number:\n"))
        if second_number == "-e":
            sys.exit()
        
        calculation_results = calculation(starting_number, operator, second_number)
        another_calculation = input("Would you like to keep calculating with this number?\npress 'y' for yes, and 'n' for no: ").lower()
        if another_calculation == "-e":
            sys.exit()
    