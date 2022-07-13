
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[2][1]
</cell>
<cell>
extract_value(lst)
</cell>
<text>
Problem 7
Write a function that takes a list as an argument and returns a list with the first element of the tuple removed and all of the other elements remained.


</text>
<cell>
def remove_element(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[2:]
</cell>
<cell>
lst = [('Bob', 40), ('Alice', 30), ('Sue', 20), ('Mary', 10)]
</cell>
<cell>
remove_element(lst)
</cell>
<text>
Problem 8
Write a function that takes a list as an argument and returns a list with the second element of the tuple removed and all of the other elements remained.


</text>
<cell>
def remove_element(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[1:]
</cell>
<cell>
lst = [('Bob', 40), ('Alice', 30), ('Sue', 20), ('Mary', 10)]
</cell>
<cell>
remove_element(lst)
</cell>
<text>
Problem 9
Write a function that takes a list as an argument and returns a list with the third element of the tuple removed and all of the other elements remained.


</text>
<cell>
def remove_element(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[2:]
</cell>
<cell>
lst = [('Bob', 40), ('Alice', 30), ('Sue', 20), ('Mary', 10)]
</cell>
<cell>
remove_element(lst)
</cell>
<text>
Problem 10
Write a function that takes a list as an argument and returns a list with the fourth element of the tuple removed and all of the other elements remained.


</text>
<cell>
def remove_element(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[3:]
</cell>
<cell>
lst = [('Bob', 40), ('Alice', 30), ('Sue', 20), ('Mary