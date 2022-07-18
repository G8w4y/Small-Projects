from msilib.schema import Error
from data import MENU
from data import resources
# 3 different MENU, each with their unique amount of ingredients
print(MENU['espresso']['cost'])
command = str


# TODO Print report by writing report. How much resources it has left
def print_report():
    for resource in resources.keys():
        if resource == "water":
            print(f"{resource.capitalize()} {resources[resource]}ml")
        elif resource == "milk":
            print(f"{resource.capitalize()} {resources[resource]}ml")
        elif resource == "coffee":
            print(f"{resource.capitalize()} {resources[resource]}g")
        elif resource == "money":
            print(f"{resource.capitalize()} ${resources[resource]}")
# TODO Check if there are sufficient resources within the machine.


# TODO Process coins.
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    while True:
        try:
            total = int(input("how many quarters?: ")) * 0.25
            total += int(input("how many dimes?: ")) * 0.1
            total += int(input("how many nickles?: ")) * 0.05
            total += int(input("how many pennies?: ")) * 0.01
            return total
        except ValueError:
            continue
        except TypeError:
            continue


# TODO Check if transaction is successfull and calculate refund.
def payment_check(payment):
    while True:
        try:
            if payment >= MENU[command]["cost"]:
                return True, print("Payment successfull")
            else:
                return False, print("Insufficient funds.\nPayment refunded.")
        except Error:
            continue


# TODO If successfull amount of coins, create the chosen drink and update
# the resources
def resource_check(order):
    if order == "espresso":
        if resources["water"] >= MENU[order]["ingredients"]["water"] and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            return True
        else:
            return False
    else:
        if resources["water"] >= MENU[order]["ingredients"]["water"] and resources["milk"] >= MENU[order]["ingredients"]["milk"] and resources["coffee"] >= MENU[order]["ingredients"]["coffee"]:
            return True
        else:
            return False


def update_resources(order):
    if order == "espresso":
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU[order]["cost"]
    else:
        resources["water"] -= MENU[order]["ingredients"]["water"]
        resources["milk"] -= MENU[order]["ingredients"]["milk"]
        resources["coffee"] -= MENU[order]["ingredients"]["coffee"]
        resources["money"] = resources["money"] + MENU[order]["cost"]

#    for key in MENU.keys():
#        if key == "espresso":


def process_order(order, payment):
    if resource_check(order) is True:
        customer_payment = payment - MENU[command]["cost"]
        if customer_payment > 0:
            print(f"Refunding ${customer_payment}")
        update_resources(order)
        print(f"Creating {order}")
    else:
        print("Insufficient resources available. Cancelling order.")
        print(f"Refunding ${payment}")


is_on = True

while is_on:
    command = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if command == "off":
        is_on = False
        break
    elif command == "report":
        print_report()
    else:
        if resource_check(command) is True:
            customer_payment = process_coins()
            valid_order = payment_check(customer_payment)[0]
        else:
            print(f"Not enough resources to create your {command}. Please choose something else.")
            customer_payment = 0
        
        if valid_order is True:
            process_order(command, customer_payment)
