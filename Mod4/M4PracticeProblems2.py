# Ask for input from the user for daylight value
daylight = int(input("Enter the daylight value: "))

# Calculate and print
if daylight < 8:
    print("Headlights on.")
else:
    print("Headlights off.")