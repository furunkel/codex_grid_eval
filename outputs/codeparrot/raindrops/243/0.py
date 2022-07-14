def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 11, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 5, so the result would be "Plong".
    55 has both 11 and 5 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 11, 5, or 7, so the result would be "2".
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
        return "10"
    if num == 11:
        return "11"
    if num == 12:
        return "12"
    if num == 13:
        return "13"
    if num == 14:
        return "14"
    if num == 15:
        return "15"
    if num == 16:
        return "16"
    if num == 17:
        return "17"
    if num == 18:
        return "18"
    if num == 19:
        return "19"
    if num == 20:
        return "20"
    if num == 21:
        return "21"
    if num == 22:
        return "22"
    if num == 23:
        return "23"
    if num == 24:
        return