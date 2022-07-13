
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Buzz".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Pling"
    elif num % 11 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 4
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced by the word FizzBuzz if it is divisible by 3, otherwise it should be replaced by the word Fizz
    or Buzz.

    Examples:
    1 should be replaced by FizzBuzz.
    3 should be replaced by FizzBuzz.
    5 should be replaced by Buzz.
    15 should be replaced by Fizz.
    21 should be replaced by FizzBuzz.
    37 should be replaced by FizzBuzz.
    63 should be replaced by Buzz.
    """
    if num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 5
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced by the word FizzBuzz if it is divisible by 3, otherwise it should be replaced by the word Fizz
    or Buzz.

    Examples:
    1 should be replaced by FizzBuzz.
    3 should be replaced by FizzBuzz.
    5 should be replaced by Buzz.
    15 should be replaced by Fizz.
    21 should be replaced by FizzBuzz.
    37 should be replaced by FizzBuzz.
    63 should be replaced by Buzz.
    """
    if num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 6
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced by the word FizzBuzz if it is divisible by 3, otherwise it should be replaced by the word Fizz
    or Buzz.

    Examples:
    1 should be replaced by FizzBuzz.
    3 should be replaced by FizzBuzz.
    5 should be replaced by Buzz.
    15 should be replaced by Fizz.
    21 should be replaced by FizzBuzz.
    37 should be replaced by FizzBuzz.
    63 should be replaced by Buzz.
    """
    if num