
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    does not have any of 3, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 3 or 5, so the result would be "Plang".
    15 has both 3 and 5 as factors, but not 11, so the result would be "FizzBuzz".
    2 is not factored by 3, 5, or 11, so the result would be "2".
    """
    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    elif num % 3 == 0:
        return 'Fizz'
    elif num % 5 == 0:
        return 'Buzz'
    else:
        return str(num)

# Test Cases
print(raindrops(22))
print(raindrops(15))
print(raindrops(2))
print(raindrops(0))
print(raindrops(1))
print(raindrops(12))
print(raindrops(13))
print(raindrops(14))
print(raindrops(15))
print(raindrops(16))
print(raindrops(17))
print(raindrops(18))
print(raindrops(19))
print(raindrops(20))
print(raindrops(21))
print(raindrops(22))
print(raindrops(23))
print(raindrops(24))
print(raindrops(25))
print(raindrops(26))
print(raindrops(27))
print(raindrops(28))
print(raindrops(29))
print(raindrops(30))
print(raindrops(31))
print(raindrops(32))
print(raindrops(33))
print(raindrops(34))
print(raindrops(35))
print(raindrops(36))
print(raindrops(37))
print(raindrops(38))
print(raindrops(39))
print(raindrops(40))
print(raindrops(41))
print(raindrops(42))
print(raindrops(43))
print(raindrops(44))
print(raindrops(45))
print(raindrops(46))
print(raindrops(47))
print(raindrops(48))
print(raindrops(49))
print(raindrops(50))
print(raindrops(51))
print(raindrops(52))
print(raindrops(53))
print(raindrops(54))
print(raindrops(55))
print(raindrops(56))
print(raindrops(57))
print(raindrops(58))
print(raindrops(59))
print(raindrops(60))
print(raindrops(61))
print(raindrops(62))
print(raindrops(63))
print(raindrops(64))
print(raindrops(65))
print(raindrops(66))
print(raindrops(67))
print(raindrops(68))
print(raindrops(69))
print(raindrops(70))
print(raindrops(71))
print(raindrops(72))
print(raindrops(73))