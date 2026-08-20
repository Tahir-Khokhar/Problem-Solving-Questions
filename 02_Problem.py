# 2. Check for Palindromes (ignoring case and punctuation).

# Problem: Determine if a given string is a palindrome, considering only alphanumeric characters and ignoring case.

import re
def is_palindrome(s):
    # Remove non-alphanumeric chars and convert to lowercase
    clean_s = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    return clean_s == clean_s[::-1]

print(is_palindrome("A man, a plan, a canal: Panama")) # Output: True