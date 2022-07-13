
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest first value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][1]

# Test Cases
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21)]) == 13
assert fibonacci([(1, 2), (3, 5), (5, 8), (13, 21), (25, 4)]) == 25
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first elements of the list.


</text>
<cell>
def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the first elements of the list.
    """
    
    lst = sorted(lst)
    
    return [x ** 2 for x in lst]

# Test Cases
assert square_sum([1, 2, 3]) == [1, 4, 9]
assert square_sum([1, 4, 9]) == [1, 4, 9]
assert square_sum([-1, -2, -3]) == [-3, -3, -3]
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first elements of the list, plus the sum of the squares of the second elements of the list.


</text>
<cell>
def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the first elements of the list.
    """
    
    lst = sorted(lst)
    
    return [x ** 2 + y for x, y in zip(lst, lst[1:])]

# Test Cases
assert square_sum([1, 2, 3]) == [1, 4, 9]
assert square_sum([1, 4, 9]) == [1, 4, 9]
assert square_sum([-1, -2, -3]) == [-3, -3, -3]
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first elements of the list, plus the sum of the squares of the second elements of the list, plus the sum of the squares of the third elements of the list.


</text>
<cell>
def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the first elements of the list.
    """
    
    lst = sorted(lst)
    
    return [x ** 2 + y ** 2 + z ** 2 for x, y, z in zip(lst, lst[1:], lst[2:])]

# Test Cases
assert square_sum([1, 2, 3]) == [1, 4, 9, 16, 25]
assert square_sum([1, 4, 9]) == [1, 4, 9, 16, 25]
assert square_sum([-1, -2, -3]) == [-3, -3, -3, -3, -3]
</