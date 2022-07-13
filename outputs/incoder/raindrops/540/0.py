
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlingPlang".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)


# Problem 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 20.

    Examples:
    15 would result in "FizzBuzz".
    21 would result in "Buzz".
    37 would result in "Fizz".
    50 would result in "BuzzBuzz".
    """
    if num % 3 == 0:
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
    You do not need to worry about numbers like 15 or 20.

    Examples:
    15 would result in "FizzBuzz".
    21 would result in "Buzz".
    37 would result in "Fizz".
    50 would result in "BuzzBuzz".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num) + "FizzBuzz"


# Problem 4
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 20.

    Examples:
    15 would result in "FizzBuzz".
    21 would result in "Buzz".
    37 would result in "Fizz".
    50 would result in "BuzzBuzz".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num) + "FizzBuzz"


# Problem 5
def 