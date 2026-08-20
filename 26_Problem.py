# 26. Check if a number is prime.

# Problem: Return True if a number is prime, False otherwise.

def is_prime(n):
    if n <= 1:
        return False
    # Only need to check up to the square root of n
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

print(is_prime(17)) # Output: True