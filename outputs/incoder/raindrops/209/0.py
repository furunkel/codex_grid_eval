
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Buzz".
    33 has both 3 and 11 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    if num % 3 == 0 and num % 11 == 0 and num % 5 == 0:
        return "Buzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by 'Fizz' if the number is divisible by 3, otherwise it should be 'Buzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by 5, otherwise it should be 'Buzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'Fizz' if the number is divisible by both 3 and 5, otherwise it should be 'FizzBuzz'.