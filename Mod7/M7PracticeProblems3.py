# this function calculates the weakness and strength of a type against another type
def type_advantage(attacker, defender):
    advantages = {
        "fire": ["grass"],
        "water": ["fire"],
        "grass": [],
    }
    disadvantages = {
        "fire": ["water"],
        "water": [],
        "grass": ["fire"],
    }
    if attacker in advantages and defender in advantages[attacker]:
        return "Super Effective"
    elif attacker in disadvantages and defender in disadvantages[attacker]:
        return "Not Very Effective"
    else:
        return "Neutral"
# example usage:
print(type_advantage("water", "fire")) # "super effective"
print(type_advantage("fire", "water")) # "not very effective"
print(type_advantage("water", "grass")) # "neutral"