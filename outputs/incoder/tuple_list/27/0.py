
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(lst)[1]


# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]))
</cell>
<text>
Problem 3
Using reduce to find the sum of the list after applying the function to the tuple with the smallest second value.

HINT: You can use the key argument of min to specify a function that extracts the value you wish to compare on.


</text>
<cell>
from functools import reduce

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the sum of the first value of the tuple with the smallest third value.
    """
    return reduce(lambda x, y: x + y, min(lst, key=lambda t: t[1]))


# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]))
</cell>
<text>
Problem 4
Using reduce to find the sum of the list after applying the function to the tuple with the smallest second value.

HINT: You can use the key argument of min to specify a function that extracts the value you wish to compare on.


</text>
<cell>
from functools import reduce

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the sum of the first value of the tuple with the smallest third value.
    """
    return reduce(lambda x, y: x + y, min(lst, key=lambda t: t[1]))


# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]))
</cell>
<text>
Problem 5
Using reduce to find the sum of the list after applying the function to the tuple with the smallest second value.

HINT: You can use the key argument of min to specify a function that extracts the value you wish to compare on.


</text>
<cell>
from functools import reduce

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the sum of the first value of the tuple with the smallest third value.
    """
    return reduce(lambda x, y: x + y, min(lst, key=lambda t: t[1]))


# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (0, 'd')]))
</cell>
<text>
Problem 6
Using reduce to find the sum of the list after applying the function to the tuple with the smallest second value.

HINT: You can use the key argument of min to specify a function that extracts the value you wish to compare on.


</text>
<cell>
from functools import reduce

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the sum of the first value of the tuple with the smallest third value.
    """
    return reduce(lambda x, y: x + y, min(lst, key=lambda t: t[1]))


# Test your function
print(some_func([(3, 'a'), (