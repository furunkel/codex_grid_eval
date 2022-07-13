
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Buzz".
    143 has both 13 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Pling"
    elif num % 7 == 0:
        return "Buzz"
    else:
        return str(num)

# END PROBLEM 4


# PROBLEM 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    3 has 3 as a factor, so the result would be "Fizz".
    5 has 5 as a factor, so the result would be "Buzz".
    7 has 7 as a factor, so the result would be "FizzBuzz".
    11 is not factored by 3, 5, or 7, so the result would be "11".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "FizzBuzz"
    else:
        return str(num)

# END PROBLEM 5


# PROBLEM 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    3 has 3 as a factor, so the result would be "Fizz".
    5 has 5 as a factor, so the result would be "Buzz".
    7 has 7 as a factor, so the result would be "FizzBuzz".
