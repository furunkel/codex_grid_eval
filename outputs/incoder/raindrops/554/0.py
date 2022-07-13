
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
    factors = []
    if num % 13 == 0:
        factors.append('Plang')
    if num % 5 == 0:
        factors.append('Pling')
    if num % 11 == 0:
        factors.append('Buzz')
    if num % 13 not in factors and num % 5 not in factors and num % 11 not in factors:
        factors.append(str(num))
    return ''.join(factors)


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if it is a multiple of 3, Fizz if it is a multiple of 5, and Buzz if it is a multiple of 7.

    Examples:
    15 would be FizzBuzz.
    21 would be FizzBuzz.
    37 would be Buzz.
    101 would be Fizz.
    103 would be FizzBuzz.
    105 would be Buzz.
    111 would be FizzBuzz.
    113 would be FizzBuzz.
    115 would be FizzBuzz.
    121 would be FizzBuzz.
    123 would be FizzBuzz.
    125 would be FizzBuzz.
    131 would be FizzBuzz.
    133 would be FizzBuzz.
    135 would be FizzBuzz.
    141 would be FizzBuzz.
    143 would be FizzBuzz.
    145 would be FizzBuzz.
    151 would be FizzBuzz.
    153 would be FizzBuzz.
    155 would be FizzBuzz.
    161 would be FizzBuzz.
    163 would be FizzBuzz.
    165 would be FizzBuzz.
    171 would be FizzBuzz.
    173 would be FizzBuzz.
    175 would be FizzBuzz.
    181 would be FizzBuzz.
    183 would be FizzBuzz.
    185 would be FizzBuzz.
    191 would be FizzBuzz.
    193 would be FizzBuzz.
    195 would be FizzBuzz.
    201 would be FizzBuzz.
    203 would be FizzBuzz.
    205 would be FizzBuzz.
    211 would be FizzBuzz.
    213 would be FizzBuzz.
    215 would be FizzBuzz.
    221 would be FizzBuzz.
    