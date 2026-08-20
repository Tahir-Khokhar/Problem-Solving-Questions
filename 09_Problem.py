# 9. Flatten a 2D list.

# Problem: Convert a list of lists into a single flat list.

def flatten_2d(matrix):
    # Using list comprehension
    return [item for sublist in matrix for item in sublist]

print(flatten_2d([[1, 2], [3, 4], [5]])) # Output: [1, 2, 3, 4, 5]