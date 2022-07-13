
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "PlingPlang".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Pling"
    elif num % 3 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(10))
print(raindrops(39))
print(raindrops(2))
print(raindrops(100))
print(raindrops(1000))
print(raindrops(10000))
print(raindrops(100000))
print(raindrops(1000000))
print(raindrops(10000000))
print(raindrops(100000000))
print(raindrops(1000000000))
print(raindrops(10000000000))
print(raindrops(100000000000))
print(raindrops(1000000000000))
print(raindrops(10000000000000))
print(raindrops(100000000000000))
print(raindrops(1000000000000000))
print(raindrops(10000000000000000))
print(raindrops(100000000000000000))
print(raindrops(1000000000000000000))
print(raindrops(10000000000000000000))
print(raindrops(100000000000000000000))
print(raindrops(1000000000000000000000))
print(raindrops(10000000000000000000000))
print(raindrops(100000000000000000000000))
print(raindrops(1000000000000000000000000))
print(raindrops(10000000000000000000000000))
print(raindrops(100000000000000000000000000))
print(raindrops(1000000000000000000000000000))
print(raindrops(10000000000000000000000000000))
print(raindrops(100000000000000000000000000000))
print(raindrops(1000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000000000000000))
print(raindrops(10000000000000000000000000000000000000000000000))
print(raindrops(100000000000000000000000000000000000000000000000))
print(raindrops(1000000000000000000000000000000000000000000000000))
print(raindrops(1000000000000000000