
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return 'Fizz'
    elif num % 11 == 0:
        return 'Pling'
    elif num % 7 == 0:
        return 'Plong'
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(143))
print(raindrops(2))
</cell>
<text>
Problem 3
Write a function that takes an integer and returns the sum of the squares of the digits of that integer.


</text>
<cell>
def sum_of_squares(num):
    """
    Your task is to write a function that takes an integer and returns the sum of the squares of the digits of that integer.
    
    For example, if the input is 123, the function should return 1 + 4 + 9 + 3 = 22.
    """
    sum = 0
    
    while num > 0:
        sum += num % 10 ** 2
        num = num // 10
    return sum

# Test Cases
print(sum_of_squares(123))
print(sum_of_squares(1234))
print(sum_of_squares(12345))
print(sum_of_squares(123456))
print(sum_of_squares(1234567))
print(sum_of_squares(12345678))
print(sum_of_squares(123456789))
</cell>
<text>
Problem 4
Write a function that takes an integer and returns the sum of the cubes of the digits of that integer.


</text>
<cell>
def sum_of_cubes(num):
    """
    Your task is to write a function that takes an integer and returns the sum of the cubes of the digits of that integer.
    
    For example, if the input is 123, the function should return 1 + 8 + 27 + 12 + 3 + 1 = 40.
    """
    sum = 0
    
    while num > 0:
        sum += num % 10 ** 3
        num = num // 10
    return sum

# Test Cases
print(sum_of_cubes(123))
print(sum_of_cubes(1234))
print(sum_of_cubes(12345))
print(sum_of_cubes(123456))
print(sum_of_cubes(1234567))
print(sum_of_cubes(12345678))
print(sum_of_cubes(123456789))
</cell>
<text>
Problem 5
Write a function that takes an integer and returns the sum of the cubes of the digits of that integer multiplied by three.


</text>
<cell>
def sum_of_cubes_multiplied_by_three(num):
    """
    Your task is to write a function that takes an integer and returns the sum of the cubes of the digits of that integer multiplied by three.
    
    For example, if the input is 123, the function should return 1 + 8 + 27 + 