# this code calculates the number of vowels in a string, however i 
word = input("Count the number of vowels in: ")

count_vowels = "Count Vowels in a String"
def count_vowels(input):
    vowels = "aeiouAEIOU"
    count = 0
    
    # Loop through each character in the string
    for char in word:
        # Check if the character is a vowel
        if char in vowels:
            count += 1
            
    return count
print(f"The number of vowels in '{word}' is: {count_vowels(word)}")