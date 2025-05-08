# Get user input for order total
ordertotal = int(input("Enter the order total: $"))

# Determine total cost
if ordertotal >= 50:
    print(f"Total order will be ${ordertotal} with free shipping.")
else:
    ordertotal += 5
    print(f"Total order will be ${ordertotal} after shipping.")