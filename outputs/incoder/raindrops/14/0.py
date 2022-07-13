
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Buzz".
    15 has both 3 and 5 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 3:
        return 'Plang'
    elif len(factors) == 5:
        return 'Pling'
    elif len(factors) == 7:
        return 'Buzz'
    else:
        return str(num)


# Problem 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'Fizz' to the result, and for multiples of five (buzz), you append 'Buzz' to the result.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and seven.
    You do not need to worry about numbers which are multiples of both five and seven.
    You do not need to worry about numbers which are multiples of both five and three.
    You do not need to worry about numbers which are multiples of both seven and three.
    You do not need to worry about numbers which are multiples of both seven and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and seven.
    You do not need to worry about numbers which are multiples of both five and seven.
    You do not need to worry about numbers which are multiples of both five and three.
    You do not need to worry about numbers which are multiples of both seven and three.
    You do not need to worry about numbers which are multiples of both seven and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and seven.
    You do not need to worry about numbers which are multiples of both five and seven.
    You do not need to worry about numbers which are multiples of both five and three.
    You do not need to worry about numbers which are multiples of both seven and three.
    You do not need to worry about numbers which are multiples of both seven and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and seven.
    You do not need to worry about numbers which are multiples of both five and 