# this code seperates even and odd numbers from a list into two different lists
numbers = [1, 2, 3, 4, 5]
even_num = []
odd_num = []

# calculate which values are even and odd, and add them to the respective lists
for num in numbers:
    if num % 2 == 0:
        even_num.append(num)
    if num % 2 != 0:
        odd_num.append(num)

print("Even numbers:", even_num)
print("Odd numbers:", odd_num)