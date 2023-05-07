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
            "water": 2500,
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
TOTAL_MONEY = 0


# TODO: 1.Print report of all coffee machine resources
def print_report():
    """Print report of all coffee machine resources"""
    print(
        f"Water: {resources['water']}ml \nMilk: {resources['milk']}ml \nCoffee: {resources['coffee']}g "
        f"\nMoney: ${TOTAL_MONEY}")


# TODO: 2.Check resources sufficient
def check_resources(beverages):
    """Check resources sufficient"""
    result = True
    if beverages not in MENU:
        return "beverages not support"
    ingredient = MENU[beverages]['ingredients']
    for i in ingredient:
        if ingredient[i] > resources[i]:
            result = False
    return result


# TODO: 3.Process coins.
def check_coins(beverages):
    """Process coins"""
    beverages_cost = MENU[beverages]['cost']
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))
    total = quarters * 0.25 + dimes * 0.1 + nickles * 0.05 + pennies * 0.01
    if total > beverages_cost:
        return total - beverages_cost
    else:
        return -1


# TODO: 4.Check transaction successful?
# TODO: 5.Make Coffee.
def coffe_machine():
    end_session = False
    while not end_session:
        beverages = input("What would you like? (espresso/latte/cappuccino): ")
        if beverages == 'report':
            print_report()
        elif beverages == 'exit':
            end_session = True
        else:
            check_resource = check_resources(beverages)
            if check_resource:
                print("Please insert coins. ")
                check_coin = check_coins(beverages)
                if check_coin > -1:
                    global TOTAL_MONEY
                    TOTAL_MONEY += MENU[beverages]['cost']
                    print(f"Here is ${check_coin} in change. \nHere is your {beverages}. Enjoy!")
                else:
                    print(f"Sorry that's not enough money. Money refunded.")
                    coffe_machine()
            else:
                print("Not enough resources")


coffe_machine()
