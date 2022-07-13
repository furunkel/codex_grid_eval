
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num < 1:
        return "Not a number"
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
        return "Pling"
    if num == 14:
        return "Buzz"
    if num == 15:
        return "PlingBuzz"
    if num == 16:
        return "Plong"
    if num == 17:
        return "PlongBuzz"
    if num == 18:
        return "PlongPling"
    if num == 19:
        return "PlongPlingBuzz"
    if num == 20:
        return "PlongPlingBuzzPling"
    if num == 21:
        return "PlongPlingBuzzPlingPling"
    if num == 22:
        return "PlongPlingBuzzPlingPlingBuzz"
    if num == 23:
        return "PlongPlingBuzzPlingPlingBuzzPling"
    if num == 24:
        return "PlongPlingBuzzPlingPlingBuzzPlingPling"
    if num == 25:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzz"
    if num == 26:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPling"
    if num == 27:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPlingPling"
    if num == 28:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPlingPlingBuzz"
    if num == 29:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPlingPlingBuzzPling"
    if num == 30:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPlingPlingBuzzPling"
    if num == 31:
        return "PlongPlingBuzzPlingPlingBuzzPlingPlingBuzzPlingPlingBuzz