
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    return max(lst)[2]

# Test your function
print(some_func([(7, 8, 9), (4, 5, 6), (10, 11, 12)]))
</cell>
<text>
The first line of the function definition uses the built-in function max() which returns the largest element in a list. max() also takes in optional arguments that allow you to specify which element you want to compare the list against. In the example above, we are comparing the list against the third element of the tuple. As you can see, this works because tuples are compared element-wise.

The second line of the function definition uses the built-in function enumerate() which returns a list of tuples, where each tuple is composed of (index, element) where index is the position in the list from which you want the element and element is the actual element in the list.

The third line of the function definition uses the built-in function max() again to return the third element of the tuple with the largest first value.

The fourth line of the function definition uses the built-in function list() which returns a list of all the elements in the list.

The fifth line of the function definition uses the built-in function tuple() which converts the list to a tuple.

The last line of the function definition uses the built-in function max() again to return the third element of the tuple with the largest first value.


</text>
<text>
Problem 3
Write a function that takes a list and returns a new list with all the odd indexed elements of the original list concatenated together.

For example, given [1,2,3,4,5,6,7], your function should return [1,3,5,7].

Hint: You can use the built-in function enumerate().


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the odd indexed elements of the tuple with the largest first value.
    """
    return lst[1::2]

# Test your function
print(some_func([(7, 8, 9), (4, 5, 6), (10, 11, 12)]))
</cell>
<text>
Problem 4
Write a function that takes a list and returns a new list with all the even indexed elements of the original list concatenated together.

For example, given [1,2,3,4,5,6,7], your function should return [2,4,6,8].

Hint: You can use the built-in function enumerate().


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the even indexed elements of the tuple with the largest first value.
    """
    return lst[0::2]

# Test your function
print(some_func([(7, 8, 9), (4, 5, 6), (10, 11, 12)]))
</cell>
<text>
Problem 5
Write a function that takes a list and returns a new list with all the even indexed elements of the original list concatenated together.

For example, given [1,2,3,4,5,6,7], your function should return 