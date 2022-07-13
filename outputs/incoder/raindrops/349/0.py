
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 11, 3, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 11 or 3, so the result would be "Plang".
    33 has both 11 and 3 as factors, but not 7, so the result would be "FizzBuzz".
    2 is not factored by 11, 3, or 7, so the result would be "2".
    """
    if num < 1:
        return ""
    factors = []
    factors.append(num % 10)
    factors.append(num % 3)
    factors.append(num % 7)
    factors.append(num % 11)
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
    factors.append(num % 107)
    factors.append(num % 113)
    factors.append(num % 127)
    factors.append(num % 131)
    factors.append(num % 137)
    factors.append(num % 143)
    factors.append(num % 147)
    factors.append(num % 151)
    factors.append(num % 157)
    factors.append(num % 163)
    factors.append(num % 167)
    factors.append(num % 173)
    factors.append(num % 177)
    factors.append(num % 183)
    factors.append(num % 187)
    factors.append(num % 193)
    factors.append(num % 197)
    factors.append(num % 203)
    factors.append(num % 207)
    factors.append(num % 213)
    factors.append(num % 217)
    factors.append(num % 223)
    factors.append(num % 227)
    factors.append(num % 233)
    factors.append(num % 237)
    factors.append(num % 243)
    factors.append(num % 247)
    factors.append(num % 251)
    factors.append(num % 257)
    factors.append(num % 263)
    factors.append(num % 267)
    factors.append(num % 273)
    factors.append(num % 277)
    factors.append(num % 283)
    factors.append(num % 287)
    factors.append(num % 293)
    factors.append(num % 297)
    factors.append(num % 303)
    factors.append(num % 307)
    factors.append(num