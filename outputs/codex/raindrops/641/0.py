
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Buzz".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzPlang".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    result = ''
    if num % 13 == 0:
        result += 'Fizz'
    if num % 3 == 0:
        result += 'Plang'
    if num % 11 == 0:
        result += 'Buzz'
    if result == '':
        result = str(num)
    return result