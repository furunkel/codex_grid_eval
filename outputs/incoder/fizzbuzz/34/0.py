
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of five (instead of the number),
        "Buzz" for multiples of 11 (instead of the number),
        "FizzBuzz" for multiples of both five and 11  (instead of the number),
        the number itself otherwise.
    """
    if num % 5 == 0:
        return "FizzBuzz"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 11 == 0:
        return "FizzBuzz"
    else:
        return num

# Test Cases
# ---------
# Let's test our fizzbuzz function with some different test cases.
# We'll start by testing it on a number that should be divisible by five.
print(fizzbuzz(15))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five,
# but not by 11.
print(fizzbuzz(10))
# > Buzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(5))
# > FizzBuzz

# Now we'll test it on a number that should not be divisible by five or 11.
print(fizzbuzz(20))
# > 20

# Now we'll test it on a number that should not be divisible by five and 11.
print(fizzbuzz(25))
# > 25

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(35))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(45))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(55))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(65))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(75))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(85))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(95))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
print(fizzbuzz(105))
# > FizzBuzz

# Now we'll test it on a number that should be divisible by five and 11.
