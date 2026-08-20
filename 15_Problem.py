# 15. Merge two dictionaries summing values.

# Problem: Merge two dictionaries with numeric values. If keys overlap, sum their values.

def merge_dicts(d1, d2):
    merged = d1.copy()
    for key, value in d2.items():
        merged[key] = merged.get(key, 0) + value
    return merged

print(merge_dicts({'a': 10, 'b': 5}, {'b': 3, 'c': 7})) # Output: {'a': 10, 'b': 8, 'c': 7}