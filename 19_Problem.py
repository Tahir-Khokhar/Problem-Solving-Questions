# 19. Count lines in a file.

# Problem: Read a text file and return the total number of lines.

def count_lines(filepath):
    with open(filepath, 'r') as file:
        return sum(1 for line in file)


with open("sample.txt", "w") as f:
    f.write("Line 1\nLine 2\nLine 3\n")
print(count_lines("sample.txt"))  # Output: 3