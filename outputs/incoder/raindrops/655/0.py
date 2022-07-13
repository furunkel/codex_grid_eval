
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plang".
    143 has both 13 and 11 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num < 1:
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
        return "Pling"
    elif num == 12:
        return "Plang"
    else:
        factors = []
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        factors.append(num % 13)
        factors.append(num % 11)
        factors.append(num % 7)
        factors.append(num % 3)
        factors.append(num % 5)
        factors.append(num % 7)
        factors.append(num % 9)
        factors.append(num % 11)
        