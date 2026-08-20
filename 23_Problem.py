# 23. Write list of dictionaries to CSV.

# Problem: Export a list of dictionaries to a CSV file.

import csv

def write_to_csv(data, filepath):
    if not data:
        return
    keys = data[0].keys()
    with open(filepath, 'w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=keys)
        writer.writeheader()
        writer.writerows(data)

data = [
    {"name": "Alice", "age": "30"},
    {"name": "Bob", "age": "25"}
]
write_to_csv(data, "output.csv")
print("Written to output.csv")