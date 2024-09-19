"""
Assessment 2: Python Functions
Task:4
Author : AMAN KUMAR
Student ID: 20240054
"""
# collecting staff basic information and the total of his requisition
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
