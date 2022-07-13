
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 3 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 3 or 5, so the result would be "Plong".
    15 has both 3 and 5 as factors, but not 7, so the result would be "PlingPlang".
    2 is not factored by 3, 5, or 7, so the result would be "2".
    """
    if num % 3 == 0:
        return "Pling"
    elif num % 5 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(15))
print(raindrops(2))
</cell>
<text>
The above code should produce the following output:

Pling
PlingPlang
Plang
2

</text>
<text>
Question 3
Write a function that takes a positive integer and returns the sum of the squares of the digits of that integer.

Examples:
123 should return $1 + 4 + 9 + 3 = 22$
1234 should return $1 + 4 + 9 + 3 + 4 + 9 + 3 + 4 = 42$
1001 should return $1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10$

</text>
<cell>
def sum_of_squares(num):
    """
    Your task is to write a function that takes a positive integer and returns the sum of the squares of the digits of that integer.
    """
    total = 0
    
    # Your code here
    
    return total

# Test Cases
print(sum_of_squares(123))
print(sum_of_squares(1234))
print(sum_of_squares(1001))
</cell>
<text>
The above code should produce the following output:

22
42
10

</text>
<text>
Question 4
Write a function that takes a positive integer and returns the sum of the squares of the digits of that integer.

Examples:
123 should return $1 + 4 + 9 + 3 = 22$
1234 should return $1 + 4 + 9 + 3 + 4 + 9 + 3 + 4 = 42$
1001 should return $1 + 1 + 1 + 1 + 1 + 1 + 1 + 1 = 10$

</text>
<cell>
def sum_of_squares(num):
    """
    Your task is to write a function that takes a positive integer and returns the sum of the squares of the digits of that integer.
    """
    total = 0
    
    # Your code here
    
    return total

# Test Cases
print(sum_of_squares(123))
print(sum_of_squares(1234))
print(sum_of_squares(1001))
</cell>
<text>
The above code should produce the following output:

22
42
10

</text>
<text>
Question 5
Write a function that takes a positive integer and returns the sum of the squares of the digits of that integer.

Examples:
123 should return $1 + 4 + 9 + 3 = 22$
1234 should return $1 + 4 + 9 + 3 + 4 + 9 + 3 + 4 = 42$
1001 should return $