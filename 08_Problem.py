# 8. Remove duplicates while preserving order.

# Problem: Remove duplicates from a list without using set() to destroy the original order.

def remove_duplicates_ordered(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

print(remove_duplicates_ordered([1, 2, 2, 3, 1, 4])) # Output: [1, 2, 3, 4]
