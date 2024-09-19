"""
Assessment 2: Python Functions
Author : AMAN KUMAR
Student ID: 20240054
"""
# Information about the staff members
def staff_info():
    Date = input("Enter the Date:")
    Staff_ID = (input("Enter your Staff ID:"))
    Staff_Name = input("Enter your Name:")
    Unique_ID = 10000            #given unique id
    Requisition_ID = Unique_ID + 1
    print(f"Printing Staff Information: \nDate:{Date} \nStaff ID:{Staff_ID} \nStaff Name:{Staff_Name} \nRequisition ID: {Requisition_ID}")
    return Date, Staff_ID, Staff_Name, Requisition_ID
staff_info()