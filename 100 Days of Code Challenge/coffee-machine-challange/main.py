from data import MENU
# 3 different MENU, each with their unique amount of ingredients
print(MENU['espresso']['cost'])

# TODO Print report by writing report. How much resources it has left

# TODO Check if there are sufficient resources within the machine.

# TODO Process coins.


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

# TODO Check if transaction is successfull and calculate refund.

# TODO If successfull amount of coins, create the chosen drink and update
# the resources
