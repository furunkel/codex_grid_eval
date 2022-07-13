
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Pling"
    elif num % 3 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'Fizz' to the result, and for multiples of five (buzz), you append 'Buzz' to the result.
    You do not need to check for factors or use any sort of modulus operation.

    Examples:
    1 becomes '1', because 1 is a multiple of both 3 and 5.
    2 becomes '2', because 2 is a multiple of both 3 and 5.
    3 becomes 'Fizz', because 3 is a multiple of both 3 and 5.
    4 becomes 'Fizz', because 4 is a multiple of both 3 and 5.
    5 becomes 'Buzz', because 5 is a multiple of both 3 and 5.
    15 becomes 'FizzBuzz', because 15 is a multiple of both 3 and 5.
    16 becomes 'Fizz', because 16 is a multiple of both 3 and 5.
    17 becomes 'Buzz', because 17 is a multiple of both 3 and 5.
    21 becomes 'Fizz', because 21 is a multiple of both 3 and 5.
    28 becomes 'Fizz', because 28 is a multiple of both 3 and 5.
    37 becomes 'Buzz', because 37 is a multiple of both 3 and 5.
    123 becomes 'FizzBuzz', because 123 is a multiple of both 3 and 5.
    124 becomes 'Fizz', because 124 is a multiple of both 3 and 5.
    125 becomes 'Buzz', because 125 is a multiple of both 3 and 5.
    254 becomes 'Fizz', because 254 is a multiple of both 3 and 5.
    257 becomes 'Fizz', because 257 is a multiple of both 3 and 5.
    258 becomes 'Buzz', because 258 is a multiple of both 3 and 5.
    65535 becomes 'FizzBuzz', because 65535 is a multiple of both 3 and 5.
    65536 becomes 'Fizz', because 65536 is a multiple of both 3 and 5.
    65537 becomes 'Buzz', because 65537 is a multiple of both 3 and 5.
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 9
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'F