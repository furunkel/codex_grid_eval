
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 13, 5, or 11, so the result would be "2".
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
        return "10"
    elif num == 11:
        return "11"
    elif num == 12:
        return "12"
    elif num == 13:
        return "Fizz"
    elif num == 14:
        return "Buzz"
    elif num == 15:
        return "FizzBuzz"
    else:
        factors = []
        factors.append(num)
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
        factors.append(num % 10000000000000000000000)
        factors.append(num % 100000000000000000000000)
        factors.append(num % 1000000000000000000000000)
        factors.append(num % 10000000000000000000000000)
        factors.append(num % 100000000000000000000000000)
        factors.append(num % 1000000000000000000000000000)
        factors.append(num % 10000000000000000000000000000)
        factors.append(num % 1000000000000000000000000000000)
        factors.append(num % 10000000000000000000000000000000)
        factors.append(num % 100000000000000000000000000000000)
        factors.append(num % 1000000000000000000000000000000000)
        factors.append(num % 10000000000000000000000000000000000)
        factors.append(num % 100000000000000000000000000000000000)
        factors.append(num % 1000000000000000000000000000000000000)
        factors.append(num % 100000000000000000000000000000000000000)
        factors.append(num % 1000000000000000000000000000000000000000)
        factors.append(num % 10000000000000000000000000000000000000000