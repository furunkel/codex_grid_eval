
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Buzz' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Buzz".
    65 has both 13 and 5 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num == 4:
        return '4'
    elif num == 5:
        return '5'
    elif num == 6:
        return '6'
    elif num == 7:
        return '7'
    elif num == 8:
        return '8'
    elif num == 9:
        return '9'
    elif num == 10:
        return '10'
    elif num == 11:
        return '11'
    elif num == 12:
        return '12'
    elif num == 13:
        return 'Pling'
    elif num == 14:
        return 'Plang'
    elif num == 15:
        return 'Buzz'
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if len(factors) == 0:
            return str(num)
        elif len(factors) == 1:
            return str(factors[0])
        else:
            return str(factors[0]) + str(factors[1])

# Cell
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz if a number is divisible by 3, Fizz if a number is divisible by 5, and Buzz if a number is divisible by both 3 and 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is divisible by 3, or 'Buzz' if a number is divisible by 5.
    Your function should return 'FizzBuzz' if a number is divisible by both 3 and 5, or 'Fizz' if a number is 