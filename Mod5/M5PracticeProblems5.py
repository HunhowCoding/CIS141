# This code continuously prompts the user to enter a number, stopping when the user enters zero.
while True:
    num = int(input("Enter a number: "))
    # Check if the number is zero to stop the loop
    if num == 0:
        print("Stopping the loop.")
        break
    print(num)