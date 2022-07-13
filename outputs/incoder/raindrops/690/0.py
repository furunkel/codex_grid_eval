
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 5, so the result would be "PlangBuzz".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)


# Task 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by either 'Fizz' or 'Buzz', and each number should be followed by a space.
    For example:

    1 should be 'Fizz Buzz'.
    2 should be 'Fizz 2'.
    3 should be 'Fizz 3'.
    4 should be 'Buzz 4'.
    5 should be 'Buzz 5'.
    6 should be 'Buzz 6'.
    7 should be 'Buzz 7'.
    8 should be 'Buzz 8'.
    9 should be 'Buzz 9'.
    10 should be 'Buzz 10'.
    11 should be 'Fizz 11'.
    12 should be 'Fizz 12'.
    13 should be 'Fizz 13'.
    14 should be 'Fizz 14'.
    15 should be 'Buzz 15'.
    16 should be 'Buzz 16'.
    17 should be 'Buzz 17'.
    18 should be 'Buzz 18'.
    19 should be 'Buzz 19'.
    20 should be 'Buzz 20'.
    21 should be 'Fizz 21'.
    22 should be 'Fizz 22'.
    23 should be 'Fizz 23'.
    24 should be 'Fizz 24'.
    25 should be 'Buzz 25'.
    26 should be 'Buzz 26'.
    27 should be 'Buzz 27'.
    28 should be 'Buzz 28'.
    29 should be 'Buzz 29'.
    30 should be 'Buzz 30'.
    31 should be 'Fizz 31'.
    32 should be 'Fizz 32'.
    33 should be 'Fizz 33'.
    34 should be 'Fizz 34'.
    35 should be 'Buzz 35'.
    36 should be 'Buzz 36'.
    37 should be 'Buzz 37'.
    38 should be 'Buzz 38'.
    39 should be 'Buzz 39'.
    40 should be 'Buzz 40'.
    41 should be 'Fizz 41'.
    42 should be 'Fiz