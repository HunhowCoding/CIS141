# this code counts the number of times the word "Olympic" appears in a list of words
words = ["Olympic", "games", "Olympic", "torch", "Olympic", "medal", "winner"]
count = 0

# calculate how many times the word "Olympic" appears in the list, and add it to the counter
for word in words:
    if word == "Olympic":
        count += 1

print("The word 'Olympic' appears", count, "times in the list.")
