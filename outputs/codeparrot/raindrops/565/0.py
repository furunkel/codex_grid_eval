def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plang".
    65 has both 13 and 5 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return "0"
    if num % 2 == 0:
        return str(num)
    else:
        return str(num) + " " + str(num / 2)


def raindrops_with_factors(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "FizzBuzz".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0