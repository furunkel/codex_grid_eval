def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plang".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num == 13:
        return 'Pling'
    elif num == 11:
        return 'Buzz'
    elif num == 7:
        return 'Plang'
    else:
        return '2'


def raindrops_with_factors(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "PlingBuzz".
    143 has both 13 and 11 as factors, but not 7, so the result would be "2".
    2 is not factored by