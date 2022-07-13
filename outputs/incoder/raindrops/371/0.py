
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num == 0:
        return "0"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                return "Buzz"
            else:
                return "Fizz"
        else:
            return "Plang"
    else:
        if num % 3 == 0:
            return "Fizz"
        else:
            return "Plang"


# Problem 4
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz.
    You will need to use the following rules:

    If num is divisible by 3, return "Fizz".
    If num is divisible by 5, return "Buzz".
    If num is divisible by both 3 and 5, return "FizzBuzz".
    If num is divisible by neither 3 nor 5, return "FizzBuzz".
    If num is not divisible by either 3 or 5, return "FizzBuzz".
    """
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    if num