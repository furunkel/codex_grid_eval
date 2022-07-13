
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest third value.
    """
    
    smallest_third = min(lst)
    
    return smallest_third[2]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Write a function that takes a list and returns a list of only the elements that are greater than the mean of the list.


</text>
<cell>
def list_greater_than_mean(lst):
    """
    Given a list of numbers, return a list that contains only the elements that are greater than the mean of the list.
    """
    
    lst = [1,2,3,4,5,6,7,8,9,10]
    
    mean = sum(lst) / len(lst)
    
    return [x for x in lst if x > mean]
</cell>
<cell>
list_greater_than_mean(lst)
</cell>
<text>
Write a function that takes a list and returns a list of only the elements that are less than the mean of the list.


</text>
<cell>
def list_less_than_mean(lst):
    """
    Given a list of numbers, return a list that contains only the elements that are less than the mean of the list.
    """
    
    lst = [1,2,3,4,5,6,7,8,9,10]
    
    mean = sum(lst) / len(lst)
    
    return [x for x in lst if x < mean]
</cell>
<cell>
list_less_than_mean(lst)
</cell>
<text>
Write a function that takes a list and returns a list of only the elements that are less than or equal to the mean of the list.


</text>
<cell>
def list_less_than_or_equal_mean(lst):
    """
    Given a list of numbers, return a list that contains only the elements that are less than or equal to the mean of the list.
    """
    
    lst = [1,2,3,4,5,6,7,8,9,10]
    
    mean = sum(lst) / len(lst)
    
    return [x for x in lst if x <= mean]
</cell>
<cell>
list_less_than_or_equal_mean(lst)
</cell>
<text>
Write a function that takes a list and returns a list of only the elements that are greater than or equal to the mean of the list.


</text>
<cell>
def list_greater_than_or_equal_mean(lst):
    """
    Given a list of numbers, return a list that contains only the elements that are greater than or equal to the mean of the list.
    """
    
    lst = [1,2,3,4,5,6,7,8,9,10]
    
    mean = sum(lst) / len(lst)
    
    return [x for x in lst if x >= mean]
</cell>
<cell>
list_greater_than_or_equal_mean(lst)
</cell>
<text>
Write a function that takes a list and returns a list of only the elements that are equal to the mean of the list.


</text>
<cell>
