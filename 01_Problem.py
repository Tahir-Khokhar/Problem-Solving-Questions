# 1. Reverse the words in a sentence.

# Problem: Given a string sentence, reverse the order of the words, but keep the words themselves intact.

def reverse_words(sentence):
    # Split by space, reverse the list, and join back with space
    words = sentence.split()
    return " ".join(words[::-1])

print(reverse_words("Hello world this is Python")) 
# Output: "Python is this world Hello"