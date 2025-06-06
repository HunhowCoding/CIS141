# this code calculates the sum of even numbers in a given list
numbers = [2, 7, 15, 32, 59, 68]
even_sum = 0

# calculate which values are even and add them to the sum
for num in numbers:
    if num % 2 == 0:
        even_sum += num

# and print the result
print("Sum of even numbers:", even_sum)
