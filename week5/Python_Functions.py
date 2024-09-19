"""
Assessment 2: Python Functions
Author : AMAN KUMAR
Student ID: 20240054
"""
def staff_info():
    Date = input("Enter the Date:")
    Staff_ID = (input("Enter your Staff ID:"))
    Staff_Name = input("Enter your Name:")
    Unique_ID = 10000
    Requisition_ID = Unique_ID + 1
    print(f"Printing Staff Information: \nDate:{Date} \nStaff ID:{Staff_ID} \nStaff Name:{Staff_Name} \nRequisition ID: {Requisition_ID}")
    return Date, Staff_ID, Staff_Name, Requisition_ID


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
    return Total_Value


def requisition_approval(requisitions_total):
    Status = "Approved"
    if Total_Value < 500:
        approval_reference_number = ((Staff_ID)+"001")
    else:
        print("Status: Pending")
    print(f"Total: {Total_Value} \nStatus: {Status} \nApproval Reference Number:{approval_reference_number}")
    return Total_Value, Status, approval_reference_number
requisition_approval(requisitions_total)

def display_requisitions(Date, Requisition_ID, Staff_ID, Staff_Name, Total_Value, Status, approval_reference_number):
    print("Printing Requisitions:")
    print(f"Date:{Date}")
    print(f"Requisition ID:{Requisition_ID}")
    print(f"Staff ID:{Staff_ID}")
    print(f"Staff Name:{Staff_Name}")
    print(f"Total:{Total_Value}")
    print(f"Status:{Status}")
    print(f"Approval Reference Number:{approval_reference_number}")
display_requisitions(Date, Requisition_ID, Staff_ID, Staff_Name, Total_Value, Status, approval_reference_number)

def main():
    Date, Staff_ID, Staff_Name, Requisition_ID = staff_info()
    Total_Value = requisitions_total()
    Total_Value, Status, approval_reference_number = requisition_approval(Total_Value)
    display_requisitions(Date, Requisition_ID, Staff_ID, Staff_Name, Total_Value, Status, approval_reference_number)
main()



