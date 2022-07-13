
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 11, 3, or 7, so the result would be "2".
    """
    if num % 11 == 0:
        return 'Pling'
    elif num % 3 == 0:
        return 'Plang'
    elif num % 7 == 0:
        return 'Buzz'
    else:
        return str(num)


# Problem 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (but not for five or ten), output "Fizz" instead of the number and for the multiples of five (but not for nine), output "Buzz".
    And for the multiples of both three and five, output "FizzBuzz".
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)


# Problem 6
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (but not for five or ten), output "Fizz" instead of the number and for the multiples of five (but not for nine), output "Buzz".
    And for the multiples of both three and five, output "FizzBuzz".
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'
    else:
        return str(num)


# Problem 7
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (but not for five or ten), output "Fizz" instead of the number and for the multiples of five (but not for nine), output "Buzz".
    And for the multiples of both three and five, output "FizzBuzz".
    """
    if num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    elif num % 15 == 0:
        return 'FizzBu