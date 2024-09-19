def categorize_request():
    total_amount  =  float(input("enter the total amount: $"))
    if total_amount< 150:
        category = "Low"
        recommendation = "Proceed with standard processing"
    else:
        category =" high"
        recommendation = "Review for ptotential discount"
    print(f"category:{category}")
    print(f"recommendation:{recommendation}")
def main():
    categorize_request()
main()
