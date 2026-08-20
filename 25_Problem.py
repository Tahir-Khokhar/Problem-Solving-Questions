# 25. FizzBuzz.

# Problem: Print numbers 1 to 50. Multiples of 3 print "Fizz", multiples of 5 print "Buzz", multiples of both 
# print "FizzBuzz".

def fizzbuzz():
    for i in range(1, 51):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)