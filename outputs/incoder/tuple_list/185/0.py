
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
    
    smallest_third = lst[0][2]
    second_smallest_third = lst[1][2]
    
    for tup in lst[2:]:
        if tup[2] < second_smallest_third:
            second_smallest_third = tup[2]
        elif tup[2] > smallest_third:
            smallest_third = tup[2]
    
    return smallest_third

print(min_max([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first two elements in the list. For example, given the list [1,2,3,4,5], the function should return [1,9,25,49,141].


</text>
<cell>
def sum_of_squares(lst):
    """
    Given a list of numbers, return the sum of squares.
    """
    
    sum_squares = []
    
    for num in lst:
        sum_squares.append(num**2)
    
    return sum_squares

print(sum_of_squares([1,2,3,4,5]))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first two elements in the list. For example, given the list [1,2,3,4,5], the function should return [1,9,25,49,141].


</text>
<cell>
def sum_of_squares(lst):
    """
    Given a list of numbers, return the sum of squares.
    """
    
    sum_squares = []
    
    for num in lst:
        sum_squares.append(num**2)
    
    return sum_squares

print(sum_of_squares([1,2,3,4,5]))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first two elements in the list. For example, given the list [1,2,3,4,5], the function should return [1,9,25,49,141].


</text>
<cell>
def sum_of_squares(lst):
    """
    Given a list of numbers, return the sum of squares.
    """
    
    sum_squares = []
    
    for num in lst:
        sum_squares.append(num**2)
    
    return sum_squares

print(sum_of_squares([1,2,3,4,5]))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first two elements in the list. For example, given the list [1,2,3,4,5], the function should return [1,9,25,49,141].


</text>
<cell>
def sum_