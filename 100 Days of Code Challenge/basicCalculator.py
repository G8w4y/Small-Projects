# Author: G8w4y
# This is a basic calculator that lets the user calculate on previously calculated results.
# The calculator has simple errorhandling functionalities. Urging the user to use correct syntax while operating the program.


import sys
import ASCIIArt

# Define the functions that will define the calculators capabilitites
def add(a, b):
    return format(float(a) + float(b), '.2f')

def subtract(a,b):
    return format(float(a) - float(b), '.2f')

def multiply(a, b):
    return format(float(a) * float(b), '.2f')

def divide(a, b):
    return format(float(a) / float(b), '.2f')

def calculation(starting_number, operator, second_number):
    '''Takes inputs as string. First number, operator +, -, *, / and second number'''

    if operator == "+":
        # Always making sure that the user types inn valid inputs, looping back and prompting the user again if not.
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

# Define a function that checks for a valid operator input
def operatorValid(operator):
    "This function checks to see if the operator inputted by the user is of a valid type and format, returning True, returning False if not"
    if len(operator) == 1:
        try:
            if type(int(operator)) == int:
                return False
            elif type(float(operator)) == float:
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

# We want to keep calculating as long as the user wants.
keep_calculating = True
while keep_calculating:
    print(ASCIIArt.calcArt())
    print("Welcome to the calculator. Type -e at any time to exit the program.")
    starting_number = str(input("Please choose your starting number:\n"))
    # Giving the user the ability to always exit the program
    if starting_number == "-e":
        sys.exit()
    
    operator = input("Please choose an operator:\n+\n-\n*\n/\n")
    if operator == "-e":
        sys.exit()
    # Always making sure that the user types inn valid inputs, looping back and prompting the user again if not.
    while operatorValid(operator) != True:
        operator = input("Please choose a valid operator:\n+\n-\n*\n/\n")
        continue
    
    second_number = str(input("Please choose your next number:\n"))
    if second_number == "-e":
        sys.exit()
    calculation_results = calculation(starting_number, operator, second_number)

    # Keep running a second calculation on the previus result, as long as the user wants.
    another_calculation = input(f"Would you like to keep calculating with {calculation_results}?\npress 'y' for yes, and 'n' for no: ").lower()
    if another_calculation == "-e":
        sys.exit()

    while another_calculation == "y":
        print(f"{calculation_results}")
        starting_number = calculation_results
        
        operator = input("Please choose a valid operator:\n+\n-\n*\n/\n")
        if operator == "-e":
            sys.exit()
        while operatorValid(operator) != True:
            operator = input("Please choose a valid operator:\n+\n-\n*\n/\n")
            continue
        
        second_number = str(input("Please choose your next number:\n"))
        if second_number == "-e":
            sys.exit()
        
        calculation_results = calculation(starting_number, operator, second_number)
        another_calculation = input(f"Would you like to keep calculating with {calculation_results}?\npress 'y' for yes, and 'n' for no: ").lower()
        if another_calculation == "-e":
            sys.exit()