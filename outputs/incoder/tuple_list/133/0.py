
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    smallest_last_value = None
    
    for tup in lst:
        
        if smallest_last_value is None or tup[-1] < smallest_last_value:
            smallest_last_value = tup[-1]
            
    return smallest_last_value
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(tuple_extract(lst))
</cell>
<text>
Write a function that returns a list of all the tuples with the smallest second value.


</text>
<cell>
# Solution
def tuple_extract_2(lst):
    """
    Given a list of tuples, return a list containing the tuples with the smallest second value.
    """
    
    smallest_second_value = None
    
    for tup in lst:
        
        if smallest_second_value is None or tup[1] < smallest_second_value:
            smallest_second_value = tup[1]
            
    return smallest_second_value
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(tuple_extract_2(lst))
</cell>
<text>
Write a function that returns a list of all the tuples with the smallest third value.


</text>
<cell>
# Solution
def tuple_extract_3(lst):
    """
    Given a list of tuples, return a list containing the tuples with the smallest third value.
    """
    
    smallest_third_value = None
    
    for tup in lst:
        
        if smallest_third_value is None or tup[2] < smallest_third_value:
            smallest_third_value = tup[2]
            
    return smallest_third_value
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
print(tuple_extract_3(lst))
</cell>
<text>
Write a function that returns a list of all the tuples with the smallest second and third value.


</text>
<cell>
# Solution
def tuple_extract_4(lst):
    """
    Given a list of tuples, return a list containing the tuples with the smallest second and third value.
    """
    
    smallest_second_and_third_value = None
    
    for tup in lst:
        
        if smallest_second_and_third_value is None or tup[1] < smallest_second_and_third_value:
            smallest_second_and_third_value = tup[1]
            
        if smallest_second_and_third_value is None or tup[2] < smallest_second_and_third_value:
            smallest_second_and_third_value = tup[2]
            
    return smallest_second_and_third_value
</cell>
<cell>
# Test your code