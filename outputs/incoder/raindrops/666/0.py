
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)


# In[11]:


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (ie, 3, 6, 9, 12, ...), print Fizz.
    For multiples of five (ie, 5, 10, 15, 20, ...), print Buzz.
    For multiples of both three and five (ie, 3, 6, 9, 12, ...), print FizzBuzz.
    Otherwise, print Num.

    Examples:
    1 -> 1
    2 -> 2
    3 -> Fizz
    4 -> 4
    5 -> Buzz
    6 -> Fizz
    7 -> 7
    8 -> 8
    9 -> Fizz
    10 -> Buzz
    11 -> Fizz
    12 -> FizzBuzz
    13 -> 13
    14 -> FizzBuzz
    15 -> Buzz
    16 -> 16
    17 -> 17
    18 -> FizzBuzz
    19 -> 19
    20 -> Buzz
    21 -> Fizz
    22 -> 22
    23 -> Fizz
    24 -> 24
    25 -> Buzz
    26 -> Fizz
    27 -> 27
    28 -> Fizz
    29 -> 29
    30 -> Fizz
    31 -> 31
    32 -> Fizz
    33 -> 33
    34 -> Fizz
    35 -> Buzz
    36 -> Fizz
    37 -> 37
    38 -> Fizz
    39 -> 39
    40 -> Fizz
    41 -> 41
    42 -> Fizz
    43 -> 43
    44 -> Fizz
    45 -> Buzz
    46 -> Fizz
    47 -> 47
    48 -> Fizz
    49 -> 49
    50 -> Buzz
    51 -> Fizz
    52 -> 52
    53 -> Fizz
    54 -> 54
    55 -> Buzz
    56 -> Fizz
    57 -> 57
    58 -> Fizz
    59 -> 59
    60 -> Buzz
    61 -> Fizz
    62 -> 62
    63 -> Fizz
    64 -> 64
    65 -> Bu