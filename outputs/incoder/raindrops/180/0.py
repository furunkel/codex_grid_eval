
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 11 == 0:
        return 'Plang'
    elif num % 7 == 0:
        return 'Plong'
    else:
        return str(num)


# Task 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three or 5, you should add 'Fizz' to the result, and for multiples of both three and five,
    you should add 'Buzz'.
    For example, fizzbuzz(3) should return 'FizzBuzz'.
    Your function should work for any positive integer num.
    """
    if num % 3 == 0 or num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


# Task 3
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three or 5, you should add 'Fizz' to the result, and for multiples of both three and five,
    you should add 'Buzz'.
    For example, fizzbuzz2(3) should return 'FizzBuzz'.
    Your function should work for any positive integer num.
    """
    if num % 3 == 0 or num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif 