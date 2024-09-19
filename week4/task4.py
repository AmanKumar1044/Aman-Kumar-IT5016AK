def collect_user_information():
        counter_value = 5000
        return counter_value+1
    
user_name = input("ENTER THE NAME OF THE STUDENT:")
user_age = input("ENTER THE AGE OF THE USER:")
user_email = input("ENTER THE EMAIL OF THE USER:")
unique_id_counter=collect_user_information()
print("user information:")


def  calculate_total_amount():
    total_amount = float(input("enter the amount"))
    while True:
        price_input = input("enter the name of the item(or type 'finish' to end ):")
        
        if price_input.lower == 'finish':
            break

        try:

            price = float(input(f"enter the price of the item{price_input}"))
            total_amount += price
        except ValueError:
            print("Invalid input, please enter a value number.")
 
    

def categorize_request():
    tot_amount  =  float(input("enter the total amount: $"))
    if tot_amount< 150:
        category = "Low"
        recommendation = "Proceed with standard processing"
    else:
        category =" high"
        recommendation = "Review for ptotential discount"


def create_detailed_report():

    print("Detiled Report")
    total_amount = calculate_total_amount
    tot_amount= categorize_request
    print(f"Unique ID:{collect_user_information(unique_id_counter)} ")
    print(f"Name: {collect_user_information(user_name)}")
    print(f"Age:{collect_user_information(user_age)}")
    print(f"Email:{collect_user_information(user_email)}")
    print((f"Total Amount : ${calculate_total_amount}{total_amount: .2f}"))
    print(f"category:{categorize_request(tot_amount)}")
    print(f"Recommendation:{categorize_request(tot_amount)}")

create_detailed_report()
