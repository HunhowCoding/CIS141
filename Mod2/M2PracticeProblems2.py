# provides inputtable values to calculate
# also provide note about what to NOT type down
print("Simple Calculator! Input 2 values for them to be added, subtracted, multiplied, and divided.")
print("NOTE: Do not set the second value to zero, this will crash the program!")
value1 = float(input("first value: "))
value2 = float(input("second value: "))

# calculate and assign to variable
add = value1 + value2
sub = value1 - value2
mult = value1 * value2
div = value1 / value2

# print results
print(f"addition: {add}")
print(f"subtraction: {sub}")
print(f"multiplication: {mult}")
print(f"division: {div}")