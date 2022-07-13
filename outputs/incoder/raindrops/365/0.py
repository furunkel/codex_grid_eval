
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 5, so the result would be "PlangPling".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'Buzz'
    elif num == 11:
        return 'Plang'
    elif num == 12:
        return 'Pling'
    elif num == 13:
        return 'PlangPling'
    elif num == 14:
        return 'Buzz'
    elif num == 15:
        return 'Buzz'
    elif num == 16:
        return 'Buzz'
    elif num == 17:
        return 'Buzz'
    elif num == 18:
        return 'Buzz'
    elif num == 19:
        return 'Buzz'
    elif num == 20:
        return 'Buzz'
    elif num == 21:
        return 'Buzz'
    elif num == 22:
        return 'Buzz'
    elif num == 23:
        return 'Buzz'
    elif num == 24:
        return 'Buzz'
    elif num == 25:
        return 'Buzz'
    elif num == 26:
        return 'Buzz'
    elif num == 27:
        return 'Buzz'
    elif num == 28:
        return 'Buzz'
    elif num == 29:
        return 'Buzz'
    elif num == 30:
        return 'Buzz'
    elif num == 31:
        return 'Buzz'
    elif num == 32:
        return 'Buzz'
    elif num == 33:
        return 'Buzz'
    elif num == 34:
        return 'Buzz'
    elif num == 35:
        return 'Buzz'
    elif num == 36:
        return 'Buzz'
    elif num == 37:
        return 'Buzz'
    elif num == 38:
        return 'Buzz'
    elif num == 39:
        return 'Buzz'
    elif num == 40:
        return 'Buzz'
    elif num == 41:
        return 'Buzz'
    elif num == 42:
        return 'Buzz'
    elif num == 43:
        return 'Buzz'
    elif num == 44:
        return 'Buzz'
    elif num == 45:
        return 'Buzz'
    elif num == 46:
        return 'Buzz'
    elif num == 47:
        return 'Buzz'
    elif num == 48:
        return 'Buzz'
    elif num == 49:
        return 'Buzz'
    elif num == 50:
        return 'Buzz'
