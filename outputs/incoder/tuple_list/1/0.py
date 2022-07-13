
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    
    smallest_value = lst[0][0]
    
    for value in lst:
        if value[0] < smallest_value:
            smallest_value = value[0]
    
    return smallest_value

# Test Cases
print(tuple_extract(lst))
print(tuple_extract(lst2))
print(tuple_extract(lst3))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the numbers in the list. For example, given the list [4, 9, 16, 25] the function should return [64, 125, 128, 250].


</text>
<cell>
# Solution

def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers.
    """
    
    sum_squares = []
    
    for value in lst:
        sum_squares.append(value**2)
    
    return sum_squares

# Test Cases
print(square_sum([4, 9, 16, 25]))
print(square_sum([1, 2, 3, 4, 5]))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the numbers in the list. For example, given the list [4, 9, 16, 25] the function should return [64, 125, 128, 250].


</text>
<cell>
# Solution

def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers.
    """
    
    sum_squares = []
    
    for value in lst:
        sum_squares.append(value**2)
    
    return sum_squares

# Test Cases
print(square_sum([4, 9, 16, 25]))
print(square_sum([1, 2, 3, 4, 5]))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the numbers in the list. For example, given the list [4, 9, 16, 25] the function should return [64, 125, 128, 250].


</text>
<cell>
# Solution

def square_sum(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the numbers.
    """
    
    sum_squares = []
    
    for value in lst:
        sum_squares.append(value**2)
    
    return sum_squares

# Test Cases
print(square_sum([4, 9, 16, 25]))
print(square_sum([1, 2, 3, 4, 5]))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the numbers in the 