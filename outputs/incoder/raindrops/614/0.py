
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Buzz".
    39 has both 13 and 3 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)

# Test Cases
print(raindrops(10))
print(raindrops(39))
print(raindrops(2))
</cell>
<text>
Problem 3
Write a function that takes in a positive integer and returns the number of digits in that number.

Examples:
If the number is 123, the function should return 3.
If the number is 120, the function should return 2.
If the number is 992323, the function should return 5.


</text>
<cell>
def digits(num):
    """
    Your task is to write a function named digits that takes in a positive integer and returns the number of digits in that number.

    Examples:
    If the number is 123, the function should return 3.
    If the number is 120, the function should return 2.
    If the number is 992323, the function should return 5.
    """
    return len(str(num))

# Test Cases
print(digits(123))
print(digits(120))
print(digits(992323))
</cell>
<text>
Problem 4
Write a function that takes in a positive integer and returns the sum of the squares of the digits in that number.

Examples:
If the number is 123, the function should return 50.
If the number is 120, the function should return 52.
If the number is 992323, the function should return 560223.


</text>
<cell>
def digits_squared(num):
    """
    Your task is to write a function named digits_squared that takes in a positive integer and returns the sum of the squares of the digits in that number.

    Examples:
    If the number is 123, the function should return 50.
    If the number is 120, the function should return 52.
    If the number is 992323, the function should return 560223.
    """
    total = 0
    digits = str(num)
    for digit in digits:
        total += int(digit) ** 2
    return total

# Test Cases
print(digits_squared(123))
print(digits_squared(120))
print(digits_squared(992323))
</cell>
<text>
Problem 5
Write a function that takes in a positive integer and returns the sum of the cubes of the digits in that number.

Examples:
If the number is 123, the function should return 627.
If the number is 120, the function should return 620.
If the number is 992323, the function should return 6680223.


</text>
<cell>
def digits_cubed(num):
    """
    Your task is to write a function named digits_cubed that takes in a 