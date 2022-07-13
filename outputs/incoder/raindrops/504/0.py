
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Fizz' to the result.
    has 5 as a factor, add 'Plang' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 7, so the result would be "FizzPlang".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    if num % 13 == 0:
        return "Fizz"
    elif num % 5 == 0:
        return "Plang"
    elif num % 7 == 0:
        return "Plong"
    else:
        return str(num)

# Test Cases
print(raindrops(14))
print(raindrops(65))
print(raindrops(2))
</cell>
<text>
Exercise 4
Write a function that takes a string and returns the number of vowels contained in the string.

Examples:
"hello" has 5 vowels.
"hello" has 0 vowels.
"hello" has 1 vowel.
"hello" has 2 vowels.
"hello" has 3 vowels.
"hello" has 4 vowels.
"hello" has 5 vowels.
"hello" has 6 vowels.
"hello" has 7 vowels.
"hello" has 8 vowels.
"hello" has 9 vowels.
"hello" has 10 vowels.
"hello" has 11 vowels.
"hello" has 12 vowels.
"hello" has 13 vowels.
"hello" has 14 vowels.
"hello" has 15 vowels.
"hello" has 16 vowels.
"hello" has 17 vowels.
"hello" has 18 vowels.
"hello" has 19 vowels.
"hello" has 20 vowels.
"hello" has 21 vowels.
"hello" has 22 vowels.
"hello" has 23 vowels.
"hello" has 24 vowels.
"hello" has 25 vowels.
"hello" has 26 vowels.
"hello" has 27 vowels.
"hello" has 28 vowels.
"hello" has 29 vowels.
"hello" has 30 vowels.
"hello" has 31 vowels.
"hello" has 32 vowels.
"hello" has 33 vowels.
"hello" has 34 vowels.
"hello" has 35 vowels.
"hello" has 36 vowels.
"hello" has 37 vowels.
"hello" has 38 vowels.
"hello" has 39 vowels.
"hello" has 40 vowels.
"hello" has 41 vowels.
"hello" has 42 vowels.
"hello" has 43 vowels.
"hello" has 44 vowels.
"hello" has 45 vowels.
"hello" has 46 vowels.
"hello" has 47 vowels.
"hello" has 48 vowels.
"hello" has 49 vowels.
"hello" has 