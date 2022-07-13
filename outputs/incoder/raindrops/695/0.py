
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Buzz".
    143 has both 13 and 11 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    if num == 0:
        return '0'
    factors = []
    factors.append(num % 13)
    factors.append(num % 11)
    factors.append(num % 5)
    factors.sort()
    factors.reverse()
    factors.insert(0, 0)
    factors.append(0)
    factors.insert(len(factors)-1, 0)
    factors.insert(len(factors)-2, 0)
    factors.insert(len(factors)-3, 0)
    factors.insert(len(factors)-4, 0)
    factors.insert(len(factors)-5, 0)
    factors.insert(len(factors)-6, 0)
    factors.insert(len(factors)-7, 0)
    factors.insert(len(factors)-8, 0)
    factors.insert(len(factors)-9, 0)
    factors.insert(len(factors)-10, 0)
    factors.insert(len(factors)-11, 0)
    factors.insert(len(factors)-12, 0)
    factors.insert(len(factors)-13, 0)
    factors.insert(len(factors)-14, 0)
    factors.insert(len(factors)-15, 0)
    factors.insert(len(factors)-16, 0)
    factors.insert(len(factors)-17, 0)
    factors.insert(len(factors)-18, 0)
    factors.insert(len(factors)-19, 0)
    factors.insert(len(factors)-20, 0)
    factors.insert(len(factors)-21, 0)
    factors.insert(len(factors)-22, 0)
    factors.insert(len(factors)-23, 0)
    factors.insert(len(factors)-24, 0)
    factors.insert(len(factors)-25, 0)
    factors.insert(len(factors)-26, 0)
    factors.insert(len(factors)-27, 0)
    factors.insert(len(factors)-28, 0)
    factors.insert(len(factors)-29, 0)
    factors.insert(len(factors)-30, 0)
    factors.insert(len(factors)-31, 0)
    factors.insert(len(factors)-32, 0)
    factors.insert(len(factors)-33, 0)
    factors.insert(len(factors)-34, 0)
    factors.insert(len(factors)-35, 0)
    factors.insert(len(factors)-36, 0)
    factors.insert(len(factors)-37, 0)
    factors.insert(len(factors)-38, 0)
    factors.insert(len(factors)-39, 0)
    factors.insert(len(factors)-40, 0)
    factors.insert(len(factors)-41, 0)
    factors.insert(len(factors)-42, 0)
    factors.insert(len(factor