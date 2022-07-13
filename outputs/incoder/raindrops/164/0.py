
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Buzz".
    33 has both 3 and 11 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    factors = []
    if num % 3 == 0:
        factors.append('Pling')
    if num % 11 == 0:
        factors.append('Plang')
    if num % 7 == 0:
        factors.append('Buzz')
    if len(factors) == 0:
        return str(num)
    else:
        return ''.join(factors)


# Problem 2
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to add any numbers that end in 0, 2, 4, 5, 7, or 8.
    You do not need to consider negative numbers.
    You do not need to consider floats (except for 3.0).
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.
    You do not need to consider negative numbers.
    You do not need to consider floats.