
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Buzz".
    15 has both 3 and 5 as factors, but not 11, so the result would be "PlingPlang".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Buzz"
    else:
        return str(num)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (ie. 3, 6, 9, 12, ...), you append 'Fizz' to the result, and for the multiples of five (ie. 5, 10, 15, ...), you append 'Buzz' to the result.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    You do not need to worry about numbers which are multiples of both three and five.
    