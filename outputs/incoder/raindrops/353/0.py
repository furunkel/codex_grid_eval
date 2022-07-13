
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 5, so the result would be "PlingPlang".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    if num % 11 == 0:
        return 'Pling'
    if num % 3 == 0:
        return 'Plang'
    if num % 5 == 0:
        return 'Buzz'
    return str(num)


# Problem 4
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced with 'Fizz' if it is divisible by 3, 'Buzz' if it is divisible by 5
    and 'FizzBuzz' if it is divisible by both.

    Examples:
    1 should be replaced with 'Fizz'.
    3 should be replaced with 'Fizz'.
    5 should be replaced with 'Buzz'.
    15 should be replaced with 'FizzBuzz'.
    21 should be replaced with 'FizzBuzz'.
    37 should be replaced with 'FizzBuzz'.
    63 should be replaced with 'FizzBuzz'.
    """
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 21 == 0:
        return 'FizzBuzz'
    if num % 37 == 0:
        return 'FizzBuzz'
    if num % 63 == 0:
        return 'FizzBuzz'
    return str(num)


# Problem 5
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced with 'Fizz' if it is divisible by 3, 'Buzz' if it is divisible by 5
    and 'FizzBuzz' if it is divisible by both.

    Examples:
    1 should be replaced with 'Fizz'.
    3 should be replaced with 'Fizz'.
    5 should be replaced with 'Buzz'.
    15 should be replaced with 'FizzBuzz'.
    21 should be replaced with 'FizzBuzz'.
    37 should be replaced with 'FizzBuzz'.
    63 should be replaced with 'FizzBuzz'.
    """
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    if num % 15 == 0:
        return 'FizzBuzz'
    if num % 21 == 0:
        return 'FizzBuzz'
    if num % 37 == 0:
        return 'FizzBuzz'
    if num % 63 == 0:
        return 'FizzBuzz'
