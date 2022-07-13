
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plang".
    65 has both 13 and 5 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    factors = []
    factors.append(num)
    factors.append(num % 13)
    factors.append(num % 5)
    factors.append(num % 7)
    factors.sort()
    factors.reverse()
    factors = factors[:len(factors)-1]
    factors.reverse()
    factors = ''.join(str(factor) for factor in factors)
    return factors

# Test Cases
print(raindrops(14))
print(raindrops(65))
print(raindrops(2))
</cell>
<text>
Problem 4
Write a function that returns the number of prime factors of a given number.


</text>
<cell>
def prime_factors(num):
    """
    Your task is to write a function that, given a number, returns the number of prime factors.
    
    Your function should return an integer that represents the number of prime factors.
    
    Your function should return 0 if there are no prime factors.
    
    Your function should raise a ValueError if your input is not an integer.
    """
    factors = []
    factors.append(num)
    factors.append(num % 2)
    factors.append(num % 3)
    factors.append(num % 5)
    factors.append(num % 7)
    factors.append(num % 11)
    factors.append(num % 13)
    factors.append(num % 17)
    factors.append(num % 19)
    factors.append(num % 23)
    factors.append(num % 29)
    factors.append(num % 31)
    factors.append(num % 37)
    factors.append(num % 41)
    factors.append(num % 43)
    factors.append(num % 47)
    factors.append(num % 53)
    factors.append(num % 59)
    factors.append(num % 61)
    factors.append(num % 67)
    factors.append(num % 71)
    factors.append(num % 73)
    factors.append(num % 79)
    factors.append(num % 83)
    factors.append(num % 89)
    factors.append(num % 97)
    factors.append(num % 101)
    factors.append(num % 103)
    factors.append(num % 107)
    factors.append(num % 109)
    factors.append(num % 113)
    factors.append(num % 127)
    factors.sort()
    factors.reverse()
    factors = factors[:len(factors)-1]
    factors.reverse()
    factors = ''.join(str(factor) for factor in factors)
    return factors

# Test Cases
print(prime_factors(14))
print(prime_factors(65))
print(prime_factors(2))
</cell>
