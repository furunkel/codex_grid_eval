
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(lst)[1]


# Test your function
print(some_func([(3, 'a'), (5, 'b'), (7, 'c'), (9, 'd')]))
</cell>
<text>
The second function takes in a list of tuples and returns the second value of the tuple with the smallest third value.


</text>
<cell>
# Test your function
print(second_smallest_value([(3, 'a'), (5, 'b'), (7, 'c'), (9, 'd')]))
</cell>
<text>
Write a function that returns a list of all the values in the given list except the one that matches the value you are searching for.


</text>
<cell>
# UNQ_C8 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# You do not have to input any code in this cell, but it is relevant to grading, so please do not change anything

def values_matching_second_largest(largest_list, target_value):
    """
    Given a list of tuples, and a target value, return a list containing all values in the given list except the one that matches the target value.

    >>> values_matching_second_largest([(3, 'a'), (5, 'b'), (7, 'c'), (9, 'd')], 'd')
    [(3, 'a'), (5, 'b')]
    """
    
    return list(filter(lambda value: value[0] != target_value, largest_list))
    
    
# Test your function
print(values_matching_second_largest([(3, 'a'), (5, 'b'), (7, 'c'), (9, 'd')], 'd'))
</cell>
<text>
Use lambda and filter to solve the following problems:


</text>
<text>
Problem 1
Create a function that returns a list of numbers, such that duplicates are not removed.

For example, given [1,2,2,3,3,4,4,5,5,5,6,6,6], it should return [1,2,3,4,5,6].

Note: Each number in the result should only be used once.

</text>
<cell>
# UNQ_C9 (UNIQUE CELL IDENTIFIER, DO NOT EDIT)
# You do not have to input any code in this cell, but it is relevant to grading, so please do not change anything

def list_of_numbers_without_duplicates(input_list):
    """
    Given a list of numbers, return a list where each number only occurs once.

    Example: list_of_numbers_without_duplicates([1,2,2,3,3,4,4,5,5,5,6,6,6]) should return the list [1,2,3,4,5,6]
    
    When there are two equal numbers in the list, you only need to keep one of them.
    """
    
    # initialize an empty list to store the unique numbers
    unique_list = []
    
    # loop through each value in the list
    for value in input_list:
        
        # 