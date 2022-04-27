
def fizzbuzz(num):
    """
    Given a number, this function returns
        "Fizz" for multiples of 3 (instead of the number),
        "Buzz" for multiples of 5 (instead of the number),
        "FizzBuzz" for multiples of both 3 and 5  (instead of the number),
        the number itself otherwise.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return num

# Test cases
print(fizzbuzz(3))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(4))

# Output
# Fizz
# Buzz
# FizzBuzz
# 4

#%%
# Problem 2
# Write a function that takes a string as input and returns a string with all vowels removed.

def remove_vowels(string):
    """
    Given a string, this function returns a string with all vowels removed.
    """
    vowels = "aeiouAEIOU"
    new_string = ""
    for char in string:
        if char not in vowels:
            new_string += char
    return new_string

# Test cases
print(remove_vowels("Hello"))
print(remove_vowels("World"))
print(remove_vowels("Hello World"))

# Output
# Hll
# Wrld
# Hll Wrld

#%%
# Problem 3
# Write a function that takes a list of numbers as input and returns a list of the squares of each number.

def square_list(nums):
    """
    Given a list of numbers, this function returns a list of the squares of each number.
    """
    squares = []
    for num in nums:
        squares.append(num ** 2)
    return squares

# Test cases
print(square_list([1, 2, 3, 4]))
print(square_list([0, -1, -2, -3]))

# Output
# [1, 4, 9, 16]
# [0, 1, 4, 9]

#%%
# Problem 4
# Write a function that takes a list of numbers as input and returns a list of the even numbers.

def even_list(nums):
    """
    Given a list of numbers, this function returns