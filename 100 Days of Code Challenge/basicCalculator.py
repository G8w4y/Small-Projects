keep_calculating = True

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

while keep_calculating:
    starting_number = str(input("Please choose your starting number:\n"))
    operator = input("Please choose an operator:\n+\n-\n*\n/\n")
    second_number = str(input("Please choose your second number:\n"))
    calculation_results = calculation(starting_number, operator, second_number)
    #print("***********************************************************************************************************************")
    another_calculation = input("Would you like to keep calculating with this number?\npress 'y' for yes, and 'n' for no: ").lower()
    while another_calculation == "y":
        print(f"{calculation_results}")
        starting_number = calculation_results
        operator = input("Please choose an operator:\n+\n-\n*\n/")
        second_number = str(input("Please choose your second number:\n"))
        calculation_results = calculation(starting_number, operator, second_number)
        another_calculation = input("Would you like to keep calculating with this number?\npress 'y' for yes, and 'n' for no: ").lower()


    
    