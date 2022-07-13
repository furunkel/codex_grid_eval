
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plang".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num % 3 == 0 and num % 11 == 0 and num % 7 == 0:
        return "FizzBuzz"
    elif num % 3 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "Plang"
    else:
        return str(num)


# Problem 3
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by 'Fizz' if the number is divisible by 3, otherwise it should be 'Buzz'.
    Each number should be preceded by 'FizzBuzz' if the number is divisible by both 3 and 11, otherwise it should be 'FizzBuzz'.
    Each number should be preceded by 'FizzBuzzPlang' if the number is divisible by both 3 and 11, 7 and 3, otherwise it should be 'FizzBuzzPlang'.
    Each number should be preceded by 'FizzBuzzPlangFizz' if the number is divisible by all three factors, otherwise it should be 'FizzBuzzPlangFizz'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzz' if the number is divisible by all three factors, 11 and 7, otherwise it should be 'FizzBuzzPlangFizzBuzz'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzzPlang' if the number is divisible by all three factors, 11, 7, and 3, otherwise it should be 'FizzBuzzPlangFizzBuzzPlang'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzzPlangFizz' if the number is divisible by all three factors, 11, 7, and 3, 11, otherwise it should be 'FizzBuzzPlangFizzBuzzPlangFizz'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzzPlangFizzBuzz' if the number is divisible by all three factors, 11, 7, and 3, 11, 7, otherwise it should be 'FizzBuzzPlangFizzBuzzPlangFizzBuzz'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzzPlangFizzBuzzPlang' if the number is divisible by all three factors, 11, 7, and 3, 11, 7, 3, otherwise it should be 'FizzBuzzPlangFizzBuzzPlangFizzBuzzPlang'.
    Each number should be preceded by 'FizzBuzzPlangFizzBuzzPlangF