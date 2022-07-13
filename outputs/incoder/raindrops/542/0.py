
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Buzz".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlingPlang".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return 'Buzz'
    elif num == 11:
        return 'Pling'
    elif num == 12:
        return 'Plang'
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if 13 in factors:
            factors.append(13)
        if 5 in factors:
            factors.append(5)
        if 11 in factors:
            factors.append(11)
        factors.sort()
        result = ''
        for i in factors:
            result += str(i)
        return result


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be replaced with 'Fizz' if it is divisible by 3, 'Buzz' if it is divisible by 5
    and 'FizzBuzz' if it is divisible by both.

    Examples:
    1 should be replaced with 'Fizz'.
    3 should be replaced with 'Fizz'.
    5 should be replaced with 'Buzz'.
    15 should be replaced with 'FizzBuzz'.
    21 should be replaced with 'FizzBuzz'.
    37 should be replaced with 'FizzBuzz'.
    63 should be replaced with 'FizzBuzz'.
    123 should be replaced with 'FizzBuzz'.
    """
    if num == 0:
        return '0'
    elif num == 1:
        return 'Fizz'
    elif num == 2:
        return 'Buzz'
    elif num == 3:
        return 'Fizz'
    elif num == 4:
        return 'Buzz'
    elif num == 5:
        return 'Fizz'
    elif num == 6:
        return 'Buzz'
    elif num == 7:
        return 'Fizz'
    elif num == 8:
        return 'Buzz'
    elif num == 9:
        return 'Fizz'
    elif num == 10:
        return 'Buzz'
    elif num == 11:
        return 'Fizz'
    elif num == 12:
        return 'Buzz'
    elif num == 13:
        return 'Fizz'
    elif num == 14:
        return 'Buzz'
    elif num == 15:
        return 'FizzBuzz'
    elif num == 16:
        return 'Buzz'
