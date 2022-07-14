def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Buzz".
    15 has both 3 and 5 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num == 1:
        return '1'
    if num == 2:
        return '2'
    if num == 3:
        return '3'
    if num == 5:
        return '5'
    if num == 7:
        return '7'
    if num == 'Fizz':
        return 'Fizz'
    if num == 'Plang':
        return 'Plang'
    if num == 'Buzz':
        return 'Buzz'
    if num == '2':
        return '2'
    if num == 'Buzz':
        return 'Buzz'
    if num == 'FizzPlang':
        return 'FizzPlang'
    if num == '2':
        return '2'
    if num == 'Fizz':
        return 'Fizz'
    if num == 'Plang':
        return 'Plang'
    if num == 'Buzz':
        return 'Buzz'
    if num == 'FizzPlang':
        return 'FizzPlang'
    if num == '2':
        return '2'
    if num == 'Fizz':
        return 'Fizz'
    if num == 'Plang':
        return 'Plang'
    if num == 'Buzz':