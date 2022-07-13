
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest third value.
    """
    return max(lst, key=lambda t: t[2])[0]


# Test your function
print(some_func([(3, "a"), (2, "b"), (2, "c")]))
</cell>
<text>
The key argument to max is a function that specifies how to compare two elements of the list. Here we are using the lambda function we defined above to compare the third element of each tuple.


</text>
<text>
Write a function that returns the first element of the tuple with the largest second value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first element of the tuple with the largest second value.
    """
    return max(lst, key=lambda t: t[1])[0]


# Test your function
print(some_func([(3, "a"), (2, "b"), (2, "c")]))
</cell>
<text>
Now write a function that returns the first element of the tuple with the smallest second value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first element of the tuple with the smallest second value.
    """
    return min(lst, key=lambda t: t[1])[0]


# Test your function
print(some_func([(3, "a"), (2, "b"), (2, "c")]))
</cell>
<text>
Great job!

</text>
<text>
Exercise - Write a function that returns a list of numbers, such that duplicates are removed from the list. Assume that the list does not contain any duplicate entries.


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list where no adjacent duplicate entries exist.
    """
    
    # Remove duplicates
    lst = list(set(lst))
    
    # Return list
    return lst


# Test your function
print(remove_duplicates([3, 1, 2, 3, 2]))
</cell>
<text>
Great job!

</text>
<text>
Exercise - Write a function that returns a list of numbers, such that adjacent duplicate entries are removed. Assume that the list does not contain any duplicate entries.


</text>
<cell>
def remove_adjacent(lst):
    """
    Given a list of numbers, return a list where adjacent duplicate entries are removed.
    """
    
    # Remove adjacent duplicates
    lst = list(set(lst))
    
    # Return list
    return lst


# Test your function
print(remove_adjacent([3, 1, 2, 3, 2]))
</cell>
<text>
Great job!

</text>
<text>
Exercise - Write a function that returns a list of numbers, such that every number appears only once and no other number appears in the list.


</text>
<cell>
def remove_duplicates_2(lst):
    """
    Given a list of numbers, return a 