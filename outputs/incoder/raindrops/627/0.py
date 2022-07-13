
def raindrops(num):
    """
    Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
    A factor is a number that evenly divides into another number, leaving no remainder.
    The simplest way to test if one number is a factor of another is to use the modulo operation.

    The rules of raindrops are that if a given number:

    has 13 as a factor, add 'Pling' to the result.
    has 3 as a factor, add 'Buzz' to the result.
    has 11 as a factor, add 'Plong' to the result.
    does not have any of 13, 3, or 11 as a factor, the result should be the digits of the number as a string.

    Examples:
    22 has 11 as a factor, but not 13 or 3, so the result would be "Plong".
    39 has both 13 and 3 as factors, but not 11, so the result would be "PlingBuzz".
    2 is not factored by 13, 3, or 11, so the result would be "2".
    """
    if num % 13 == 0:
        return "Pling"
    elif num % 3 == 0:
        return "Buzz"
    elif num % 11 == 0:
        return "Plong"
    else:
        return str(num)

# Write your tests here
assert raindrops(22) == "Plong"
assert raindrops(39) == "PlingBuzz"
assert raindrops(2) == "2"
</cell>
<text>
Exercise 2
Write a function that takes in a list of integers and returns the sum of the integers in the list. Your function should handle non-numeric types (like strings) gracefully.

Examples:
sum([1, 2, 3]) == 6
sum([1, 2, 'three']) == 6
sum([1, 'two', 3]) == 6
sum([1, 'two', 3, False]) == 6
sum([1, 'two', 3, None, False]) == 6
sum([1, 'two', 3, [], False]) == 6
sum([1, 'two', 3, {}, False]) == 6
sum([1, 'two', 3, set(), False]) == 6
sum([1, 'two', 3, frozenset(), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), False]) == 6
sum([1, 'two', 3, Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), Decimal('3.14'), 