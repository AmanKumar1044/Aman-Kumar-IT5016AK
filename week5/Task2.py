"""
Assessment 2: Python Functions
Task:2
Author : AMAN KUMAR
Student ID: 20240054
"""
# input the requisition items by the staff
def requisitions_total():
    Total_Value = 0
    while True:
        Requisition_items = input("Enter each item name (type 'finish' to end items):")
        if Requisition_items.lower() == "finish":
            break
        try:
            Price = float(input("Enter the price of the item:"))
            Total_Value += Price
        except ValueError:
            print("Invalid price")
    print(f"${Total_Value}")
    return Requisition_items, Total_Value
requisitions_total()