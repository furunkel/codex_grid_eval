
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    factors = []
    if num % 3 == 0:
        factors.append('Fizz')
    if num % 11 == 0:
        factors.append('Pling')
    if num % 7 == 0:
        factors.append('Plong')
    if num in factors:
        return num
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(33))
print(raindrops(2))
print(raindrops(7))
print(raindrops(12))
print(raindrops(25))
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
print(raindrops(100