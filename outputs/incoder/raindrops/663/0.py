
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlangBuzz".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(143))
print(raindrops(2))
</cell>
<text>
Problem 3
Write a function that takes in a positive integer and returns the number of digits in that number.

Examples:
If the number is 123, the function should return 3.
If the number is 12, the function should return 2.
If the number is 1, the function should return 0.
If the number is 0, the function should return 0.
If the number is -5, the function should return 0.


</text>
<cell>
def digits(num):
    """
    Your task is to write a function named digits that takes in a positive integer and returns the number of digits in that number.

    Examples:
    123 has 3 digits, so the function should return 3.
    12 has 2 digits, so the function should return 2.
    1 has 0 digits, so the function should return 0.
    0 has 0 digits, so the function should return 0.
    -5 has 0 digits, so the function should return 0.
    """
    if num == 0:
        return 0
    elif num < 0:
        return 0
    else:
        return len(str(num))

# Test Cases
print(digits(123))
print(digits(12))
print(digits(1))
print(digits(0))
print(digits(-5))
</cell>
<text>
Problem 4
Write a function that takes in a positive integer and returns the sum of the digits of that number.

Examples:
If the number is 123, the function should return 6 (1 + 2).
If the number is 12, the function should return 3 (1 + 0).
If the number is 1, the function should return 1 (0 + 0).
If the number is 0, the function should return 0 (0 + 0).
If the number is -5, the function should return 0 (0 + 0).


</text>
<cell>
def digitsum(num):
    """
    Your task is to write a function named digitsum that takes in a positive integer and returns the sum of the digits of that number.

    Examples:
    123 has 6 digits, so the function should return 6.
    12 has 3 digits, so the function should return 3.
    1 has 1 digit, so the function should return 1.
    0 has 0 digits, so the function should return 0.
    -5 has 0 digits, so the function should return 0.
    """
    if num == 0:
        return 0
    elif num < 0:
        return 0
    else:
        return sum(map(int, str(num)))

# Test Cases
print(digitsum(123))
print(digitsum(12))
