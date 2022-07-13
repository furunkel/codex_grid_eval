
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    factors = []
    if num % 3 == 0:
        factors.append('Fizz')
    if num % 11 == 0:
        factors.append('Plang')
    if num % 5 == 0:
        factors.append('Plong')
    if len(factors) == 0:
        return str(num)
    else:
        return ''.join(factors)

# Cell
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three ('Fizz') you append 'Fizz' to the result, and for multiples of five ('Buzz') you append 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 20.
    You do not need to worry about numbers like 1 or 0.
    You do not need to worry about negative numbers.
    You do not need to worry about numbers greater than num.
    You do not need to worry about numbers less than 1.
    You do not need to worry about numbers less than 0.
    You do not need to worry about numbers greater than or equal to num.
    You do not need to worry about numbers greater than or equal to 1.
    You do not need to worry about numbers greater than or equal to 0.
    You do not need to worry about negative numbers.
    You do not need to worry about numbers greater than or equal to num.
    You do not need to worry about numbers greater than or equal to 1.
    You do not need to worry about numbers greater than or equal to 0.
    You do not need to worry about numbers less than or equal to num.
    You do not need to worry about numbers less than or equal to 1.
    You do not need to worry about numbers less than or equal to 0.
    You do not need to worry about numbers greater than or equal to num.
    You do not need to worry about numbers greater than or equal to 1.
    You do not need to worry about numbers greater than or equal to 0.
    You do not need to worry about numbers less than or equal to num.
    You do not need to worry about numbers less than or equal to 1.
    You do not need to worry about numbers less than or equal to 0.
    You do not need to worry about numbers greater than or equal to num.
    You do not need to worry about numbers greater than or equal to 1.
    You do not need to worry about numbers greater than or equal to 0.
    You do not need to worry about numbers less than or equal to num.
    You do not need to worry about numbers less than or equal to 1.
    You do not need to worry about numbers less than or equal to 0.
    You do not need to worry about numbers greater than or equal to num.
    You do not need to worry about numbers greater than or equal to 1.
    You 