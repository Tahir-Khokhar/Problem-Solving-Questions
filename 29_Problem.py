# 29. Find the Greatest Common Divisor (GCD).

# Problem: Find the GCD of two numbers using the Euclidean algorithm.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

print(gcd(48, 18)) # Output: 6