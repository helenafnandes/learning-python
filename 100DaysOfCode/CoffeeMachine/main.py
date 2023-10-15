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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def check_resources(drink_name):
    ingredients_needed = MENU[drink_name]["ingredients"]
    for ingredient, amount in ingredients_needed.items():
        if resources[ingredient] < amount:
            print(f"Sorry, there is not enough {ingredient} for {drink_name}.")
            return False
    return True


def get_coins():
    total = 0
    total += int(input("How many quarters? ")) * 0.25
    total += int(input("How many dimes? ")) * 0.10
    total += int(input("How many nickles? ")) * 0.05
    total += int(input("How many pennies? ")) * 0.01
    return total


def check_transaction(money, desired_drink):
    if MENU[desired_drink]["cost"] <= money:
        if MENU[desired_drink]["cost"] < money:
            change = money - MENU[desired_drink]["cost"]
            print("Here's your change: $", change)
        global profit
        profit += money
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
    return False


def make_coffee(drink_name):
    ingredients_needed = MENU[drink_name]["ingredients"]
    for ingredient, amount in ingredients_needed.items():
        resources[ingredient] -= amount
    print(f"Here's your {drink_name}. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources["water"]}ml")
        print(f"Milk: {resources["milk"]}ml")
        print(f"Coffee: {resources["coffee"]}g")
        print(f"Money: {profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        if check_resources(choice):
            inserted_money = get_coins()
            if check_transaction(inserted_money, choice):
                make_coffee(choice)
