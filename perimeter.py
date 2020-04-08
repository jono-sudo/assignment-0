# Calculates the total fence required to fence of the perimeter of the give diagram
# Jonathan Henderson
# HNDAND010
# 8 April 2020

# Prompt user for inputs:
w1 = eval(input("Enter width 1: "))
h1 = eval(input("Enter height 1: "))
w2 = eval(input("Enter width 2: "))
h2 = eval(input("Enter height 2: "))
price_per_metre = eval(input("Enter price per metre: "))

# Calculate perimeter:
perimeter = h1 + w1*2 + w2*2 + h2 + (h1 - h2)
total_price = perimeter*price_per_metre

#Display outputs:
print("The total fence required =",perimeter,"metres")
print("The total price = R",total_price)