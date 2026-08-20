# 30. Check if a year is a leap year.

# Problem: Determine if a given year is a leap year.

def is_leap_year(year):
    # Divisible by 4, but not 100, unless also divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    return False

print(is_leap_year(2024)) # Output: True