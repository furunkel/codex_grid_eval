
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 3, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 3 or 11, so the result would be "Plong".
    33 has both 3 and 11 as factors, but not 5, so the result would be "PlangBuzz".
    2 is not factored by 3, 11, or 5, so the result would be "2".
    """
    if num < 1:
        return "Invalid input"
    if num == 1:
        return "1"
    if num == 2:
        return "2"
    if num % 3 == 0:
        return "Plang"
    if num % 11 == 0:
        return "Buzz"
    if num % 5 == 0:
        return "Plong"
    factors = []
    for i in range(1, num + 1):
        if num % i == 0:
            factors.append(i)
    if len(factors) == 0:
        return str(num)
    factors.sort()
    factors.reverse()
    factors = factors[:len(factors)-1]
    factors = factors + ["1"]
    factors = factors + ["2"]
    factors = factors + ["3"]
    factors = factors + ["4"]
    factors = factors + ["5"]
    factors = factors + ["6"]
    factors = factors + ["7"]
    factors = factors + ["8"]
    factors = factors + ["9"]
    factors = factors + ["10"]
    factors = factors + ["11"]
    factors = factors + ["12"]
    factors = factors + ["13"]
    factors = factors + ["14"]
    factors = factors + ["15"]
    factors = factors + ["16"]
    factors = factors + ["17"]
    factors = factors + ["18"]
    factors = factors + ["19"]
    factors = factors + ["20"]
    factors = factors + ["21"]
    factors = factors + ["22"]
    factors = factors + ["23"]
    factors = factors + ["24"]
    factors = factors + ["25"]
    factors = factors + ["26"]
    factors = factors + ["27"]
    factors = factors + ["28"]
    factors = factors + ["29"]
    factors = factors + ["30"]
    factors = factors + ["31"]
    factors = factors + ["32"]
    factors = factors + ["33"]
    factors = factors + ["34"]
    factors = factors + ["35"]
    factors = factors + ["36"]
    factors = factors + ["37"]
    factors = factors + ["38"]
    factors = factors + ["39"]
    factors = factors + ["40"]
    factors = factors + ["41"]
    factors = factors + ["42"]
    factors = factors + ["43"]
    factors = factors + ["44"]
    factors = factors + ["45"]
    factors = 