
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "PlangPling".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    factors = []
    factors.append(num)
    factors.append(num % 13)
    factors.append(num % 3)
    factors.append(num % 5)
    factors.sort()
    factors.reverse()
    factors = [str(x) for x in factors]
    factors = ''.join(factors)
    return factors

def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the word "Fizz" if the number is divisible by 3, the word "Buzz" if the number is divisible by 5, and the word "FizzBuzz" if the number is divisible by both 3 and 5.

    Examples:
    10 would return "FizzBuzz".
    20 would return "Buzz".
    30 would return "Fizz".
    40 would return "Fizz".
    50 would return "Buzz".
    60 would return "Buzz".
    70 would return "FizzBuzz".
    80 would return "Fizz".
    90 would return "Fizz".
    100 would return "Fizz".
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
    Your task is to convert a number into a string that contains the word "Fizz" if the number is divisible by 3, the word "Buzz" if the number is divisible by 5, and the word "FizzBuzz" if the number is divisible by both 3 and 5.

    Examples:
    10 would return "FizzBuzz".
    20 would return "Buzz".
    30 would return "Fizz".
    40 would return "Fizz".
    50 would return "Buzz".
    60 would return "Buzz".
    70 would return "FizzBuzz".
    80 would return "Fizz".
    90 would return "Fizz".
    100 would return "Fizz".
    """
    if num % 3 == 0 and num % 5 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0: