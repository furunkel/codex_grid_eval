
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz.
    When a number is divisible by 3, the word Fizz is added to the string.
    When a number is divisible by 5, the word Buzz is added to the string.
    When a number is divisible by both 3 and 5, the word FizzBuzz is added to the string.
    When a number is not divisible by 3 or 5, the word Number is added to the string.

    Examples:
    12 returns "FizzBuzz".
    21 returns "FizzBuzz".
    37 returns "FizzBuzz".
    21 returns "Buzz".
    37 returns "Fizz".
    37 returns "Buzz".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "FizzBuzz"
    else:
        return "Number"


# Problem 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz.
    When a number is divisible by 3, the word Fizz is added to the string.
    When a number is divisible by 5, the word Buzz is added to the string.
    When a number is divisible by both 3 and 5, the word FizzBuzz is added to the string.
    When a number is not divisible by 3 or 5, the word Number is added to the string.

    Examples:
    12 returns "FizzBuzz".
    21 returns "FizzBuzz".
    37 returns "FizzBuzz".
    21 returns "Buzz".
    37 returns "Fizz".
    37 returns "Buzz".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "FizzBuzz"
    elif num % 5 == 0:
        return "FizzBuzz"
    else:
        return "Number"


# Problem 7
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz.
    When a number is divisible by 3, the word Fizz is added to the string.
    When a number is divisible by 5, the word 