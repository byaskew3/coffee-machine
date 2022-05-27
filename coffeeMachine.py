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

money = 0

def payment_process():
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    quarters *= 0.25
    dimes = int(input('How many dimes?: '))
    dimes *= 0.10
    nickles = int(input('How many nickles?: '))
    nickles *= 0.05
    pennies = int(input('How many pennies?: '))
    pennies *= 0.01

    total = quarters + dimes + nickles + pennies
    return total

def get_espresso():
    total = payment_process()
    espresso_cost = MENU['espresso']['cost']
    if total >= espresso_cost:
        if resources['water'] >= MENU['espresso']['ingredients']['water']:
            resources['water'] -= MENU['espresso']['ingredients']['water']
            if resources['coffee'] >= MENU['espresso']['ingredients']['coffee']:
                resources['coffee'] -= MENU['espresso']['ingredients']['coffee']
                total -= espresso_cost
                print(f'Here is ${total:.2f} in change')
                print('Here is your espresso ☕ Enjoy!')
            else:
                print('Sorry there is not enough coffee.')
        else:
            print('Sorry there is not enough water.')
    else:
        print('Sorry that\'s not enough money. Money refunded')

def get_latte():
    total = payment_process()
    latte_cost = MENU['latte']['cost']
    if total >= latte_cost:
        if resources['water'] >= MENU['latte']['ingredients']['water']:
            resources['water'] -= MENU['latte']['ingredients']['water']
            if resources['milk'] >= MENU['latte']['ingredients']['milk']:
                resources['milk'] -= MENU['latte']['ingredients']['milk']
                if resources['coffee'] >= MENU['latte']['ingredients']['coffee']:
                    resources['coffee'] -= MENU['latte']['ingredients']['coffee']
                    total -= latte_cost
                    print(f'Here is ${total:.2f} in change')
                    print('Here is your latte ☕ Enjoy!')
                else:
                    print('Sorry there is not enough coffee.')
            else:
                print('Sorry there is not enough milk.')
        else:
            print('Sorry there is not enough water.')
    else:
        print('Sorry that\'s not enough money. Money refunded')

def get_cappuccino():
    total = payment_process()
    cappuccino_cost = MENU['cappuccino']['cost']
    if total >= cappuccino_cost:
        if resources['water'] >= MENU['cappuccino']['ingredients']['water']:
            resources['water'] -= MENU['cappuccino']['ingredients']['water']
            if resources['milk'] >= MENU['cappuccino']['ingredients']['milk']:
                resources['milk'] -= MENU['cappuccino']['ingredients']['milk']
                if resources['coffee'] >= MENU['cappuccino']['ingredients']['coffee']:
                    resources['coffee'] -= MENU['cappuccino']['ingredients']['coffee']
                    total -= cappuccino_cost
                    print(f'Here is ${total:.2f} in change')
                    print('Here is your cappuccino ☕ Enjoy!')
                else:
                    print('Sorry there is not enough coffee.')
            else:
                print('Sorry there is not enough milk.')
        else:
            print('Sorry there is not enough water.')
    else:
        print('Sorry that\'s not enough money. Money refunded')

def get_report():
    print(f'Water: {resources["water"]}ml')
    print(f'Milk: {resources["milk"]}ml')
    print(f'Coffee: {resources["coffee"]}g')
    print(f'Money: ${money}')

def runner():
    user_choice = input('What would you like? (espresso/latte/cappuccino) ').lower()
    if user_choice == 'espresso':
        get_espresso()
    elif user_choice == 'latte':
        get_latte()
    elif user_choice == 'cappuccino':
        get_cappuccino()
    elif user_choice == 'report':
        get_report()
    else:
        print('Please select a valid option.')
        runner()

runner()
