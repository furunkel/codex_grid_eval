
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 5, so the result would be "PlangBuzz".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    result = ''
    if num % 13 == 0:
        result += 'Plang'
    if num % 11 == 0:
        result += 'Buzz'
    if num % 5 == 0:
        result += 'Plong'
    if result == '':
        result = str(num)
    return result