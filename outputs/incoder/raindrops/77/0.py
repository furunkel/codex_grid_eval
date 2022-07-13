
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Buzz".
    15 has both 3 and 5 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Pling"
    if num % 11 == 0:
        return "Buzz"
    factors = []
    factors.append(num % 3)
    factors.append(num % 5)
    factors.append(num % 11)
    factors.sort()
    factors.reverse()
    factors = factors[:3]
    factors = factors + ["Fizz", "Pling", "Buzz"]
    return "".join(factors)


# Problem 4
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (ie. 3, 6, 9, 12, ...), you append 'Fizz' to the result, and for multiples of five (ie. 5, 10, 15, 20, ...), you append 'Buzz' to the result.
    You do not need to worry about numbers which are multiples of both three and five.

    Examples:
    1 returns "1"
    2 returns "2"
    3 returns "Fizz"
    4 returns "Buzz"
    5 returns "Buzz"
    6 returns "Fizz"
    7 returns "Fizz"
    8 returns "Buzz"
    9 returns "Fizz"
    10 returns "Buzz"
    11 returns "FizzBuzz"
    12 returns "Fizz"
    13 returns "Fizz"
    14 returns "Buzz"
    15 returns "Fizz"
    16 returns "Fizz"
    17 returns "Buzz"
    18 returns "Fizz"
    19 returns "Fizz"
    20 returns "Buzz"
    21 returns "Fizz"
    22 returns "Fizz"
    23 returns "Buzz"
    24 returns "Fizz"
    25 returns "Fizz"
    26 returns "Buzz"
    27 returns "Fizz"
    28 returns "Fizz"
    29 returns "Buzz"
    30 returns "Fizz"
    31 returns "Fizz"
    32 returns "Buzz"
    33 returns "Fizz"
    34 returns "Fizz"
    35 returns "Buzz"
    36 returns "Fizz"
    37 returns "Fizz"