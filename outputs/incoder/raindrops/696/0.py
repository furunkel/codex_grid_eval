
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 5, so the result would be "FizzPling".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)


# Task 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if a number is divisible by 3, Fizz if a number is divisible by 5, and Buzz if a number is divisible by both 3 and 5.

    Examples:
    21 is divisible by both 3 and 5, so the result would be "Buzz".
    17 is divisible by 3, so the result would be "Fizz".
    9 is not divisible by either 3, 5 or both, so the result would be "9".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Task 3
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if a number is divisible by 3, Fizz if a number is divisible by 5, and Buzz if a number is divisible by both 3 and 5.

    Examples:
    21 is divisible by both 3 and 5, so the result would be "Buzz".
    17 is divisible by 3, so the result would be "Fizz".
    9 is not divisible by either 3, 5 or both, so the result would be "9".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 5 == 0 and num % 3 == 0:
        return "Buzz"
    elif num % 