# this function calculates the ferry fare based on age and vehicle type
def ferry_fare(age, vehicle):
    if age < 18:
        return 0.0  # Free for passangers under 18
    
    elif age <= 64:
        if vehicle == 'walking':
            return 10.00  # Adult walk on fare
        elif vehicle == 'car':
            return 20.00  # Adult car fare
        
    else:  # age >= 65
        if vehicle == 'walking':
            return 5.00  # Senior walk on fare
        elif vehicle == 'car':
            return 15.00  # Senior car fare
        
# Example usage:
print("$",ferry_fare(17, 'walking'))  # Free for under 18
print("$",ferry_fare(30, 'car'))      # Adult car fare
print("$",ferry_fare(70, 'walking'))  # Senior walk on fare