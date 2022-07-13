
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 11, so the result would be "PlingPlang".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)

# END PROBLEM 4


# PROBLEM 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1, 3, and 5 followed by the numbers 3, and 5, respectively.
    For example, if the number passed is 5, the result should be "153".
    """
    if num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    else:
        return str(num)

# END PROBLEM 5


# PROBLEM 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1, 3, and 5 followed by the numbers 3, and 5, respectively.
    For example, if the number passed is 5, the result should be "153".
    """
    if num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    else:
        return str(num)

# END PROBLEM 6


# PROBLEM 7
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1, 3, and 5 followed by the numbers 3, and 5, respectively.
    For example, if the number passed is 5, the result should be "153".
    """
    if num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num % 5 == 0:
        return "5"
    elif num % 3 == 0:
        return "3"
    elif num