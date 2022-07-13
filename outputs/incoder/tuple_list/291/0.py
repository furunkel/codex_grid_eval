
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
    
    # your code here
    
    return lst[11]
</cell>
<cell>
# test your code
some_func([(2, 'a'), (3, 'b'), (4, 'c'), (5, 'd'), (6, 'e'), (7, 'f'), (8, 'g'), (9, 'h'), (10, 'i'), (11, 'j')])
</cell>
<text>
Problem 3
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given [1,2,2,3,4,4,4,5,5,5,6,6,6], it should return [1,3,4,5,6].


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, 
    remove duplicates and return a list of unique numbers.
    """
    
    # your code here
    
    return lst
</cell>
<cell>
# test your code
remove_duplicates([1,2,2,3,4,4,4,5,5,5,6,6,6])
</cell>
<text>
Problem 4
Write a function that returns a list consisting of the first element in the given list followed by all elements that are 2 indexes after it in a list.

For example, given [1,2,3,4,5,6,7], it should return [1,3,5,7].

Hint: You may want to use lst.index() to get the index of the current element you are looking at in the list.


</text>
<cell>
def two_index_after(lst):
    """
    Given a list of numbers, 
    return a list consisting of the first element in the given list followed by all elements that are 2 indexes after it in a list.
    """
    
    # your code here
    
    return lst
</cell>
<cell>
# test your code
two_index_after([1,2,3,4,5,6,7])
</cell>
<text>
Problem 5
Write a function that returns a list consisting of the first element in the given list followed by all elements that are 3 indexes after it in a list.

For example, given [1,2,3,4,5,6,7], it should return [1,4,7].

Hint: You may want to use lst.index() to get the index of the current element you are looking at in the list.


</text>
<cell>
def three_index_after(lst):
    """
    Given a list of numbers, 
    return a list consisting of the first element in the given list followed by all elements that are 3 indexes after it in a list.
    """
    
    # your code here
    
    return lst
</cell>
<cell>
# test your code
three_index_after([1,2,3,4,5,6,7])
</cell>
<text>
Problem 6
Write a function that returns a list consisting of the first element in the given list followed by all elements that are 4 indexes after it in a 