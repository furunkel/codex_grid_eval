
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest second value.
    """
    return max(lst, key=lambda tup: tup[1])[1]

# Test the function
print(some_func([(7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)]))
</cell>
<text>
The lambda function can take in multiple arguments and return a value. In this case, the lambda function will return the second value of the tuple with the largest second value.


</text>
<text>
Exercise
Write a function that returns the second value of the tuple with the largest second value.


</text>
<cell>
# Solution

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lambda tup: tup[1])[1]

# Test the function
print(some_func([(7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)]))
</cell>
<text>
The max function can also take in multiple arguments and return multiple values. In this case, the max function will return the second value of the tuple with the largest second value.


</text>
<text>
Exercise
Write a function that returns the second value of the tuple with the largest second value.


</text>
<cell>
# Solution

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest second value.
    """
    return max(lst, key=lambda tup: tup[1])[1]

# Test the function
print(some_func([(7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)]))
</cell>
<text>
The min function
The min function returns the minimum value of the argument. min can take in multiple arguments and return multiple values.


</text>
<cell>
# Solution

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the tuple.
    """
    return min(lst)

# Test the function
print(some_func([(7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)]))
</cell>
<text>
The min function can also take in multiple arguments and return multiple values. In this case, the min function will return the minimum value of the tuple.


</text>
<text>
Exercise
Write a function that returns the minimum value of the tuple.


</text>
<cell>
# Solution

def some_func(lst):
    """
    Given a list of tuples, write a function that returns the minimum value of the tuple.
    """
    return min(lst)

# Test the function
print(some_func([(7, 1), (6, 2), (5, 3), (4, 4), (3, 5), (2, 6)]))
</cell>
<text>
The sum function
The sum function returns the sum of the argument. sum can take in multiple arguments and return multiple values.


</text>