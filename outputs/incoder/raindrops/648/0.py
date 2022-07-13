
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num == 3:
        return "3"
    if num == 4:
        return "4"
    if num == 5:
        return "5"
    if num == 6:
        return "6"
    if num == 7:
        return "7"
    if num == 8:
        return "8"
    if num == 9:
        return "9"
    if num == 10:
        return "A"
    if num == 11:
        return "B"
    if num == 12:
        return "C"
    if num == 13:
        return "D"
    if num == 14:
        return "E"
    if num == 15:
        return "F"
    if num == 16:
        return "G"
    if num == 17:
        return "H"
    if num == 18:
        return "I"
    if num == 19:
        return "J"
    if num == 20:
        return "K"
    if num == 21:
        return "L"
    if num == 22:
        return "M"
    if num == 23:
        return "N"
    if num == 24:
        return "O"
    if num == 25:
        return "P"
    if num == 26:
        return "Q"
    if num == 27:
        return "R"
    if num == 28:
        return "S"
    if num == 29:
        return "T"
    if num == 30:
        return "U"
    if num == 31:
        return "V"
    if num == 32:
        return "W"
    if num == 33:
        return "X"
    if num == 34:
        return "Y"
    if num == 35:
        return "Z"
    if num == 36:
        return "0"
    if num == 37:
        return "1"
    if num == 38:
        return "2"
    if num == 39:
        return "3"
    if num == 40:
        return "4"
    if num == 41:
        return "5"
    if num == 42:
        return "6"
    if num == 43:
        return "7"
    if num == 44:
        return "8"
    if num == 45:
        return "9"
    if num == 46:
        return "A"
    if num == 47:
        return "B"
    if num == 48:
        return "C"
    if num == 49:
        return "D"
    if num == 50:
        return "E"
    if num == 51:
        return "F"
    if num == 52:
        return "G"
    if num == 53:
        return "H"
    if num == 54:
        return "I"
    if num == 55:
        return "J"
    if 