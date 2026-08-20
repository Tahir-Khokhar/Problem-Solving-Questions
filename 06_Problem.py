# 6. Convert a CSV string to a list of dictionaries.

# Problem: Parse a multi-line CSV string where the first line is the header.

import csv
import io

def csv_to_dicts(csv_string):
    reader = csv.DictReader(io.StringIO(csv_string))
    return list(reader)

csv_data = "name,age\nAlice,30\nBob,25"
print(csv_to_dicts(csv_data)) 
# Output: [{'name': 'Alice', 'age': '30'}, {'name': 'Bob', 'age': '25'}]