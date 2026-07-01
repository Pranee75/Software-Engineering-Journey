# The "Join vs. Concatenation" Pattern

# (O(n^2) complexity)
def concat_slow(words):
    res = ""
    for w in words:
        res += w  # Creates a new string object every time
    return res

# (O(n) complexity)
def concat_fast(words):
    return "".join(words) # Allocates memory once


# The Cleaning & Tokenizing Workflow

raw_data = "  USER@example.com,  Admin@test.org,  guest@site.net  "

# Strip whitespace and split into a list
emails = [email.strip() for email in raw_data.split(',')]
print(emails)
# Use list comprehension to filter or modify
clean_emails = [e.lower() for e in emails if "@" in e]
print(clean_emails)

# Modern String Formatting (f-strings)

name = "Alice"
balance = 1234.5678

# {width:type}
# :.2f = 2 decimal places, :>10 = right align with 10 spaces
print(f"User: {name:<10} | Balance: ${balance:>10.2f}")

# Encoding/Decoding (Bytes vs. Strings)

# Text (str) to Binary (bytes)
text = "Python"
encoded = text.encode("utf-8") 

# Binary to Text
decoded = encoded.decode("utf-8")
print(f"Bytes: {encoded}, Decoded: {decoded}")


# String Constants (Using the string module)

import string

def get_stats(text):
    letters = sum(1 for char in text if char in string.ascii_letters)
    digits = sum(1 for char in text if char in string.digits)
    punct = sum(1 for char in text if char in string.punctuation)
    return letters, digits, punct

print(get_stats("Hello World! 123"))


# The "In-place" Logic (The Palindrome/Reversal Trick)

# Reversing a string
s = "abcdef"
reversed_s = s[::-1] 

# (if you were converting to a list)
char_list = list(s)
char_list.reverse()
new_s = "".join(char_list)
