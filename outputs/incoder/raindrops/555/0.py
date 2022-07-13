
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlangBuzz".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    if num == 3:
        return '3'
    if num == 4:
        return '4'
    if num == 5:
        return '5'
    if num == 6:
        return '6'
    if num == 7:
        return '7'
    if num == 8:
        return '8'
    if num == 9:
        return '9'
    if num == 10:
        return '10'
    if num == 11:
        return 'Plong'
    if num == 12:
        return 'Plang'
    if num == 13:
        return 'Buzz'
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                return 'BuzzPlang'
            else:
                return 'Buzz'
        else:
            if num % 5 == 0:
                return 'Plang'
            else:
                return 'Plong'
    else:
        if num % 3 == 0:
            return 'Plang'
        else:
            return 'Plong'


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'FizzBuzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 3 as a factor, but not 5 or 7, so the result would be "FizzBuzz".
    65 has both 3 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    if num == 3:
        return 'Fizz'
    if num == 4:
        return '4'
    if num == 5:
        return 'Buzz'
    if num == 6:
        return '6'
    if num == 7:
        return 'FizzBuzz'
    if num % 2 == 0:
        if num % 3 == 0:
            if num % 5 == 0:
                return 'FizzBuzz'
            else:
                return 'Fizz'
        else:
            if num % 5 == 0:
                return 'Buzz