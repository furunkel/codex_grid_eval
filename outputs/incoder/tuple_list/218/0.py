
def f(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]))
</cell>
<text>
The second function takes in a list of tuples and returns the second value of the tuple with the smallest first value.


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]))
</cell>
<text>
The third function takes in a list of tuples and returns the third value of the tuple with the smallest first value.


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]))
</cell>
<text>
The fourth function takes in a list of tuples and returns the fourth value of the tuple with the smallest first value.


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the fourth value of the tuple with the smallest first value.
    """
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]))
</cell>
<text>
Challenge Exercise
Write a function that returns a list of numbers, such that duplicates are removed from the list. For example, if the list is [3, 3, 3, 3, 4, 4, 4, 4], then your function should return [3, 4, 4, 4].

Hint: You can use the function set() to remove duplicates from lists.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns a list of numbers, such that duplicates are removed from the list.
    """
    return list(set(lst))

# Test your function
print(f([3, 3, 3, 3, 4, 4, 4, 4]))
</cell>
<text>
Great Job!

</text>
<text>
Exercise - Write a function that returns a list of numbers, such that duplicates are removed from the list, in order.

</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns a list of numbers, such that duplicates are removed from the list, in order.
    """
    
    lst = list(set(lst))
    
    return lst

# Test your function
print(f([3, 3, 3, 3, 4, 4, 4, 4]))
</cell>
<text>
Great Job!

</text>
<text>
Exercise - Write a function that 