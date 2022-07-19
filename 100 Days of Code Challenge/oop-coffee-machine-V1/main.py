from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_machine = CoffeeMaker()
transaction_handler = MoneyMachine()

#print(menu.__getattribute__(MenuItem(menu.find_drink("latte"))))

print(menu.__getattribute__(str(menu.find_drink("latte"))))

# transaction_handler.process_coins() make_payment
# is_on = True

# while is_on:
#     order = input(f"What would you like to order? {menu.get_items()}")
#     if order == "report":
#         coffee_machine.report()
#         transaction_handler.report()
#     else:
#         if coffee_machine.is_resource_sufficient(menu.find_drink(order)) is True:
#             if transaction_handler.make_payment(XXXXX) is True:
#                 coffee_machine.make_coffee(menu.find_drink(order))
