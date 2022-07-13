
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Plang".
    33 has both 11 and 3 as factors, but not 5, so the result would be "PlingBuzz".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num < 1:
        return ""
    factors = []
    for n in range(1, num + 1):
        if num % n == 0:
            factors.append(n)
    if len(factors) == 0:
        return str(num)
    elif len(factors) == 1:
        return str(factors[0])
    elif len(factors) == 2:
        if factors[0] == factors[1]:
            return str(factors[0])
        else:
            return str(factors[0]) + "Buzz"
    elif len(factors) == 3:
        if factors[0] == factors[1] and factors[1] == factors[2]:
            return str(factors[0])
        else:
            return str(factors[0]) + "Plang"
    else:
        return str(num) + "".join(str(n) for n in factors)


# Problem 8
def fizzbuzz(num):
    """
    Your task is to convert a number into a string that contains the numbers 1 to num.
    However, for multiples of three (fizz), you append 'Fizz' to the result, and for multiples of five (buzz), you append 'Buzz' to the result.
    You do not need to test for divisibility by 3 or 5, as you cannot produce both 'FizzBuzz' and 'Fizz'.
    You do not need to test for divisibility by 11, as you cannot produce both 'Fizz11' and 'Fizz'.
    You do not need to test for divisibility by 5, as you cannot produce both 'Buzz5' and 'Buzz'.
    You do not need to test for divisibility by 1, as you cannot produce both '1' and 'Buzz1'.
    You do not need to test for divisibility by 13, as you cannot produce both '13' and 'Fizz13'.
    You do not need to test for divisibility by 17, as you cannot produce both '17' and 'Fizz17'.
    You do not need to test for divisibility by 19, as you cannot produce both '19' and 'Fizz19'.
    You do not need to test for divisibility by 23, as you cannot produce both '23' and 'Fizz23'.
    You do not need to test for divisibility by 29, as you cannot produce both '29' and 'Fizz29'.
    You do not need to test for divisibility by 31, as you cannot produce both '31' and 'Fizz31'.
    You do not need to test for divisibility by 37, as you cannot produce both '37' and 'Fizz37'.
    You do not need to test for divisibility by 41, as you cannot produce both '41' and 'Fizz41'.
    You do not need to test for divisibility by 43, as you cannot produce both '43' and 'Fizz43'.
    You do not need to test for divisibility by 47, as you 