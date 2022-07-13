
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Plang' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 5, so the result would be "PlangPling".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num == 0:
        return '0'
    factors = []
    factors.append(num % 11)
    factors.append(num % 3)
    factors.append(num % 5)
    factors.append(num % 7)
    factors.append(num % 9)
    factors.append(num % 13)
    factors.append(num % 17)
    factors.append(num % 21)
    factors.append(num % 25)
    factors.append(num % 29)
    factors.append(num % 31)
    factors.append(num % 37)
    factors.append(num % 41)
    factors.append(num % 47)
    factors.append(num % 51)
    factors.append(num % 57)
    factors.append(num % 61)
    factors.append(num % 67)
    factors.append(num % 71)
    factors.append(num % 77)
    factors.append(num % 81)
    factors.append(num % 87)
    factors.append(num % 91)
    factors.append(num % 97)
    factors.append(num % 101)
    factors.append(num % 103)
    factors.append(num % 105)
    factors.append(num % 107)
    factors.append(num % 109)
    factors.append(num % 111)
    factors.append(num % 113)
    factors.append(num % 115)
    factors.append(num % 117)
    factors.append(num % 119)
    factors.append(num % 121)
    factors.append(num % 123)
    factors.append(num % 125)
    factors.append(num % 127)
    factors.append(num % 129)
    factors.append(num % 131)
    factors.append(num % 133)
    factors.append(num % 135)
    factors.append(num % 137)
    factors.append(num % 139)
    factors.append(num % 141)
    factors.append(num % 143)
    factors.append(num % 145)
    factors.append(num % 147)
    factors.append(num % 149)
    factors.append(num % 151)
    factors.append(num % 153)
    factors.append(num % 155)
    factors.append(num % 157)
    factors.append(num % 159)
    factors.append(num % 161)
    factors.append(num % 163)
    factors.append(num % 165)
    factors.append(num % 167)
    factors.append(num % 169)
    factors.append(num % 171)
    factors.append(num % 173)
    factors.append(num % 175)
    factors.append(num % 177)
    factors.append(num % 179)