
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    
    # Your code here
    
    if num % 13 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)

# Test cases
print(raindrops(10))
print(raindrops(143))
print(raindrops(2))
</cell>
<text>
Exercise 3
Write a function that takes an integer and returns the sum of the squares of the digits of that integer.

Examples:
For 123, the function should return 1 + 4 + 9 = 17.
For 9, the function should return 0 + 9 = 9.
For 38, the function should return 8 + 8 + 8 = 24.
For 0, the function should return 0.


</text>
<cell>
def sum_of_squares(num):
    """
    Your code here
    """
    
    # Your code here
    
    return sum((int(i) ** 2) for i in str(num))

# Test cases
print(sum_of_squares(123))
print(sum_of_squares(9))
print(sum_of_squares(38))
print(sum_of_squares(0))
</cell>
<text>
Exercise 4
Write a function that takes an integer and returns the sum of the squares of the digits of that integer modulo 10.

Examples:
For 123, the function should return 1 + 4 + 9 = 17.
For 9, the function should return 0 + 9 = 9.
For 38, the function should return 8 + 8 + 8 = 24.
For 0, the function should return 0.


</text>
<cell>
def sum_of_squares_modulo(num):
    """
    Your code here
    """
    
    # Your code here
    
    return sum((int(i) ** 2) % 10 for i in str(num))

# Test cases
print(sum_of_squares_modulo(123))
print(sum_of_squares_modulo(9))
print(sum_of_squares_modulo(38))
print(sum_of_squares_modulo(0))
</cell>
<text>
Exercise 5
Write a function that takes an integer and returns the sum of the squares of the digits of that integer modulo 100. Do not use the built-in modulo function for this exercise.

Examples:
For 123, the function should return 1 + 4 + 9 = 17.
For 9, the function should return 0 + 9 = 9.
For 38, the function should return 8 + 8 + 8 = 24.
For 0, the function should return 0.


</text>
<cell>
def sum_of_squares_modulo_100(num):
    """
    Your code here
    """
    
    # Your code here