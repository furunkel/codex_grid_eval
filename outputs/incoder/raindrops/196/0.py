
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Plang".
    33 has both 3 and 11 as factors, but not 5, so the result would be "PlingBuzz".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    if num % 3 == 0:
        return 'Pling'
    elif num % 11 == 0:
        return 'Buzz'
    elif num % 5 == 0:
        return 'Plang'
    else:
        return str(num)

# Write your tests here
def test_raindrops():
    assert raindrops(10) == 'Plang'
    assert raindrops(33) == 'PlingBuzz'
    assert raindrops(2) == '2'

def test_raindrops_fail():
    assert raindrops(0) == '0'
    assert raindrops(-1) == '-1'
    assert raindrops(2) == '2'
    assert raindrops(-2) == '-2'
    assert raindrops(3) == '3'
    assert raindrops(4) == '4'
    assert raindrops(5) == '5'
    assert raindrops(6) == '6'
    assert raindrops(7) == '7'
    assert raindrops(8) == '8'
    assert raindrops(9) == '9'
    assert raindrops(10) == 'Pling'
    assert raindrops(11) == 'Buzz'
    assert raindrops(12) == 'PlingBuzz'
    assert raindrops(13) == 'PlingBuzz'
    assert raindrops(14) == 'PlingBuzz'
    assert raindrops(15) == 'PlingBuzz'
    assert raindrops(16) == 'PlingBuzz'
    assert raindrops(17) == 'PlingBuzz'
    assert raindrops(18) == 'PlingBuzz'
    assert raindrops(19) == 'PlingBuzz'
    assert raindrops(20) == 'PlingBuzz'
    assert raindrops(21) == 'PlingBuzz'
    assert raindrops(22) == 'PlingBuzz'
    assert raindrops(23) == 'PlingBuzz'
    assert raindrops(24) == 'PlingBuzz'
    assert raindrops(25) == 'PlingBuzz'
    assert raindrops(26) == 'PlingBuzz'
    assert raindrops(27) == 'PlingBuzz'
    assert raindrops(28) == 'PlingBuzz'
    assert raindrops(29) == 'PlingBuzz'
    assert raindrops(30) == 'PlingBuzz'
    assert raindrops(31) == 'PlingBuzz'
    assert raindrops(32) == 'PlingBuzz'
    assert raindrops(33) == 'PlingBuzz'
    assert raindrops(34) == 'PlingBuzz'
    assert raindrops(35) == 'PlingBuzz'
    assert raindrops(36) == 'PlingBuzz'
    assert raindrops(37) == 'PlingBu