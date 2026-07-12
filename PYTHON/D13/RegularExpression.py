# Data Validation

import re

def is_valid_email(email):
    # Pattern: chars/dots/dashes + @ + domain + . + extension
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("test.user@example.com"))  # True
print(is_valid_email("invalid-email@com"))      # False

def is_valid_email(email):
    # Pattern: chars/dots/dashes + @ + domain + . + extension
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))

print(is_valid_email("test.user@example.com"))  # True
print(is_valid_email("invalid-email@com"))      # False


# Text Extraction & Manipulation

text = "Contact us at 123-456-7890 or 987-654-3210"
# Use parentheses () to create capturing groups
pattern = r'(\d{3})-(\d{3}-\d{4})'

matches = re.findall(pattern, text)
for area_code, number in matches:
    print(f"Area Code: {area_code}, Number: {number}")



html_text = "<p>Hello <b>World</b>!</p>"
# Pattern matches < followed by any char except > one or more times
clean_text = re.sub(r'<[^>]+>', '', html_text)

print(clean_text)  # "Hello World!"