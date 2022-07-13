
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)

# Write your tests here
assert raindrops(14) == "Plong"
assert raindrops(65) == "PlingPlang"
assert raindrops(2) == "2"
assert raindrops(10) == "PlongPlang"
assert raindrops(100) == "PlingPlangPlong"
assert raindrops(1000) == "PlingPlangPlongPlang"
assert raindrops(10000) == "PlingPlangPlongPlangPlong"
assert raindrops(100000) == "PlingPlangPlongPlangPlongPlang"
assert raindrops(1000000) == "PlingPlangPlongPlangPlongPlangPlong"
assert raindrops(10000000) == "PlingPlangPlongPlangPlongPlangPlongPlang"
assert raindrops(100000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlong"
assert raindrops(1000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlang"
assert raindrops(10000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlong"
assert raindrops(100000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlang"
assert raindrops(1000000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlong"
assert raindrops(10000000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlang"
assert raindrops(100000000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlong"
assert raindrops(1000000000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlang"
assert raindrops(10000000000000000) == "PlingPlangPlongPlangPlongPlangPlongPlangPlongPlangPlongPlangP