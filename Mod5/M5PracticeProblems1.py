# Prompt the user for a positive integer
n = int(input("Enter a positive integer: "))

# Ensure the input is positive
while n <= 0:
    print("Please enter a positive integer.")
    n = int(input("Enter a positive integer: "))

# Initialize variables
total_sum = 0
current = 1

# Use a while loop to calculate the sum
while current <= n:
    total_sum += current
    current += 1

# Print the final sum
print(f"The sum of integers from 1 to {n} is {total_sum}.")