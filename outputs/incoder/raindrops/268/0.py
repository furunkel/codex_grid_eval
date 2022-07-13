
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 11, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 5, so the result would be "Plang".
    55 has both 11 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 11, 5, or 7, so the result would be "2".
    """
    factors = []
    if num % 11 == 0:
        factors.append('Fizz')
    if num % 5 == 0:
        factors.append('Buzz')
    if num % 7 == 0:
        factors.append('Plang')
    if factors == []:
        return str(num)
    else:
        return ''.join(factors)

# END PROBLEM 4


# PROBLEM 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of FizzBuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 3 as a factor, but not 5 or 7, so the result would be "Fizz".
    55 has both 3 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    factors = []
    if num % 3 == 0:
        factors.append('Fizz')
    if num % 5 == 0:
        factors.append('Buzz')
    if num % 7 == 0:
        factors.append('FizzBuzz')
    if factors == []:
        return str(num)
    else:
        return ''.join(factors)

# END PROBLEM 5


# PROBLEM 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of FizzBuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 3 as a factor, but not 5 or 7, so the result would be "F