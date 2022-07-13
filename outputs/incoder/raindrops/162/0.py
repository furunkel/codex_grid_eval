
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 3, 11, or 7, so the result would be "2".
    """
    if num % 3 == 0:
        return 'Pling'
    elif num % 11 == 0:
        return 'Plang'
    elif num % 7 == 0:
        return 'Plong'
    else:
        return str(num)

# Write your tests here
assert raindrops(14) == 'Plong'
assert raindrops(33) == 'PlingPlang'
assert raindrops(2) == '2'
assert raindrops(10) == 'Plong'
assert raindrops(100) == 'PlangPlingPlong'
assert raindrops(1000) == 'PlangPlingPlong'
assert raindrops(10000) == 'PlangPlingPlong'
assert raindrops(100000) == 'PlangPlingPlong'
assert raindrops(1000000) == 'PlangPlingPlong'
assert raindrops(10000000) == 'PlangPlingPlong'
assert raindrops(100000000) == 'PlangPlingPlong'
assert raindrops(1000000000) == 'PlangPlingPlong'
assert raindrops(10000000000) == 'PlangPlingPlong'
assert raindrops(100000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000000000000000) == 'PlangPlingPlong'
assert raindrops(1000000000000000000000000000) == 'PlangPlingPlong'
assert raindrops(10000000000000000000000000000) == 'PlangPlingPlong'
assert raindrops(100000000000000000000000000000