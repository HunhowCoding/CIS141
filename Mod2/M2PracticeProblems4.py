# wait we're not supposed to use f-strings on the previous questions?
# anyways i chose to guess the age to cover jan 1 2025 to jan 1 2026

dobyear = int(input("enter your birth year: "))

# setting the year values 2024 and 2025 may seem counterintuitive, trust me
firvalage = 2024 - dobyear
secvalyage = 2025 - dobyear

# print guess age
print(f"you are between the age of {firvalage} and {secvalyage}")
