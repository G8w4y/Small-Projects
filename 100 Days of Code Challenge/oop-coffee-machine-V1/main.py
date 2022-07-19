from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
transaction_handler = MoneyMachine()

is_on = True

while is_on:
    order = input(f"What would you like to order? {menu.get_items()}")
    if order == "off":
        is_on = False    
    elif order == "report":
        coffee_machine.report()
        transaction_handler.report()
    else:
        coffee_drink = menu.find_drink(order)
        if coffee_machine.is_resource_sufficient(coffee_drink) is True:
            if transaction_handler.make_payment(coffee_drink.cost) is True:
                coffee_machine.make_coffee(coffee_drink)
