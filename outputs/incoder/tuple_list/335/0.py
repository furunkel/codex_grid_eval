
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    
    return max(lst)
    
#test
print(min_max([(1,2,3), (4,5,6), (7,8,9)]))
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than zero.


</text>
<cell>
def count_greater_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than zero.
    """
    
    return len([x for x in lst if x > 0])
    
#test
print(count_greater_zero([1,2,3]))
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns the number of elements in the list that are less than zero.


</text>
<cell>
def count_less_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than zero.
    """
    
    return len([x for x in lst if x < 0])
    
#test
print(count_less_zero([1,2,3]))
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to zero.


</text>
<cell>
def count_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are equal to zero.
    """
    
    return len([x for x in lst if x == 0])
    
#test
print(count_zero([1,2,3]))
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to zero.


</text>
<cell>
def count_greater_equal_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are greater than or equal to zero.
    """
    
    return len([x for x in lst if x >= 0])
    
#test
print(count_greater_equal_zero([1,2,3]))
</cell>
<text>
Problem 11
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to zero.


</text>
<cell>
def count_less_equal_zero(lst):
    """
    Given a list of tuples, write a function that returns the number of elements in the list that are less than or equal to zero.
    """
    
    return len([x for x in lst if x <= 0])
    
#test
print(count_less_equal_zero([1,2,3]))
</cell>
<text>
Problem 12
Write a function that takes a list as an argument and returns the number of elements in the list that are equal to or less than zero.


</text>
<cell>
def count_equal_or_less_zero(lst):
    """
