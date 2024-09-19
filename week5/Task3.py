"""
Assessment 2: Python Functions
Task:3
Author : AMAN KUMAR
Student ID: 20240054
"""
# function to make approval decisions 
def requisition_approval(requisitions_total):
    Status = "Approved"
    if Total_Value < 500:
        approval_reference_number = ((Staff_ID)+"001")
    else:
        print("Status: Pending")
    print(f"Total: {Total_Value} \nStatus: {Status} \nApproval Reference Number:{approval_reference_number}")
    return Total_Value, Status, approval_reference_number
requisition_approval(requisitions_total)