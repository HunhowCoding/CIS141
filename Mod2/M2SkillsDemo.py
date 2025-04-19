# finding intial values
name = input("What is your name? ")
cost = float(input("How much was the bill? $"))
nopeople = float(input("How many people are splitting the bill tonight? "))

# calculate the values
costsplit = cost / nopeople
roundedcost = round(costsplit, 2)

# print calculation
print(f"{name}, each person shall spend ${roundedcost}")
print(f"April fools! You're paying the tab entirely.")