# this script reads a text file containing a bunch of yeas and nays, counts the occurrences of each, and prints the results
with open("Mod8/poll.txt", "r") as file:
    content = file.read().lower()  # read the file and convert to lowercase

# count the occurrences of 'yea' and 'nay'
nay_count = content.count("nay")
yea_count = content.count("yea")

# print the results
print(f"Yea: {yea_count}")
print(f"Nay: {nay_count}")