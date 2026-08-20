# 13. Count frequency of elements.

# Problem: Count how many times each item appears in a list.

from collections import Counter

def count_frequency(items):
    return dict(Counter(items))

print(count_frequency(['apple', 'banana', 'apple', 'orange', 'banana', 'apple'])) 
# Output: {'apple': 3, 'banana': 2, 'orange': 1}
