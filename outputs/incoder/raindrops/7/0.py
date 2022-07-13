
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Plang".
    15 has both 3 and 5 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num == 3:
        return "Pling"
    if num == 5:
        return "Buzz"
    if num == 7:
        return "Plang"
    factors = []
    factors.append(num)
    while num != 1:
        factors.append(num % 10)
        num = num // 10
    factors.append(num)
    factors.sort()
    factors.reverse()
    factors = factors[:3]
    factors = [str(x) for x in factors]
    factors = "".join(factors)
    return factors


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if num is divisible by 3, Fizz if num is divisible by 5, and Buzz if num is divisible by 7.

    You can assume that the input is a positive integer.
    """
    if num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Fizz"
    if num % 7 == 0:
        return "Buzz"
    return "Not divisible by 3, 5 or 7"


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if num is divisible by 3, Fizz if num is divisible by 5, and Buzz if num is divisible by 7.

    You can assume that the input is a positive integer.
    """
    if num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Fizz"
    if num % 7 == 0:
        return "Buzz"
    return "Not divisible by 3, 5 or 7"


def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if num is divisible by 3, Fizz if num is divisible by 5, and Buzz if num is divisible by 7.

    You can assume that the input is a positive integer.
    """
    if num % 3 == 0:
        return "FizzBuzz"
    if num % 5 == 0:
        return "Fizz"
    if num % 7 == 0:
        return "Buzz"
    return "Not divisible by 3, 5 or 7"


def fizzbuzz4(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if num is divisible by 3, Fizz if num is divisible by 5, and Buzz if num is divisible by 7.

    You can assume that the input is a positive integer.
