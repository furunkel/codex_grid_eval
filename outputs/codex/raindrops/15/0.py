
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 7, so the result would be "PlangBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    result = ''
    if num % 3 == 0:
        result += 'Pling'
    if num % 5 == 0:
        result += 'Plang'
    if num % 7 == 0:
        result += 'Plong'
    if result == '':
        result = str(num)
    return result