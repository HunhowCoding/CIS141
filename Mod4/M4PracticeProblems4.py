# get age from user
age = int(input("Enter your age: "))

# determine ESRB rating acceptability
if age < 13:
    print("You can see G rated movies.")
elif age < 18:
    print("You can see G and PG-13 rated movies.")
elif age < 19:
    print("You can see G, PG-13, and R rated movies.")