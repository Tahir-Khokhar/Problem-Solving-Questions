# 7. Find the second largest number in a list.

# Problem: Return the second highest unique number in a list of integers.

def second_largest(nums):
    unique_nums = list(set(nums)) # Remove duplicates
    unique_nums.sort(reverse=True)
    if len(unique_nums) >= 2:
        return unique_nums[1]
    return None

print(second_largest([10, 20, 4, 45, 99, 99])) # Output: 45