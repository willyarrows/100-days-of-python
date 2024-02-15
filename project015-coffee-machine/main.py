MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

QUARTER = 0.25
DIME = 0.10
NICKLE = 0.05
PENNY = 0.01

money = 0


def print_report():
    print(f"Water : {resources['water']}ml")
    print(f"Milk : {resources['milk']}ml")
    print(f"Coffee : {resources['coffee']}g")
    print(f"Money : S{money}")


def check_resource(coffee):
    global resources

    if coffee not in list(MENU.keys()):
        print(f"Sorry, {coffee} is not available in our menu")
        return False
    else:
        if resources['water'] < MENU[coffee]['ingredients']['water']:
            print("Sorry, there is not enough water")
            return False
        elif resources['coffee'] < MENU[coffee]['ingredients']['coffee']:
            print("Sorry, there is not enough coffee")
            return False
        elif coffee != 'espresso' and resources['milk'] < MENU[coffee]['ingredients']['milk']:
            print("Sorry, there is not enough milk")
            return False
        else:
            return True


def process_coins(quarters=0.0, dimes=0.0, nickles=0.0, pennies=0.0):
    total_money = (quarters * QUARTER) + (dimes * DIME) + (nickles * NICKLE) + (pennies * PENNY)
    return total_money


def check_transaction(received_payment, coffee):
    global money
    coffee_price = MENU[coffee]['cost']
    print(f"Total Payment = ${received_payment:.2f}")
    if received_payment < coffee_price:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif received_payment > coffee_price:
        change = received_payment - coffee_price
        print(f"Here is ${change:.2f} dollars in change.")
        money += coffee_price
        return True
    else:
        money += coffee_price
        return True


def make_coffee(coffee):
    global resources
    resources['water'] -= MENU[coffee]['ingredients']['water']
    resources['coffee'] -= MENU[coffee]['ingredients']['coffee']
    if coffee != 'espresso':
        resources['milk'] -= MENU[coffee]['ingredients']['milk']

    print(f"Here is your {coffee.title()} ☕. Enjoy!”")


is_off = False

while not is_off:
    command = input('What would you like? (espresso/latte/cappuccino):').lower()
    if command == 'off':
        print("Machine is turned off.")
        is_off = True
    elif command == 'report':
        print_report()
    else:
        if check_resource(command):
            print(f"{command.title()}'s price = ${MENU[command]['cost']:.2f}")
            print("Please insert coins.")
            payment = 0
            try:
                coin_quarters = float(input("how many quarters ? : "))
                coin_dimes = float(input("how many dimes ? : "))
                coin_nickles = float(input("how many nickles ? : "))
                coin_pennies = float(input("how many pennies ? : "))
                payment = process_coins(coin_quarters, coin_dimes, coin_nickles, coin_pennies)
            except ValueError:
                print("Coin is not valid")

            if check_transaction(payment, command):
                make_coffee(command)
