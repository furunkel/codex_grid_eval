
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Plang".
    33 has both 3 and 11 as factors, but not 5, so the result would be "FizzBuzz".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    if num % 3 == 0:
        return "Fizz"
    if num % 11 == 0:
        return "Buzz"
    if num % 5 == 0:
        return "Plang"
    return str(num)

# Test Cases
print(raindrops(10))
print(raindrops(33))
print(raindrops(2))
print(raindrops(1))
print(raindrops(0))
print(raindrops(-1))
print(raindrops(-3))
print(raindrops(-33))
print(raindrops(-333))
print(raindrops(-4444))
print(raindrops(-5555))
print(raindrops(-6666))
print(raindrops(-7777))
print(raindrops(-8888))
print(raindrops(-9999))
print(raindrops(-10000))
print(raindrops(-1000))
print(raindrops(-10000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(raindrops(-1000))
print(rain