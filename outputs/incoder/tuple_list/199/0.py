
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest eleventh value.
    """
    
    return max(lst, key=lambda x: x[-1])
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value removed from the list.


</text>
<cell>
def remove_element(lst, element):
    """
    Given a list and a value, remove that value from the list.
    """
    
    return [x for x in lst if x != element]
</cell>
<cell>
remove_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value added to the list.


</text>
<cell>
def add_element(lst, element):
    """
    Given a list and a value, add that value to the list.
    """
    
    return [element + x for x in lst]
</cell>
<cell>
add_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value multiplied by the list.


</text>
<cell>
def multiply_element(lst, element):
    """
    Given a list and a value, multiply that value by the list.
    """
    
    return [element * x for x in lst]
</cell>
<cell>
multiply_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value divided by the list.


</text>
<cell>
def divide_element(lst, element):
    """
    Given a list and a value, divide that value by the list.
    """
    
    return [x / element for x in lst]
</cell>
<cell>
divide_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value raised to the list.


</text>
<cell>
def exponentiate_element(lst, element):
    """
    Given a list and a value, raise that value to the list.
    """
    
    return [element**x for x in lst]
</cell>
<cell>
exponentiate_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value divided by the list.


</text>
<cell>
def divide_element(lst, element):
    """
    Given a list and a value, divide that value by the list.
    """
    
    return [x / element for x in lst]
</cell>
<cell>
divide_element(lst, 'a')
</cell>
<text>
Write a function that takes a list and a value, and returns a list with the value multiplied by the list.


</text>
<cell>
def multiply_element(l