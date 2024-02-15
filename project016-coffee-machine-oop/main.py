from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_mcn = CoffeeMaker()
money_mcn = MoneyMachine()
coffee_menu = Menu()

is_off = False

while not is_off:
    drink = input(f'What would you like? {coffee_menu.get_items()}:').lower()
    if drink == 'off':
        print("Machine is turned off.")
        is_off = True
    elif drink == 'report':
        coffee_mcn.report()
        money_mcn.report()
    else:
        order = coffee_menu.find_drink(drink)
        if order is not None:
            if coffee_mcn.is_resource_sufficient(order):
                print(f"{order.name.title()}'s price = ${order.cost:.2f}")
                try:
                    if money_mcn.make_payment(order.cost):
                        coffee_mcn.make_coffee(order)
                except ValueError:
                    print("Coin is not valid")
