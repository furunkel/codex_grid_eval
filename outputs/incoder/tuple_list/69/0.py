
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest last value.
    """
    return max(lst)[1]


# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (9, 'd')]))
</cell>
<text>
Expected output
9

</text>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given the list l = [1, 1, 2, 3, 4, 4, 4, 4] your function should return [1, 2].

Hint: use a set object to remove duplicates.


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list where all duplicates have been removed.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
print(remove_duplicates([1, 1, 2, 3, 4, 4, 4, 4]))
</cell>
<text>
Expected output
[1, 2]

</text>
<text>
Write a function that checks whether a number is "happy" or not. A happy number is defined by the following process:

Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

For example, starting with 6, we have the following:

$$6^2 + 6^2 + 6^2 + 6^2 + 1$$

Now we replace the 1 in the process above with the sum of the squares of the digits of 6, and we get:

$$9 + 9 + 9 + 9 + 1 + 1$$

This process ends in 1 so the new number equals 1, and it is a happy number. Similarly, starting with 31, the process of replacing 1 ends in 1 so the new number equals 1, and it is a happy number.

Write a function that takes in a number and returns "happy", "not happy", or None if it is not a happy number.


</text>
<cell>
def check_squares(num):
    """
    Takes in a number and returns "happy", "not happy", or None if it is not a happy number.
    """
    
    # Your code here
    
    return None
</cell>
<cell>
print(check_squares(6))
print(check_squares(9))
print(check_squares(31))
print(check_squares(12))
</cell>
<text>
Expected output
happy
not happy
None
happy

</text>
<text>
Write a function that takes in a year and returns the number of days since the start of the year. For example, if the year is 2016, it would return the number of days between January 1, 2016 and January 1, 2017.

