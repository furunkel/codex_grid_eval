
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 11 as a factor, add 'Buzz' to the result.
    has 5 as a factor, add 'Plong' to the result.
    does not have any of 13, 11, or 5 as a factor, the result should be the digits of the number as a string.

    Examples:
    10 has 5 as a factor, but not 13 or 11, so the result would be "Plong".
    143 has both 13 and 11 as factors, but not 5, so the result would be "FizzBuzz".
    2 is not factored by 13, 11, or 5, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 11 == 0:
        return "Buzz"
    elif num % 5 == 0:
        return "Plong"
    else:
        return str(num)

# Write your tests here
def test_raindrops():
    assert raindrops(10) == "Plong"
    assert raindrops(143) == "FizzBuzz"
    assert raindrops(2) == "2"

# Run tests
test_raindrops()
</cell>
<text>
Exercise 3
Write a function that takes a string and returns the number of words in the string. Words are separated by spaces.

Examples:
"Hello World" returns 5.
"Hello World!" returns 3.
"   " returns 0.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   " returns 5.
"   Hello   World!   