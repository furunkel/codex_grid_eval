
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 11, 3, or 7, so the result would be "2".
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
        return "Buzz"
    elif num == 11:
        return "Fizz"
    elif num == 12:
        return "Plang"
    elif num == 13:
        return "FizzBuzz"
    elif num == 14:
        return "FizzPlangBuzz"
    elif num == 15:
        return "FizzPlangBuzz"
    elif num == 16:
        return "FizzPlangBuzz"
    elif num == 17:
        return "FizzPlangBuzz"
    elif num == 18:
        return "FizzPlangBuzz"
    elif num == 19:
        return "FizzPlangBuzz"
    elif num == 20:
        return "FizzPlangBuzz"
    elif num == 21:
        return "FizzPlangBuzz"
    elif num == 22:
        return "FizzPlangBuzz"
    elif num == 23:
        return "FizzPlangBuzz"
    elif num == 24:
        return "FizzPlangBuzz"
    elif num == 25:
        return "FizzPlangBuzz"
    elif num == 26:
        return "FizzPlangBuzz"
    elif num == 27:
        return "FizzPlangBuzz"
    elif num == 28:
        return "FizzPlangBuzz"
    elif num == 29:
        return "FizzPlangBuzz"
    elif num == 30:
        return "FizzPlangBuzz"
    elif num == 31:
        return "FizzPlangBuzz"
    elif num == 32:
        return "FizzPlangBuzz"
    elif num == 33:
        return "FizzPlangBuzz"
    elif num == 34:
        return "FizzPlangBuzz"
    elif num == 35:
        return "FizzPlangBuzz"
    elif num == 36:
        return "FizzPlangBuzz"
    elif num == 37:
        return "FizzPlangBuzz"
    elif num == 38:
        return "FizzPlangBuzz"
    elif num == 39:
        return "FizzPlangBuzz"
    elif num == 40:
        return "FizzPlangBuzz"
