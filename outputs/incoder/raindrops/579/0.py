
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 7, so the result would be "PlangPling".
    2 is not factored by 13, 3, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return 'Plang'
    elif num % 3 == 0:
        return 'Pling'
    elif num % 7 == 0:
        return 'Plong'
    else:
        return str(num)


# Problem 5
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'Fizz' to the result, and for multiples of five (buzz), you append 'Buzz' to the result.
    You do not need to worry about numbers like 15 or 20.
    You do not need to worry about numbers like 1 or 0.
    You do not need to worry about negative numbers.
    You do not need to worry about numbers greater than 100.
    You do not need to worry about numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5.
    You do not need to worry about numbers divisible by both 3 and 5, and numbers divisible by both 3 and 5, and numbers 