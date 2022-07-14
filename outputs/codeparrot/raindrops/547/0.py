def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plang".
    65 has both 13 and 5 as factors, but not 11, so the result would be "PlingBuzz".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num % 2 == 0:
        return str(num)
    if num % 2 == 1:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 2:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 3:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 4:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 5:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 6:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 7:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 8:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 9:
        return str(num/2) + ' ' + str(num%2)
    if num % 2 == 10:
        return str(num