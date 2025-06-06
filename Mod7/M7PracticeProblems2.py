# this function checks if a string is a palindrome by giving a true or false response
def is_palindrome(s):
    s = s.lower()  # changes the string to lowercase to fix case sensitivity
    return s == s[::-1]

# test cases
print(is_palindrome("Racecar"))  # should print true
print(is_palindrome("hello"))    # should print false