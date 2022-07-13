
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 11, so the result would be "PlingBuzz".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return 'Pling'
    elif num % 3 == 0:
        return 'Buzz'
    elif num % 11 == 0:
        return 'Plang'
    else:
        return str(num)


# Problem 3
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, if the number is divisible by 3, you should add 'Fizz' to the result.
    However, if the number is divisible by 5, you should add 'Buzz' to the result.
    However, if the number is divisible by both 3 and 5, you should add both 'FizzBuzz' to the result.
    Otherwise, just add 'FizzBuzz' to the result.

    Examples:
    1 should return 'FizzBuzz'.
    3 should return 'Fizz'.
    5 should return 'Buzz'.
    15 should return 'FizzBuzz'.
    21 should return 'FizzBuzz'.
    37 should return 'FizzBuzz'.
    63 should return 'FizzBuzz'.
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


# Problem 4
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, if the number is divisible by 3, you should add 'Fizz' to the result.
    However, if the number is divisible by 5, you should add 'Buzz' to the result.
    However, if the number is divisible by both 3 and 5, you should add both 'FizzBuzz' to the result.
    Otherwise, just add 'FizzBuzz' to the result.

    Examples:
    1 should return 'FizzBuzz'.
    3 should return 'Fizz'.
    5 should return 'Buzz'.
    15 should return 'FizzBuzz'.
    21 should return 'FizzBuzz'.
    37 should return 'FizzBuzz'.
    63 should return 'FizzBuzz'.
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'