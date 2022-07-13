
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 4 (instead of the number),
        "Buzz" for multiples of 23 (instead of the number),
        "FizzBuzz" for multiples of both 4 and 23  (instead of the number),
        the number itself otherwise.
    """
    if num % 4 == 0:
        return "Fizz"
    elif num % 23 == 0:
        return "Buzz"
    elif num % 4 == 0 and num % 23 == 0:
        return "FizzBuzz"
    else:
        return str(num)


# Test Cases
# Test Case 1
print("\nTest Case 1:")
print("Fizz Buzz FizzBuzz")
print(fizzbuzz(15))

# Test Case 2
print("\nTest Case 2:")
print("Fizz Buzz Fizz")
print(fizzbuzz(16))

# Test Case 3
print("\nTest Case 3:")
print("Fizz Buzz Buzz")
print(fizzbuzz(17))

# Test Case 4
print("\nTest Case 4:")
print("Fizz Buzz FizzBuzz")
print(fizzbuzz(18))

# Test Case 5
print("\nTest Case 5:")
print("Fizz Buzz Buzz")
print(fizzbuzz(19))

# Test Case 6
print("\nTest Case 6:")
print("Fizz Buzz Fizz")
print(fizzbuzz(20))

# Test Case 7
print("\nTest Case 7:")
print("Fizz Buzz Buzz")
print(fizzbuzz(21))

# Test Case 8
print("\nTest Case 8:")
print("Fizz Buzz FizzBuzz")
print(fizzbuzz(22))

# Test Case 9
print("\nTest Case 9:")
print("Fizz Buzz Fizz")
print(fizzbuzz(23))

# Test Case 10
print("\nTest Case 10:")
print("Fizz Buzz Buzz")
print(fizzbuzz(24))

# Test Case 11
print("\nTest Case 11:")
print("Fizz Buzz FizzBuzz")
print(fizzbuzz(25))

# Test Case 12
print("\nTest Case 12:")
print("Fizz Buzz Buzz")
print(fizzbuzz(26))

# Test Case 13
print("\nTest Case 13:")
print("Fizz Buzz Fizz")
print(fizzbuzz(27))

# Test Case 14
print("\nTest Case 14:")
print("Fizz Buzz Buzz")
print(fizzbuzz(28))

# Test Case 15
print("