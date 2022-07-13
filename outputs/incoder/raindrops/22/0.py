
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Plang".
    15 has both 3 and 5 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num % 3 == 0 and num % 5 == 0 and num % 7 == 0:
        return "FizzPling"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Pling"
    elif num % 7 == 0:
        return "Plang"
    else:
        return str(num)


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three or 5, you should add 'Fizz' to the result, and for multiples of 7 you should add 'Buzz'.
    For example, num = 3 should result in 'Fizz', not '3'.
    Similarly, num = 15 should result in 'Buzz', not '15'.
    However, if num is divisible by both 3 and 5, you should add both 'Fizz' and 'Buzz'.
    For example, num = 7 should result in 'FizzBuzz', not '7'.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three or 5, you should add 'Fizz' to the result, and for multiples of 7 you should add 'Buzz'.
    For example, num = 3 should result in 'Fizz', not '3'.
    Similarly, num = 15 should result in 'Buzz', not '15'.
    However, if num is divisible by both 3 and 5, you should add both 'Fizz' and 'Buzz'.
    For example, num = 7 should result in 'FizzBuzz', not '7'.
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "FizzBuzz"
    else:
        return str(num)


def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three or 5, you should add 'Fizz' to the result, and for multiples of 7 you should add 'Buzz'.
    For example, num = 3 should result in 'Fizz', not '3'.
    Similarly, num = 15 should result in 'Buzz', not '15'.
    However, if num is divisible by 