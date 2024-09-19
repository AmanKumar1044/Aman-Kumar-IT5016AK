def calculate_total_amount():
    total_amount = 0.0
    while True:
        price_input = input("enter the name of the item(or type 'finish' to end ):")
        
        if price_input.lower == 'finish':
            break

        try:

            price = float(input(f"enter the price of the item{price_input}"))
            total_amount += price
        except ValueError:
            print("Invalid input, please enter a value number.")
    print(f"The total amount is : ${total_amount: .2f}") 
def main():
    calculate_total_amount()
main()       


