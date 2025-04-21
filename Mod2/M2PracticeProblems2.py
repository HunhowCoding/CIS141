# provides inputtable values to calculate
value1 = float(input("first value: "))
value2 = float(input("second value: "))

# calculate and assign to variable
add = value1 + value2
sub = value1 - value2
mult = value1 * value2

# division with additional stuff to prevent /0
if value2 !=0:
    div = value1 / value2
else:
    div = "undifined, divided by zero"

# print results
print(f"addition: {add}")
print(f"subtraction: {sub}")
print(f"multiplication: {mult}")
print(f"division: {div}")