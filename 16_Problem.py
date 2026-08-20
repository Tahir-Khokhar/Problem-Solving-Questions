# 16. Find the key with the highest value.

# Problem: Return the dictionary key that has the maximum value.

def max_value_key(d):
    if not d:
        return None
    # Using the max function with a lambda key
    return max(d, key=lambda k: d[k])

print(max_value_key({'a': 10, 'b': 25, 'c': 15})) # Output: 'b'