
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst[2], key=lambda x: x[-1])
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The max function can also take an optional key argument, which is a function that takes an element of the list and returns some kind of value to be used for comparisons. For example:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: x[-1])
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The key argument can be any function that takes an element of the list and returns some kind of value to be used for comparisons. For example:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: len(x))
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The key argument can also be a string, in which case it refers to a key in the dictionary returned by the built-in function dict. For example:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=len) # key refers to the key in the dictionary returned by len
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The key argument can also be a tuple of two elements, which will be used for sorting purposes. For example:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: (x[1], x[0]))
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The key argument can also be a tuple of three elements, which will be used for sorting purposes. For example:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst, key=lambda x: (x[1], x[0], x[2]))
</cell>
<cell>
f([(1,2,3), (4,5,6), (7,8,9)])
</cell>
<text>
The key argument can also be a tuple of four elements, which will be used for sorting purposes. For example:


</text>
<cell>
def f(lst):