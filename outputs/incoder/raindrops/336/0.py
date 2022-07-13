
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 11, 3, or 7, so the result would be "2".
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
        return 'A'
    elif num == 11:
        return 'B'
    elif num == 12:
        return 'C'
    elif num == 13:
        return 'D'
    elif num == 14:
        return 'E'
    elif num == 15:
        return 'F'
    elif num == 16:
        return 'G'
    elif num == 17:
        return 'H'
    elif num == 18:
        return 'I'
    elif num == 19:
        return 'J'
    elif num == 20:
        return 'K'
    elif num == 21:
        return 'L'
    elif num == 22:
        return 'M'
    elif num == 23:
        return 'N'
    elif num == 24:
        return 'O'
    elif num == 25:
        return 'P'
    elif num == 26:
        return 'Q'
    elif num == 27:
        return 'R'
    elif num == 28:
        return 'S'
    elif num == 29:
        return 'T'
    elif num == 30:
        return 'U'
    elif num == 31:
        return 'V'
    elif num == 32:
        return 'W'
    elif num == 33:
        return 'X'
    elif num == 34:
        return 'Y'
    elif num == 35:
        return 'Z'
    elif num == 36:
        return '0'
    elif num == 37:
        return '1'
    elif num == 38:
        return '2'
    elif num == 39:
        return '3'
    elif num == 40:
        return '4'
    elif num == 41:
        return '5'
    elif num == 42:
        return '6'
    elif num == 43:
        return '7'
    elif num == 44:
        return '8'
    elif num == 45:
        return '9'
    elif num == 46:
        return 'A'
    elif num == 47:
        return 'B'
    elif num == 48:
        return 'C'
    elif num == 49:
        return 'D'
    elif num == 50:
        return 'E'
    elif num == 51:
        return 'F'
    elif num == 52:
        return 'G'
    elif num == 53:
        return 'H'
    elif num == 54:
        return 'I'
    elif num == 55:
        return 'J'
    elif 