# This function determines the level based on experience points.
def level_up(experience):
    if experience < 100:
        return "Level 1"
    elif experience < 200:
        return "Level 2"
    elif experience < 300:
        return "Level 3"

# example usage
print(level_up(50))   # Output: Level 1
print(level_up(150))  # Output: Level 2
print(level_up(250))  # Output: Level 3