
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    factors = []
    factors.append(str(num))
    if num % 13 == 0:
        factors.append('Fizz')
    if num % 3 == 0:
        factors.append('Pling')
    if num % 5 == 0:
        factors.append('Plong')
    if len(factors) == 0:
        return str(num)
    else:
        return ''.join(factors)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'Fizz' to the result, and for multiples of five (buzz), you append 'Buzz' to the result.
    You do not need to worry about numbers which are multiples of both three and five.

    Examples:
    1 returns '1', because 1 is a multiple of both 3 and 5.
    3 returns 'Fizz', because 3 is a multiple of both 3 and 5.
    5 returns 'Buzz', because 5 is a multiple of both 3 and 5.
    15 returns 'FizzBuzz', because 15 is a multiple of both 3 and 5.
    21 returns '2'.
    37 returns 'Fizz', because 37 is a multiple of both 3 and 5.
    81 returns 'Buzz', because 81 is a multiple of both 3 and 5.
    """
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5