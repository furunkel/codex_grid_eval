
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 11, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 5, so the result would be "Plong".
    55 has both 11 and 5 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 11, 5, or 7, so the result would be "2".
    """
    result = ''
    if num % 11 == 0:
        result += 'Fizz'
    if num % 5 == 0:
        result += 'Pling'
    if num % 7 == 0:
        result += 'Plong'
    if result == '':
        result = str(num)
    return result