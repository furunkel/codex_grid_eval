
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    lst = sorted(lst)
    return lst[11][1]
</cell>
<cell>
fibonacci([(5,1),(6,2),(7,3)])
</cell>
<text>
Problem 7: Write a function that takes a list as an argument and returns a list with the elements of the list sorted from smallest to largest.
Example:

>>> my_list = [1,5,2,6,8,4,7,9,3]
>>> sorted(my_list)
[1, 2, 4, 5, 6, 7, 8, 9]

</text>
<cell>
def my_sorted(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    lst = sorted(lst)
    return lst
</cell>
<cell>
my_sorted([5,1,6,2,8,4,7,9,3])
</cell>
<text>
Problem 8: Write a function that takes a list as an argument and returns a list with the elements of the list sorted from largest to smallest.
Example:

>>> my_list = [1,5,2,6,8,4,7,9,3]
>>> sorted(my_list)
[9, 8, 7, 6, 5, 4, 3, 2, 1]

</text>
<cell>
def my_reversed_sorted(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    lst = sorted(lst, reverse=True)
    return lst
</cell>
<cell>
my_reversed_sorted([5,1,6,2,8,4,7,9,3])
</cell>
<text>
Problem 9: Write a function that takes a list as an argument and returns a list with the elements of the list sorted from smallest to largest.
Example:

>>> my_list = [1,5,2,6,8,4,7,9,3]
>>> sorted(my_list)
[1, 2, 4, 5, 6, 7, 8, 9]

</text>
<cell>
def my_reversed_sorted(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    lst = sorted(lst, reverse=True)
    return lst
</cell>
<cell>
my_reversed_sorted([5,1,6,2,8,4,7,9,3])
</cell>
<text>
Problem 10: Write a function that takes a list as an argument and returns a list with the elements of the list sorted from largest to smallest.
Example:

>>> my_list = [1,5,2,6,8,4,7,9,3]
>>> sorted(my_list)
[9, 8, 7, 6, 5, 4, 3, 2, 1]

</text>
<cell>
def my_reversed_sorted(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    lst = sorted(lst, reverse=True)
    return lst
</