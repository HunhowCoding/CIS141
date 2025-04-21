# importing math library, i need square rooting
import math

# find side lengths
side1 = float(input("input first side length: "))
side2 = float(input("input second side length: "))
side3 = float(input("input third side length: "))

# calculate semiperimeter (spm)
spm = (side1 + side2 + side3) / 2

# calculate area with herson's formula
area = (math.sqrt(spm * (spm - side1) * (spm - side2) * (spm - side3)))

# print text
print(f"area: {area}")