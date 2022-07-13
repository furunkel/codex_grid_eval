
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest twelfth value.
    """
    
    smallest_twelfth = lst[0][2]
    
    for tup in lst:
        if tup[2] < smallest_twelfth:
            smallest_twelfth = tup[2]
            
    return smallest_twelfth
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Question 3
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than the average of the list.


</text>
<cell>
def count_greater_than_average(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than the average of the list.
    """
    
    average = sum(lst) / len(lst)
    
    return len([x for x in lst if x > average])
</cell>
<cell>
count_greater_than_average(lst)
</cell>
<text>
Question 4
Write a function that takes a list as an argument and returns the number of elements in the list that are less than the average of the list.


</text>
<cell>
def count_less_than_average(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than the average of the list.
    """
    
    average = sum(lst) / len(lst)
    
    return len([x for x in lst if x < average])
</cell>
<cell>
count_less_than_average(lst)
</cell>
<text>
Question 5
Write a function that takes a list as an argument and returns the number of elements in the list that are less than or equal to the average of the list.


</text>
<cell>
def count_less_than_or_equal_to_average(lst):
    """
    Given a list of numbers, return the number of elements in the list that are less than or equal to the average of the list.
    """
    
    average = sum(lst) / len(lst)
    
    return len([x for x in lst if x <= average])
</cell>
<cell>
count_less_than_or_equal_to_average(lst)
</cell>
<text>
Question 6
Write a function that takes a list as an argument and returns the number of elements in the list that are greater than or equal to the average of the list.


</text>
<cell>
def count_greater_than_or_equal_to_average(lst):
    """
    Given a list of numbers, return the number of elements in the list that are greater than or equal to the average of the list.
    """
    
    average = sum(lst) / len(lst)
    
    return len([x for x in lst if x >= average])
</cell>
<cell>
count_greater_than_or_equal_to_average