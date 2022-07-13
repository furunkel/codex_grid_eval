
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Pling'
    elif num % 11 == 0:
        return 'Plong'
    else:
        return str(num)

# Now let's try it out!
print(raindrops(22))
print(raindrops(39))
print(raindrops(2))
</cell>
<text>
The above code works, but it can be made more concise by using the modulo operator:


</text>
<cell>
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Pling' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 11, so the result would be "FizzPling".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Pling'
    elif num % 11 == 0:
        return 'Plong'
    else:
        return str(num)

# Now let's try it out!
print(raindrops(22))
print(raindrops(39))
print(raindrops(2))
</cell>
<text>
The modulo operator is often used in Python to check if a number is divisible by another number. For example, if we want to check if a number is divisible by 3, we can use the modulo operator as follows:


</text>
<cell>
# Let's check if a number is divisible by 3
print(3 % 2 == 0)
</cell>
<text>
The modulo operator returns the remainder of the division of the first number by the second number. In this case, the remainder of 3 / 2 is 1, and the remainder of 3 % 2 is 0.

The remainder operator is also used to check if a number is evenly divisible by another number. For example, if we want to check if a number is evenly divisible by 3, we can use the remainder operator as follows:


</text>
<cell>
# Let's check if a 