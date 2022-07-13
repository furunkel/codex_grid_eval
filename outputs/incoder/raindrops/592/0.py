
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "Plang"
    else:
        return str(num)


# Problem #6
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), place "Fizz" instead of the number and for the multiples of five (buzz), place "Buzz" instead.
    And for the multiples of both three and five (fizzbuzz), place "FizzBuzz" instead.

    Examples:
    1 returns "1"
    2 returns "Fizz"
    3 returns "Fizz"
    4 returns "Buzz"
    5 returns "Buzz"
    15 returns "FizzBuzz"
    16 returns "FizzBuzz"
    17 returns "FizzBuzz"
    18 returns "FizzBuzz"
    19 returns "FizzBuzz"
    20 returns "FizzBuzz"
    21 returns "FizzBuzz"
    28 returns "FizzBuzz"
    29 returns "FizzBuzz"
    30 returns "FizzBuzz"
    31 returns "FizzBuzz"
    32 returns "FizzBuzz"
    33 returns "FizzBuzz"
    34 returns "FizzBuzz"
    35 returns "FizzBuzz"
    36 returns "FizzBuzz"
    37 returns "FizzBuzz"
    38 returns "FizzBuzz"
    39 returns "FizzBuzz"
    40 returns "FizzBuzz"
    41 returns "FizzBuzz"
    42 returns "FizzBuzz"
    43 returns "FizzBuzz"
    44 returns "FizzBuzz"
    45 returns "FizzBuzz"
    46 returns "FizzBuzz"
    47 returns "FizzBuzz"
    48 returns "FizzBuzz"
    49 returns "FizzBuzz"
    50 returns "FizzBuzz"
    51 returns "FizzBuzz"
    52 returns "FizzBuzz"
    53 returns "FizzBuzz"
    54 returns "Fizz