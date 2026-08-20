# 11. Chunk a list into smaller lists.

# Problem: Split a list into smaller lists of a specified size.

def chunk_list(lst, size):
    # Using range with step size
    return [lst[i:i + size] for i in range(0, len(lst), size)]

print(chunk_list([1, 2, 3, 4, 5, 6, 7], 3)) # Output: [[1, 2, 3], [4, 5, 6], [7]]