
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    return max(lst)[1]

print(f([(3,2), (5,1), (7,3)]))
</cell>
<text>
Exercise 2
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than zero.
    """
    return len([x for x in lst if x > 0])

print(count_greater_than([3, -4, 0, 5, 2]))
</cell>
<text>
Exercise 3
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_than(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than zero.
    """
    return len([x for x in lst if x < 0])

print(count_less_than([3, -4, 0, 5, 2]))
</cell>
<text>
Exercise 4
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_equal(lst):
    """
    Given a list of numbers, return the number of elements in the list that are equal to zero.
    """
    return len([x for x in lst if x == 0])

print(count_equal([3, -4, 0, 5, 2]))
</cell>
<text>
Exercise 5
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_than_or_equal(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than or equal to zero.
    """
    return len([x for x in lst if x >= 0])

print(count_greater_than_or_equal([3, -4, 0, 5, 2]))
</cell>
<text>
Exercise 6
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>
def count_less_than_or_equal(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than or equal to zero.
    """
    return len([x for x in lst if x <= 0])

print(count_less_than_or_equal([3, -4, 0, 5, 2]))
</cell>
<text>
Exercise 7
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_than_or_equal(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than zero.
    """
    return len([x for x in lst if x > 0])

print(count_great