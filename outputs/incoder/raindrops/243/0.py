
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 11, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 5, so the result would be "Plong".
    55 has both 11 and 5 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 11, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    factors = []
    factors.append(num)
    factors.append(num % 11)
    factors.append(num % 5)
    factors.append(num % 7)
    factors.sort()
    factors.reverse()
    factors = factors[:3]
    factors = [str(x) for x in factors]
    factors = ''.join(factors)
    return factors


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to 100 in fizzbuzz order.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', followed by a space, and then the number itself.
    Each number should be preceded by 'Buzz', followed by a space, and then the number itself.
    Each number should be preceded by 'Fizz', 