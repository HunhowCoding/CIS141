# this script reads a text file containing song lyrics, lets the user input words to count, and prints the count of each word in the lyrics

# this is to read the file
with open("Mod8/song_lyrics.txt", "r") as file:
    lyrics = file.read().lower()

# this is for the user to input words to be counted
count_words = []
for i in range(5):
    word = input(f"enter word {i + 1}: ").lower()
    count_words.append(word)

# this counts the occurrences of each word in the lyrics
word_counts = {}
for word in count_words:
    count = lyrics.split().count(word)
    word_counts[word] = count

# this prints the count of each word
print(word_counts)