def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    if num % 2 == 0:
        return str(num)
    if num % 3 == 0:
        return str(num) + ' ' + str(num / 3)
    if num % 5 == 0:
        return str(num) + ' ' + str(num / 5)
    if num % 7 == 0:
        return str(num) + ' ' + str(num / 7)
    if num % 11 == 0:
        return str(num) + ' ' + str(num / 11)
    if num % 13 == 0:
        return str(num) + ' ' + str(num / 13)
    if num % 17 == 0:
        return str(num) + ' ' + str(num / 17)
    if num % 19 == 0:
        return str(num) + ' ' + str(num / 19)
    if num % 20 == 0:
        return str(num) + ' ' + str(num / 20)
    if num % 21 == 0:
        return str(num) + ' ' + str(num / 21)
    if num % 23 == 0:
        return str(num) + ' ' + str(num / 23)
    if num % 24 == 0