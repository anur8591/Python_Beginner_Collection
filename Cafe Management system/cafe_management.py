menu = {
    "pizza": 250,
    "burger": 150,
    "pasta": 200,
    "salad": 180,
    "coffee": 100
}

# order
print("Welcome To Python Cafe")
print("Menu:\n pizza = 250\n burger = 150\n pasta = 200\n salad = 180\n coffee = 100")

# price calculation
total = 0

# input from user 
item = input("Enter the item you want to order: ")

# check item is available in menu or not 
if item in menu:
    total += menu[item]
    print(f"{item} added to your order. price: {menu[item]}")
else:
    print(f"sorry, {item} is not available in the menu, please choose from the menu")

another_order = input("Do you want to order another item? (yes/no):")
if another_order.lower() == 'yes':
    item = input("Enter the another item you want to order: ")
    if item in menu:
        total += menu[item]
        print(f"{item} added to your order. price: {menu[item]}")
    else:
        print(f"sorry, {item} is not available in the menu, please choose from the menu")
    print(f"Your total bill is: {total}")
else:
    print("please enter \"yes\" or \"no\" only\n")
    print("Try again to place your order")