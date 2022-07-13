
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 11 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 11, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 11 or 3, so the result would be "Plong".
    33 has both 11 and 3 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 11, 3, or 5, so the result would be "2".
    """
    if num == 0:
        return '0'
    elif num == 1:
        return '1'
    elif num == 2:
        return '2'
    elif num == 3:
        return '3'
    elif num % 11 == 0:
        return 'Fizz'
    elif num % 3 == 0:
        return 'Plang'
    elif num % 5 == 0:
        return 'Plong'
    else:
        return str(num)

# Now let's test your code
print(raindrops(10))
print(raindrops(33))
print(raindrops(2))
print(raindrops(1))
print(raindrops(0))
</cell>
<text>
Exercise 3
Write a function that takes a positive integer and returns the sum of the squares of the digits of that number.

Examples:
123 should return 1 + 4 + 9 + 3 = 17 
(1 + 4 + 9) should return 1 + 9 = 10 
(1 + 9) should return 10
(1 + 9 + 3) should return 1 + 9 + 3 = 17 
(1 + 9 + 3 + 6) should return 1 + 9 + 3 + 6 = 20
(1 + 9 + 3 + 6 + 2) should return 1 + 9 + 3 + 6 + 2 = 25

</text>
<cell>
def sum_of_squares(num):
    """
    Your task is to write a function that takes a positive integer and returns the sum of the squares of the digits of that number.

    Examples:
    123 should return 1 + 4 + 9 + 3 = 17 
    (1 + 4 + 9) should return 1 + 9 = 10 
    (1 + 9) should return 10
    (1 + 9 + 3) should return 1 + 9 + 3 = 17 
    (1 + 9 + 3 + 6) should return 1 + 9 + 3 + 6 = 20
    (1 + 9 + 3 + 6 + 2) should return 1 + 9 + 3 + 6 + 2 = 25
    """
    
    squares = 0
    
    while num > 0:
        squares += num % 10**2
        num = num // 10
    
    return squares

# Now let's test your code
print(sum_of_squares(123))
print(sum_of_squares(1))
print(sum_of_squares(10))
print(sum_of_squares(9))
print(sum_of_squares(9 + 3))
print(sum_of_squares(9 + 3 + 6))
print(sum_of_squares(9 + 3 + 6 + 2))
</cell>
<text>
Exercise 4
Write a function that takes a positive integer and returns the sum of the cubes of the digits of that number.

Examples:
123 should return 1 + 8 + 27 + 3 = 66 
(1 + 8 + 27) should return 1 + 27 = 49 
(1 + 27) should return 49
(1 + 27 + 3) should return 1 + 27 + 3 = 