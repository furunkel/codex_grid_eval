
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    factors = [13, 3, 11]
    if num % 13 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Buzz'
    elif num % 11 == 0:
        return 'Plang'
    else:
        return str(num)


# Problem 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'FizzBuzz' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "FizzBuzz".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    factors = [13, 3, 11]
    if num % 13 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Buzz'
    elif num % 11 == 0:
        return 'FizzBuzz'
    else:
        return str(num)


# Problem 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'FizzBuzz' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "FizzBuzz".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 11, so the result would be 