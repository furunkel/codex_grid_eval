
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 3 as a factor, add 'Plang' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 5, so the result would be "FizzPlang".
    2 is not factored by 13, 3, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 3 == 0:
        return "Plang"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(10))
print(raindrops(39))
print(raindrops(2))
</cell>
<text>
Problem 4
Write a function that takes a string and returns the number of words in the string.

Examples:
"Hello World" returns 5.
"The rain in Spain" returns 8.
"abracadabra" returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The rain in Spain falls mainly on the plain." returns 0.
"The 