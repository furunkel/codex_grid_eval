
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest eleventh value.
    """
    
    return min(lst)[1]
</cell>
<cell>
tuple_extract(lst)
</cell>
<text>
Problem 3
Write a function that takes a list and a number as arguments and returns the list with the number removed.


</text>
<cell>
def remove_number(lst, number):
    """
    Given a list and a number, write a function that returns the list with the number removed.
    """
    
    return lst.remove(number)
</cell>
<cell>
remove_number(lst, 2)
</cell>
<text>
Problem 4
Write a function that takes a list and a number as arguments and returns the list with the number replaced by the number itself.


</text>
<cell>
def replace_number(lst, number):
    """
    Given a list and a number, write a function that returns the list with the number replaced by the number itself.
    """
    
    return lst.replace(number, number)
</cell>
<cell>
replace_number(lst, 2)
</cell>
<text>
Problem 5
Write a function that takes a list and a number as arguments and returns the list with the number replaced by the number itself and all elements after that removed.


</text>
<cell>
def replace_and_remove(lst, number):
    """
    Given a list and a number, write a function that returns the list with the number replaced by the number itself and all elements after that removed.
    """
    
    return lst.replace(number, number) + lst[11:]
</cell>
<cell>
replace_and_remove(lst, 2)
</cell>
<text>
Problem 6
Write a function that takes a list and a number as arguments and returns the list with the number replaced by the number itself and all elements after that removed and the number appended.


</text>
<cell>
def replace_and_remove_and_append(lst, number):
    """
    Given a list and a number, write a function that returns the list with the number replaced by the number itself and all elements after that removed and the number appended.
    """
    
    return lst.replace(number, number) + lst[11:] + number
</cell>
<cell>
replace_and_remove_and_append(lst, 2)
</cell>
<text>
Problem 7
Write a function that takes a list and a number as arguments and returns the list with the number replaced by the number itself and all elements after that removed and the number appended and all elements before that removed.


</text>
<cell>
def replace_and_remove_and_append_and_remove(lst, number):
    """
    Given a list and a number, write a function that returns the list with the number replaced by the number itself and all elements after that removed and the number appended and all elements before that removed.
    """
    
    return lst.replace(number, number) + lst[11