
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return lst[2]

# Test
print(fibonacci([(5,2), (1,3), (5,6)]))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a new list with all the even elements of the first list.

For example, fibonacci([1,2,3]) should return [2,4,6].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return [x for x in lst if x[0]%2==0]

# Test
print(fibonacci([(5,2), (1,3), (5,6)]))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a new list with all the odd elements of the first list.

For example, fibonacci([1,2,3]) should return [1,3,5].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return [x for x in lst if x[0]%2!=0]

# Test
print(fibonacci([(5,2), (1,3), (5,6)]))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a new list with all the even elements of the second list.

For example, fibonacci([1,2,3]) should return [2,4,6].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return [x for x in lst if x[1]%2==0]

# Test
print(fibonacci([(5,2), (1,3), (5,6)]))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a new list with all the odd elements of the second list.

For example, fibonacci([1,2,3]) should return [1,3,5].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return [x for x in lst if x[1]%2!=0]

# Test
print(fibonacci([(5,2), (1,3), (5,6)]))
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns a new list with all the even elements of the 