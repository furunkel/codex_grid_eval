
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Pling' to the result.
    has 7 as a factor, add 'Plang' to the result.
    does not have any of 13, 11, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 11, so the result would be "Plang".
    143 has both 13 and 11 as factors, but not 7, so the result would be "FizzPling".
    2 is not factored by 13, 11, or 7, so the result would be "2".
    """
    
    num = num % 10
    if num in (13, 11):
        return 'Fizz'
    elif num in (7, ):
        return 'Plang'
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(143))
print(raindrops(2))
</cell>
<text>
Question 3
Write a function that converts a number into its binary representation.

The function should take one parameter, num, and return the binary representation of num.

The function should return the string representation of the binary number in base 2.

The function should return an error if the input is not an integer.

Examples:
For num = 2, the function should return "10".
For num = 4, the function should return "11".
For num = 14, the function should return "11110".
For num = 25, the function should return "11111111".
For num = 0, the function should return "0".
For num = -1, the function should return "-1".
For num = -2, the function should return "-10".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = -25, the function should return "-11111111".
For num = -0, the function should return "-0".
For num = -4, the function should return "-11".
For num = 