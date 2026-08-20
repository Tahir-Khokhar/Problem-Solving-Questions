# 5. Extract all email addresses from a text.

# Problem: Parse a block of text and extract all valid-looking email addresses.

import re

def extract_emails(text):
    # Simple regex for email extraction
    pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    return re.findall(pattern, text)

print(extract_emails("Contact us at info@test.com or support@company.org")) 
# Output: ['info@test.com', 'support@company.org']