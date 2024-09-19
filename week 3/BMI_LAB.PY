def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

# Input values
weight = 68  
height = 175  
bmi = calculate_bmi(weight, height)
print(bmi)



