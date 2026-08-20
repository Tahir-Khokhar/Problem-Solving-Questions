# 14. Group dictionary items by a value.

# Problem: Given a list of dictionaries (e.g., employees), group them by a specific key (e.g., department).

def group_by_key(data, key):
    grouped = {}
    for item in data:
        group_name = item[key]
        if group_name not in grouped:
            grouped[group_name] = []
        grouped[group_name].append(item)
    return grouped

employees = [
    {"name": "Alice", "dept": "HR"},
    {"name": "Bob", "dept": "IT"},
    {"name": "Charlie", "dept": "HR"}
]
print(group_by_key(employees, "dept"))
# Output: {'HR': [{'name': 'Alice', 'dept': 'HR'}, ...], 'IT': [{'name': 'Bob', 'dept': 'IT'}]}