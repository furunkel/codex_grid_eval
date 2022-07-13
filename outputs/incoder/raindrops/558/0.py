
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 11, so the result would be "FizzPlang".
    2 is not factored by 13, 5, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Plang"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(22))
print(raindrops(65))
print(raindrops(2))
</cell>
<text>
Problem 3
Write a function that takes a positive integer and returns the sum of the squares of the digits of that number.


</text>
<cell>
def sum_of_squares(num):
    """
    Your task is to write a function that, given a positive integer, returns the sum of the squares of the digits of that number.
    
    For example, if the input number is 123, the output should be 190.
    """
    sum = 0
    
    while num > 0:
        sum += num % 10 ** 2
        num //= 10
    
    return sum

# Test Cases
print(sum_of_squares(123))
print(sum_of_squares(1232))
print(sum_of_squares(12321))
</cell>
<text>
Problem 4
Write a function that takes a positive integer and returns the sum of the cubes of the digits of that number.


</text>
<cell>
def sum_of_cubes(num):
    """
    Your task is to write a function that, given a positive integer, returns the sum of the cubes of the digits of that number.
    
    For example, if the input number is 123, the output should be 627.
    """
    sum = 0
    
    while num > 0:
        sum += num % 10 ** 3
        num //= 10
    
    return sum

# Test Cases
print(sum_of_cubes(123))
print(sum_of_cubes(1232))
print(sum_of_cubes(12321))
</cell>
<text>
Problem 5
Write a function that takes a positive integer and returns the sum of the cubes of the digits of that number.
The sum of the cubes of the digits should never exceed 20 million.


</text>
<cell>
def sum_of_cubes_limit(num):
    """
    Your task is to write a function that, given a positive integer, returns the sum of the cubes of the digits of that number.
    
    For example, if the input number is 123, the output should be 627.
    """
    sum = 0
    
    while num > 0:
        sum += num % 10 ** 3
        num //= 10
    
    return sum

# Test Cases
print(sum_of_cubes_limit(123))
print(sum_of_cubes_limit(1232))
print(sum_of_cubes_limit(12321))
print(sum_of_cubes_limit(12