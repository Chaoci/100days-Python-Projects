from resource import resources, MENU

def logo():
    logo1 ="""
    
   ____       __  __          /\/|        
  / ___|___  / _|/ _| ___  __|/\/         
 | |   / _ \| |_| |_ / _ \/ _ \           
 | |__| (_) |  _|  _|  __/  __/           
  \____\___/|_| |_| _\___|\___|       /\/|
 |  \/  | __ _  ___| |__ (_)_ __   __|/\/ 
 | |\/| |/ _` |/ __| '_ \| | '_ \ / _ \   
 | |  | | (_| | (__| | | | | | | |  __/   
 |_|  |_|\__,_|\___|_| |_|_|_| |_|\___|   
    """
    print(logo1)
# TODO:
#  1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
# a. Check the user’s input to decide what to do next.
# b. The prompt should show every time action has completed, e.g. once the drink is
# dispensed. The prompt should show again to serve the next customer.
def machine():
    keep_asking = True
    coffee = input("What would you like? (espresso/latte/cappuccino)")
    check_resource(coffee)
    profit = 0
    if coffee == "report":
        for element in resources:
            if element == "water" or element == "milk":
                unit = 'ml'
            elif element == "coffee":
                unit = "g"
            print(f"{element}:{resources[element]}{unit}")
        print(f"Money:${profit}")
    elif coffee == "espresso":
            coin(coffee)
            profit += 1.5 
    elif coffee == "latte":
            coin(coffee)
            profit += 2.5
    elif coffee == "cappuccino":
            coin(coffee)
            profit += 3.0
    elif coffee == "off":
        keep_asking = False
        
    while keep_asking:
        coffee = input("What would you like? (espresso/latte/cappuccino)")
        check_enough(coffee)
        if  check_enough(coffee) == 1:
            print("Sorry there is not enough water.")
            break
        elif check_enough == 2:
            print("Sorry there is not enough milk.")
            break
        elif check_enough == 3:
            print("Sorry there is not enough coffee.")
            break
        check_resource(coffee)
        if coffee == "off":
            keep_asking = False
            break
        if coffee == "report":
            for element in resources:
                if element == "water" or element == "milk":
                    unit = 'ml'
                elif element == "coffee":
                    unit = "g"
                print(f"{element}:{resources[element]}{unit}")
            print(f"Money:${profit}")
        elif coffee == "espresso":
            coin(coffee)
            profit += 1.5 
        elif coffee == "latte":
            coin(coffee)
            profit += 2.5
        elif coffee == "cappuccino":
            coin(coffee)
            profit += 3.0


def coin(coffee):
    print("Please insert coins.")
    # quarter = 0.25 dime = 0.10 nickle = 0.05 penny = 0.01
    quarters = int(input("How many quarters?:"))
    dimes = int(input("How many dimes?:"))
    nickles = int(input("How many nickles?:"))
    pennies = int(input("How many pennies?:"))
    total_insert = (quarters*0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
        
    if coffee == "espresso":
        price = 1.5
        res = round(float(total_insert - price), 2)
        while res < 0:
            lack = abs(res - 0)
            print(f"Please insert enough coin. lack ${lack}")
            quarters1 = int(input("How many quarters?:"))
            dimes1 = int(input("How many dimes?:"))
            nickles1 = int(input("How many nickles?:"))
            pennies1 = int(input("How many pennies?:"))
            total_insert1 = (quarters1*0.25) + (dimes1 * 0.10) + (nickles1 * 0.05) + (pennies1 * 0.01)
            res = round((total_insert1 - lack), 2)
        print(f"Here is ${res} in change.")
        print(f"Here is your {coffee} Enjoy!")
    elif coffee == "latte":
        price = 2.5
        res = round(float(total_insert - price), 2)
        while res < 0:
            lack = abs(res - 0)
            print(f"Please insert enough coin. lack ${lack}")
            quarters1 = int(input("How many quarters?:"))
            dimes1 = int(input("How many dimes?:"))
            nickles1 = int(input("How many nickles?:"))
            pennies1 = int(input("How many pennies?:"))
            total_insert1 = (quarters1*0.25) + (dimes1 * 0.10) + (nickles1 * 0.05) + (pennies1 * 0.01)
            res = total_insert1 - lack
        print(f"Here is ${res} in change.")
        print(f"Here is your {coffee} Enjoy!")
    elif coffee == "cappuccino":
        price = 3.0
        res = round(float(total_insert - price), 2)
        while res < 0:
            lack = abs(res - 0)
            print(f"Please insert enough coin. lack ${lack}")
            quarters1 = int(input("How many quarters?:"))
            dimes1 = int(input("How many dimes?:"))
            nickles1 = int(input("How many nickles?:"))
            pennies1 = int(input("How many pennies?:"))
            total_insert1 = (quarters1*0.25) + (dimes1 * 0.10) + (nickles1 * 0.05) + (pennies1 * 0.01)
            res = total_insert1 - lack
        print(f"Here is ${res} in change.")
        print(f"Here is your {coffee} Enjoy!")

def check_resource(coffee):
    water  = resources['water']
    milk = resources['milk']
    coffee_bean = resources['coffee']
    if coffee == 'espresso':
        use_milk = 0
        use_water = MENU[coffee]['ingredients']['water']
        use_coffee = MENU[coffee]['ingredients']['coffee']
    elif coffee =='latte' or coffee =='cappuccino':
        use_water = MENU[coffee]['ingredients']['water']
        use_coffee = MENU[coffee]['ingredients']['coffee']
        use_milk = MENU[coffee]['ingredients']['milk']
    elif coffee == 'report':
        use_water = 0
        use_milk = 0
        use_coffee = 0
    elif coffee == 'off':
        use_water = 0
        use_milk = 0
        use_coffee = 0
    
    rest_water = water -  use_water
    rest_milk = milk - use_milk
    rest_coffee_bean = coffee_bean - use_coffee
    
    resources['water'] = rest_water
    resources['milk'] = rest_milk
    resources['coffee'] = rest_coffee_bean
    return resources

def check_enough(coffee):
    water  = resources['water']
    milk = resources['milk']
    coffee_bean = resources['coffee']
    if coffee == 'espresso':
        use_milk = 0
        use_water = MENU[coffee]['ingredients']['water']
        use_coffee = MENU[coffee]['ingredients']['coffee']
    elif coffee =='latte' or coffee =='cappuccino':
        use_water = MENU[coffee]['ingredients']['water']
        use_coffee = MENU[coffee]['ingredients']['coffee']
        use_milk = MENU[coffee]['ingredients']['milk']
    elif coffee == 'report':
        use_water = 0
        use_milk = 0
        use_coffee = 0
    elif coffee == 'off':
        use_water = 0
        use_milk = 0
        use_coffee = 0
    
    res1 = water - use_water
    res2 = milk - use_milk
    res3 = coffee_bean - use_coffee
    if res1< 0:
        coffee_left = 1
        return coffee_left
    if res2< 0:
        coffee_left = 2
        return coffee_left
    if res3< 0:
        coffee_left = 3
        return coffee_left
logo()
machine()
# TODO:
# 2.Turn off the Coffee Machine by entering “off” to the prompt.
# a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
# the machine. Your code should end execution when this happens.


# TODO:
# 3. Print report.
# a. When the user enters “report” to the prompt, a report should be generated that shows
# the current resource values. e.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5

# TODO:
# 4. Check resources sufficient?
# a. When the user chooses a drink, the program should check if there are enough
# resources to make that drink.
# b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
# not continue to make the drink but print: “Sorry there is not enough water.”
# c. The same should happen if another resource is depleted, e.g. milk or coffee.

# TODO:
# 5. Process coins.
# a. If there are sufficient resources to make the drink selected, then the program should
# prompt the user to insert coins.
# b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
# c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
# pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52

# TODO:
# 6. Check transaction successful?
# a. Check that the user has inserted enough money to purchase the drink they selected.
# E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
# program should say “Sorry that's not enough money. Money refunded.”.
# b. But if the user has inserted enough money, then the cost of the drink gets added to the
# machine as the profit and this will be reflected the next time “report” is triggered. E.g.
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# c. If the user has inserted too much money, the machine should offer change.
# E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
# places.

# TODO:
# 7. Make Coffee.
# a. If the transaction is successful and there are enough resources to make the drink the
# user selected, then the ingredients to make the drink should be deducted from the
# coffee machine resources.
# E.g. report before purchasing latte:
# Water: 300ml
# Milk: 200ml
# Coffee: 100g
# Money: $0
# Report after purchasing latte:
# Water: 100ml
# Milk: 50ml
# Coffee: 76g
# Money: $2.5
# b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If latte was their choice of drink