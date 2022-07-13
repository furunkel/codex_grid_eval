
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Buzz".
    33 has both 3 and 11 as factors, but not 5, so the result would be "PlangPling".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    if num < 3:
        return str(num)
    elif num % 3 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to add any numbers that you do not know are multiples of three or five.

    Examples:
    1 becomes "1"
    2 becomes "2"
    3 becomes "Fizz"
    4 becomes "Fizz"
    5 becomes "Buzz"
    6 becomes "Buzz"
    7 becomes "Fizz"
    8 becomes "Fizz"
    9 becomes "Buzz"
    10 becomes "FizzBuzz"
    11 becomes "FizzBuzz"
    12 becomes "FizzBuzz"
    13 becomes "FizzBuzz"
    14 becomes "FizzBuzz"
    15 becomes "FizzBuzz"
    16 becomes "FizzBuzz"
    17 becomes "FizzBuzz"
    18 becomes "FizzBuzz"
    19 becomes "FizzBuzz"
    20 becomes "FizzBuzz"
    """
    if num < 3:
        return str(num)
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 3
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to add any numbers that you do not know are multiples of three or five.

    Examples:
    1 becomes "1"
    2 becomes "2"
    3 becomes "Fizz"
    4 becomes "Fizz"
    5 becomes "Buzz"
    6 becomes "Buzz"
    7 becomes "Fizz"
    8 becomes "Fizz"
    9 becomes "Buzz"
    