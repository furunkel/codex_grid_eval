
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(lst)[-1]

# Test your function
print(some_func([(7, 2, 9), (6, 3, 8), (5, 1, 7)]))
</cell>
<text>
The above function should return 7.


</text>
<text>
Problem 2b
Write a function that returns a list of all the even numbers from an input list. For example, if the input list is [1,2,3,4,5,6,7,8,9], your function should return [2,4,6,8].

HINT: You can use the filter function with a lambda expression. For example:

new_list = list(filter(lambda x: (x % 2) == 0, old_list))


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of numbers, return a list containing only the even numbers.
    """
    return list(filter(lambda x: (x % 2) == 0, lst))

# Test your function
print(even_numbers([1,2,3,4,5,6,7,8,9]))
</cell>
<text>
Problem 2c
Using lambda, write a function that returns a list of all the positive numbers from an input list. Your function should return a list containing all the positive numbers from the following list:

[10, -5, -20, 0, 5, 10, 15, 3, 2]


</text>
<cell>
def positive_numbers(lst):
    """
    Given a list of numbers, return a list containing only the positive numbers.
    """
    return list(filter(lambda x: (x > 0), lst))

# Test your function
print(positive_numbers([10, -5, -20, 0, 5, 10, 15, 3, 2]))
</cell>
<text>
Problem 2d
Using lambda, write a function that returns a list of all the negative numbers from an input list. Your function should return a list containing all the negative numbers from the following list:

[-10, -5, -20, 0, 5, 10, 15, 3, 2]


</text>
<cell>
def negative_numbers(lst):
    """
    Given a list of numbers, return a list containing only the negative numbers.
    """
    return list(filter(lambda x: (x < 0), lst))

# Test your function
print(negative_numbers([-10, -5, -20, 0, 5, 10, 15, 3, 2]))
</cell>
<text>
Problem 2e
Using lambda, write a function that returns a list of all the even numbers from an input list. Your function should return a list containing all the even numbers from the following list:

[10, -5, -20, 0, 5, 10, 15, 3, 2]


</text>
<cell>
def even_numbers(lst):
    """
    Given a list of numbers, return a list containing only the even numbers.
    """
    return list(filter(lambda x: (x % 2) == 0, lst))

# Test your function
print(even_numbers([10, -5, -20, 0, 5, 10, 15, 3, 2]))
</cell>
<text>