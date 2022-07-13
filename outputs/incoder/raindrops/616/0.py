
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plang".
    39 has both 13 and 3 as factors, but not 5, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    factors = []
    factors.append(num)
    factors.append(num % 3)
    factors.append(num % 5)
    factors.append(num % 13)
    factors.append(num % 17)
    factors.append(num % 21)
    factors.append(num % 25)
    factors.append(num % 29)
    factors.append(num % 31)
    factors.append(num % 37)
    factors.append(num % 41)
    factors.append(num % 45)
    factors.append(num % 49)
    factors.append(num % 51)
    factors.append(num % 55)
    factors.append(num % 59)
    factors.append(num % 61)
    factors.append(num % 65)
    factors.append(num % 69)
    factors.append(num % 71)
    factors.append(num % 75)
    factors.append(num % 79)
    factors.append(num % 81)
    factors.append(num % 85)
    factors.append(num % 89)
    factors.append(num % 91)
    factors.append(num % 95)
    factors.append(num % 99)
    factors.append(num % 101)
    factors.append(num % 105)
    factors.append(num % 109)
    factors.append(num % 113)
    factors.append(num % 117)
    factors.append(num % 121)
    factors.append(num % 125)
    factors.append(num % 129)
    factors.append(num % 131)
    factors.append(num % 135)
    factors.append(num % 139)
    factors.append(num % 143)
    factors.append(num % 147)
    factors.append(num % 151)
    factors.append(num % 155)
    factors.append(num % 159)
    factors.append(num % 163)
    factors.append(num % 167)
    factors.append(num % 171)
    factors.append(num % 175)
    factors.append(num % 179)
    factors.append(num % 183)
    factors.append(num % 187)
    factors.append(num % 191)
    factors.append(num % 195)
    factors.append(num % 199)
    factors.append(num % 203)
    factors.append(num % 207)
    factors.append(num % 211)
    factors.append(num % 215)
    factors.append(num % 219)
    factors.append(num % 223)
    factors.append(num % 227)
    factors.append(num % 231)
    factors.append(num % 235)
    factors.append(num