# open, read and print each tip
with open("Mod8/gardening_tips.txt", "r") as file:
    for line in file:
        print(line.strip())