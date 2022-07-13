
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    factors = []
    if num % 13 == 0:
        factors.append('Plang')
    if num % 5 == 0:
        factors.append('Pling')
    if num % 7 == 0:
        factors.append('Plong')
    if len(factors) == 0:
        return str(num)
    else:
        return ''.join(factors)

# Cell
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by 'Fizz', followed by a space, followed by a 'Buzz', followed by a space, followed by a 'Fizz'.
    For example:
    1 should be 'Fizz Buzz Fizz'.
    3 should be 'Fizz Fizz Buzz'.
    21 should be 'Fizz Buzz Fizz Fizz Buzz'.
    etc.
    """
    string = ''
    if num % 15 == 0:
        string += 'Fizz'
    if num % 3 == 0:
        string += ' Buzz'
    if num % 5 == 0:
        string += ' Fizz'
    return string

# Cell
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by 'Fizz', followed by a space, followed by a 'Buzz', followed by a space, followed by a 'Fizz'.
    For example:
    1 should be 'Fizz Buzz Fizz'.
    3 should be 'Fizz Fizz Buzz'.
    21 should be 'Fizz Buzz Fizz Fizz Buzz'.
    etc.
    """
    string = ''
    if num % 15 == 0:
        string += 'Fizz'
    if num % 3 == 0:
        string += ' Buzz'
    if num % 5 == 0:
        string += ' Fizz'
    return string

# Cell
def fizzbuzz3(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    Each number should be preceded by 'Fizz', followed by a space, followed by a 'Buzz', followed by a space, followed by a 'Fizz'.
    For example:
    1 should be 'Fizz Buzz Fizz'.
    3 should be 'Fizz Fizz Buzz'.
    21 should be 'Fizz Buzz Fizz Fizz Buzz'.
    etc.
    """
    string = ''
    if num % 15 == 0:
        string += 'Fizz'
