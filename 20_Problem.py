# 20. Read file and find longest word.

# Problem: Open a file, find the longest word, and return it. If tie, return the first one found.

def longest_word_in_file(filepath):
    longest = ""
    with open(filepath, 'r') as file:
        for line in file:
            words = line.strip().split()
            for word in words:
                if len(word) > len(longest):
                    longest = word
    return longest


with open("words.txt", "w") as f:
    f.write("Hello world this is Python\n")
print(longest_word_in_file("words.txt"))  # Output: Python