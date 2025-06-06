# this code squares each value in a list of numbers
numbers = [1, 3, 4, 7, 10]
squared_numbers = []

# square each value and add them to the squared_numbers list
for num in numbers:
    squared_numbers.append(num ** 2)

print("Squared numbers:", squared_numbers)