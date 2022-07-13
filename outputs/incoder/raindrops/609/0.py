
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "PlangBuzz".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Plang"
    if num % 3 == 0:
        return "Buzz"
    if num % 5 == 0:
        return "Plong"
    return str(num)


# Question 3
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the word "Fizz" if the number is divisible by 3, the word "Buzz" if the number is divisible by 5, and the word "FizzBuzz" if the number is divisible by both 3 and 5.

    Examples:
    10 would result in "FizzBuzz".
    20 would result in "Buzz".
    30 would result in "Fizz".
    40 would result in "Fizz".
    50 would result in "Buzz".
    60 would result in "Buzz".
    70 would result in "FizzBuzz".
    80 would result in "Fizz".
    90 would result in "Fizz".
    100 would result in "Fizz".
    """
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return "FizzBuzz"


# Question 4
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the word "Fizz" if the number is divisible by 3, the word "Buzz" if the number is divisible by 5, and the word "FizzBuzz" if the number is divisible by both 3 and 5.

    Examples:
    10 would result in "FizzBuzz".
    20 would result in "Buzz".
    30 would result in "Fizz".
    40 would result in "Fizz".
    50 would result in "Buzz".
    60 would result in "Buzz".
    70 would result in "FizzBuzz".
    80 would result in "Fizz".
    90 would result in "Fizz".
    100 would result in "Fizz".
    """
    if num % 3 == 0:
        return "Fizz"
    if num % 5 == 0:
        return "Buzz"
    return "FizzBuzz"


# Question 5
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the word "Fizz" if the number is divisible by 3, the word "Buzz" if the number is divisible by 5, and the word "FizzBuzz" if the number is divisible by both 3 and 5.

    Examples:
    10 would result in "FizzBuzz".
    20 would result in "Buzz".
    30 