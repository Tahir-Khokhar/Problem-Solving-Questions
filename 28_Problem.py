# 28. Generate Fibonacci sequence up to N terms.

# Problem: Return a list of the first N Fibonacci numbers.


def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    
    sequence = [0, 1]
    for _ in range(2, n):
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

print(fibonacci(7)) # Output: [0, 1, 1, 2, 3, 5, 8]