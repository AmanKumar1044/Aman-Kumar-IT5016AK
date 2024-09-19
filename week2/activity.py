item1 = float(input("enter the price for item1:"))
item2 = float(input("enter the price for item2:"))
item3 = float(input("enter the price for item3:"))


subtotal = item1 + item2 + item3
salestax = subtotal * 0.15
total = subtotal + salestax
print("your purchase total is $",total,sep="")