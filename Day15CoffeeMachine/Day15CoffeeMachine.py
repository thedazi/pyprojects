from Day15art import logo

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
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

profit = 0

#sufficient resource
def sufficient_resource(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"There is insufficient {item}")
            return False
    return True

# print(sufficient_resource(MENU["espresso"]["ingredients"]))

#money transaction
def insert_coins():
    print("Please insert coins")
    quarters = int(input("How many quarters to insert: "))
    dimes = int(input("How many dimes to insert: "))
    nickels = int(input("How many nickels to insert: "))
    penny = int(input("How many pennies to insert: "))
    return round((quarters*0.25)+(dimes*0.10)+(nickels*0.05)+(penny*0.01), 3)

def sufficient_coin(received_coins, order):
    price = order['cost']
    if received_coins < price:
        print("Sorry, that amount is insufficient.")
        return False
    elif received_coins >= order['cost']:
        change = received_coins - order['cost']
        print(f"Your change is {change}")
        global profit
        profit =+ price
        return True

def order_drink(user_order):
    return MENU[user_order]

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️.")

def coffee_machine():
    machine_on = True
    global profit
    while machine_on == True:

        user_order = input("What would you like to order? (espresso, latte, or cappuccino): ").lower()
        if user_order == "off":
            machine_on = False

        elif user_order == "report":
            print(f"There is {resources['water']} water, {resources['milk']} milk, and {resources['coffee']} coffee.")
            print(f"There is ${profit} in the machine.")

        else:
            order = order_drink(user_order)
            if sufficient_resource(order["ingredients"]) == True:
                price = order['cost']
                print(f"That will be ${price}.")
                user_payment = insert_coins()
                if sufficient_coin(user_payment, order):
                    make_coffee(user_order, order["ingredients"])



print(logo)
coffee_machine()