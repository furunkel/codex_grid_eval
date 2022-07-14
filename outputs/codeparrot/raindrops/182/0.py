def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Buzz".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num % 2 == 0:
        return str(num)
    if num % 11 == 0:
        return str(num/11) + ' ' + str(num%11)
    if num % 7 == 0:
        return str(num/7) + ' ' + str(num%7)
    return str(num) + ' ' + str(num/7)


def raindrops_to_string(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as