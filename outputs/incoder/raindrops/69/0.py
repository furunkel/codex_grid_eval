
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 11, so the result would be "PlangBuzz".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 9
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, if the number is divisible by 3, you should add 'Fizz' to the result.
    However, if the number is divisible by 5, you should add 'Buzz' to the result.
    However, if the number is divisible by both 3 and 5, you should add both 'FizzBuzz' to the result.
    Otherwise, just add 'FizzBuzz' to the result.

    Examples:
    15 -> "FizzBuzz"
    3 -> "Fizz"
    5 -> "Buzz"
    150 -> "FizzBuzz"
    17 -> "Fizz"
    175 -> "Buzz"
    1750 -> "FizzBuzz"
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 15 == 0:
        return "FizzBuzz"
    else:
        return str(num)


# Problem 10
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, if the number is divisible by 3, you should add 'Fizz' to the result.
    However, if the number is divisible by 5, you should add 'Buzz' to the result.
    However, if the number is divisible by both 3 and 5, you should add both 'FizzBuzz' to the result.
    Otherwise, just add 'FizzBuzz' to the result.

    Examples:
    15 -> "FizzBuzz"
    3 -> "Fizz"
    5 -> "Buzz"
    150 -> "FizzBuzz"
    17 -> "Fizz"
    175 -> "Buzz"
    1750 -> "FizzBuzz"
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 15 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    else:
        return str(num)


# Problem 11
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, if the 