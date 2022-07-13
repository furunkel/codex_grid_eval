
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 5, so the result would be "PlingPlang".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    factors = [11, 3, 5]
    factors_str = ['Pling', 'Plang', 'Plong']
    if num in factors:
        return factors_str[factors.index(num)]
    else:
        return str(num)


def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, 7, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 3 as a factor, but not 5, so the result would be "Buzz".
    33 has both 3 and 5 as factors, but not 7, so the result would be "BuzzBuzz".
    2 is not factored by 3, 5, 7, or 11, so the result would be "2".
    """
    factors = [3, 5, 7, 11]
    factors_str = ['Buzz', 'Buzz', 'Buzz', 'Buzz']
    if num in factors:
        return factors_str[factors.index(num)]
    else:
        return str(num)


def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains fizzbuzz sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of fizzbuzz are that if a given number:

    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, 7, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 3 as a factor, but not 5, so the result would be "Buzz".
    33 has both 3 and 5 as factors, but not 7, so the result would be "BuzzBuzz".
    2 is not factored by 3, 5, 7, or 11, so the result would be "2