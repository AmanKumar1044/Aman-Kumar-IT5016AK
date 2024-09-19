"""
shopping list
author = aman kumar
"""
def get_shoppinglist():
    shopping_list = [] #it is a list that stores value
    total_price = 0
    while True:
        item = input("enter the name of the item (or type'done' to finish):")
        if item.lower() == 'done':
            break

        try:
            price = float(input(f"enter the price of '{item}':"))
            shopping_list.append((item,price))  
            total_price += price
        except ValueError:
            print("invalid input. please enter a numeric value for the price.")

    return shopping_list, total_price

def main():
    print("Welcome to the shopping list program")
    shopping_list,total_price = get_shoppinglist()

    if not shopping_list:
        print("no item were entered")

    else:
        print("\nshopping list:")

        for item, price in shopping_list:
            print(f"{item},${price:.2f}")
        print(f"\nTotal Price: ${total_price:.2f}")



main()    