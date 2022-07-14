def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Buzz".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlangPling".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"
    elif num == 10:
        return "10"
    elif num == 11:
        return "11"
    elif num == 12:
        return "12"
    elif num == 13:
        return "13"
    elif num == 14:
        return "14"
    elif num == 15:
        return "15"
    elif num == 16:
        return "16"
    elif num == 17:
        return "17"
    elif num == 18:
        return "18"
    elif num == 19:
        return "19"
    elif num == 20:
        return "20"
    elif num == 21:
        return "21"
    elif num == 22:
        return "22"
    elif num == 23:
        return "23"
    elif num == 24:
        return