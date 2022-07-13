
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    factors = []
    if num % 13 == 0:
        factors.append('Fizz')
    if num % 3 == 0:
        factors.append('Pling')
    if num % 11 == 0:
        factors.append('Plang')
    if num % 3 != 0 and num % 13 != 0 and num % 11 != 0:
        factors.append(str(num))
    return ''.join(factors)


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Buzz' to the result, and for multiples of five ('Buzz') you append 'FizzBuzz'.
    You do not need to worry about numbers like 1 or 5, because they will always result in a FizzBuzz.
    You will always append the number as a string.

    Examples:
    1 becomes '1'
    2 becomes '2'
    3 becomes 'Fizz'
    4 becomes 'Buzz'
    5 becomes 'Buzz'
    6 becomes 'FizzBuzz'
    7 becomes '7'
    8 becomes '8'
    9 becomes 'Fizz'
    10 becomes 'Buzz'
    11 becomes 'FizzBuzz'
    12 becomes 'FizzBuzz'
    13 becomes 'FizzBuzz'
    14 becomes 'FizzBuzz'
    15 becomes 'FizzBuzz'
    16 becomes 'FizzBuzz'
    17 becomes 'FizzBuzz'
    18 becomes 'FizzBuzz'
    19 becomes 'FizzBuzz'
    20 becomes 'FizzBuzz'
    21 becomes 'FizzBuzz'
    22 becomes 'FizzBuzz'
    23 becomes 'FizzBuzz'
    24 becomes 'FizzBuzz'
    25 becomes 'FizzBuzz'
    26 becomes 'FizzBuzz'
    27 becomes 'FizzBuzz'
    28 becomes 'FizzBuzz'
    29 becomes 'FizzBuzz'
    30 becomes 'FizzBuzz'
    31 becomes 'FizzBuzz'
    32 becomes 'FizzBuzz'
    33 becomes 'FizzBuzz'
    34 becomes 'FizzBuzz'
    35 becomes 'FizzBuzz'
    36 becomes 'FizzBuzz'
    37 becomes 'Fizz