# 10. Find pairs that sum to a target.

# Problem: Given a list of numbers and a target, find all unique pairs that add up to the target.

def find_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        diff = target - num
        if diff in seen:
            # Add as a sorted tuple to avoid duplicate pair orders like (1,2) and (2,1)
            pairs.add(tuple(sorted((num, diff))))
        seen.add(num)
    return list(pairs)

print(find_pairs([1, 2, 3, 4, 5, 2], 5)) # Output: [(2, 3), (1, 4)]