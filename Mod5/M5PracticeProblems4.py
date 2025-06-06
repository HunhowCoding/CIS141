# This code prints a multiplication table from 1 to 5.
for i in range(1, 6):
    for j in range(1, 6):
        # Print the product of i and j, followed by a tab
        print(i * j, end='\t')
    print()
