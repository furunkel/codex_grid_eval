
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plang".
    65 has both 13 and 5 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    if num == 0:
        return "0"
    elif num == 1:
        return "1"
    elif num == 2:
        return "2"
    elif num == 3:
        return "3"
    elif num == 4:
        return "4"
    elif num == 5:
        return "5"
    elif num == 6:
        return "6"
    elif num == 7:
        return "7"
    elif num == 8:
        return "8"
    elif num == 9:
        return "9"
    elif num == 10:
        return "Buzz"
    elif num == 11:
        return "Plang"
    elif num == 12:
        return "Fizz"
    elif num == 13:
        return "FizzBuzz"
    else:
        factors = []
        for i in range(1, num + 1):
            if num % i == 0:
                factors.append(i)
        if num in factors:
            return "FizzBuzz"
        elif num in factors:
            return "Fizz"
        elif num in factors:
            return "Buzz"
        elif num in factors:
            return "Plang"
        else:
            return str(num)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz, Fizz, or Buzz depending on whether the number is divisible by 3, 5 or 7.
    You do not need to worry about numbers that are not divisible by 3, 5 or 7.

    Examples:
    12 returns "FizzBuzz".
    3 returns "Fizz".
    5 returns "Buzz".
    15 returns "FizzBuzz".
    21 returns "Fizz".
    37 returns "Buzz".
    81 returns "FizzBuzz".
    101 returns "Fizz".
    131 returns "Buzz".
    """
    if num % 3 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Buzz"
    elif num % 7 == 0:
        return "FizzBuzz"
    else:
        return str(num)


# Problem 9
def fizzbuzz2(num):
    """
    Your task is to convert a number into a string that contains the words FizzBuzz, Fizz, or Buzz depending on whether the number is divisible by 3, 5 or 7.
    You do not need to worry about numbers that are not divisible by 3, 5 or 7.

    Examples:
    12 returns "FizzBuzz".
    3 returns "Fizz".
    5 returns "Buzz".
    15 returns "FizzBuzz".
    21 returns "Fizz".
    37 returns "Buzz".
    81 