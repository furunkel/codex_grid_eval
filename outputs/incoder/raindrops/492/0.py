
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 5 as a factor, add 'Buzz' to the result.
    has 7 as a factor, add 'Plong' to the result.
    does not have any of 13, 5, or 7 as a factor, the result should be the digits of the number as a string.

    Examples:
    14 has 7 as a factor, but not 13 or 5, so the result would be "Plong".
    65 has both 13 and 5 as factors, but not 7, so the result would be "PlingBuzz".
    2 is not factored by 13, 5, or 7, so the result would be "2".
    """
    factors = [13, 5, 7]
    digits = str(num)
    
    if any(num % factor in factors for factor in factors):
        digits = digits + 'Pling'
    if any(num % factor in factors for factor in factors):
        digits = digits + 'Buzz'
    if any(num % factor in factors for factor in factors):
        digits = digits + 'Plong'
    
    return digits

# Test Cases
print(raindrops(14))
print(raindrops(65))
print(raindrops(2))
</cell>
<text>
Question 3
Write a function that takes a string and returns the number of words in the string.

Examples:

'Hello World' has 4 words, so it should return 4.
'The quick brown fox jumps over the lazy dog' has 9 words, so it should return 9.
'The quick brown fox jumps over the lazy dog.' has 0 words, so it should return 0.
'The quick brown fox jumps over the lazy dog.' has 1 word, so it should return 1.
'The quick brown fox jumps over the lazy dog.' has 2 words, so it should return 2.
'The quick brown fox jumps over the lazy dog.' has 3 words, so it should return 3.
'The quick brown fox jumps over the lazy dog.' has 4 words, so it should return 4.
'The quick brown fox jumps over the lazy dog.' has 5 words, so it should return 5.
'The quick brown fox jumps over the lazy dog.' has 6 words, so it should return 6.
'The quick brown fox jumps over the lazy dog.' has 7 words, so it should return 7.
'The quick brown fox jumps over the lazy dog.' has 8 words, so it should return 8.
'The quick brown fox jumps over the lazy dog.' has 9 words, so it should return 9.
'The quick brown fox jumps over the lazy dog.' has 10 words, so it should return 10.
'The quick brown fox jumps over the lazy dog.' has 11 words, so it should return 11.
'The quick brown fox jumps over the lazy dog.' has 12 words, so it should return 12.
'The quick brown fox jumps over the lazy dog.' has 13 words, so it should return 13.
'The quick brown fox jumps over the lazy dog.' has 14 words, so it should return 14.
'The quick brown fox jumps over the lazy dog.' has 