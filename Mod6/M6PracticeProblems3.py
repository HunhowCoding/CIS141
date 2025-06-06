# this code counts the number of letters in each string, and filters out strings longer than three characters
words = ["cat", "elephant", "dog", "lion", "ant", "tiger"]
filtered_words = []

# filter out strings longer than three characters
for word in words:
    if len(word) > 3:
        # adds the filtered word to the filtered_words list to be printed later
        filtered_words.append(word)

print("Strings longer than three characters:", filtered_words)