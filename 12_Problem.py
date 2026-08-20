# 12. Find the intersection of multiple lists.

# Problem: Find elements that are common to all lists provided.

def intersect_lists(*lists):
    if not lists:
        return []
    # Convert first list to set, then intersect with others
    common = set(lists[0])
    for lst in lists[1:]:
        common.intersection_update(lst)
    return list(common)

print(intersect_lists([1, 2, 3], [2, 3, 4], [2, 5, 3])) # Output: [2, 3]