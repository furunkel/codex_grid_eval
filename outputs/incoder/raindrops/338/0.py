
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Buzz".
    33 has both 11 and 3 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 11, 3, or 7, so the result would be "2".
    """
    if num == 0:
        return "0"
    factors = []
    factors.append(num % 10)
    factors.append(num % 100)
    factors.append(num % 1000)
    factors.append(num % 10000)
    factors.append(num % 100000)
    factors.append(num % 1000000)
    factors.append(num % 10000000)
    factors.append(num % 100000000)
    factors.append(num % 1000000000)
    factors.append(num % 10000000000)
    factors.append(num % 100000000000)
    factors.append(num % 1000000000000)
    factors.append(num % 1000000000000)
    factors.append(num % 10000000000000)
    factors.append(num % 100000000000000)
    factors.append(num % 1000000000000000)
    factors.append(num % 10000000000000000)
    factors.append(num % 100000000000000000)
    factors.append(num % 1000000000000000000)
    factors.append(num % 10000000000000000000)
    factors.append(num % 100000000000000000000)
    factors.append(num % 1000000000000000000000)
    factors.append(num % 10000000000000000000000)
    factors.append(num % 100000000000000000000000)
    factors.append(num % 1000000000000000000000000)
    factors.append(num % 10000000000000000000000000)
    factors.append(num % 100000000000000000000000000)
    factors.append(num % 1000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000000000000000)
    factors.append(num % 10000000000000000000000000000000000000000000000)
    factors.append(num % 100000000000000000000000000000000000000000000000)
    factors.append(num % 1000000000000000000000000000000000000000000000000)
    factors.append(num % 100