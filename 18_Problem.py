# 18. Filter dictionary by value threshold.

# Problem: Create a new dictionary containing only items where the value is greater than a threshold.

def filter_dict_by_value(d, threshold):
    return {k: v for k, v in d.items() if v > threshold}

print(filter_dict_by_value({'a': 50, 'b': 120, 'c': 80}, 75)) # Output: {'b': 120, 'c': 80}