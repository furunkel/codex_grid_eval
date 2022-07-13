
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    
    return max(lst)[1]

# Test your function
print(tuple_extract(lst))
</cell>
<text>
Expected output
4

</text>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given [1,1,1,2,2,3], return [1,2,3].

Use the remove() method of the list object.


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a new list with all of the duplicates removed.
    """
    
    return lst.remove()

# Test your function
print(remove_duplicates([1,1,1,2,2,3]))
</cell>
<text>
Expected output
[1, 2, 3]

</text>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed while maintaining the original order.

For example, given [1,1,1,2,2,3], return [1,3,2,3]. You cannot use sort for this problem.

Hint: You can create a new list by splicing together a copy of the list with itself after it has been sorted.


</text>
<cell>
def remove_duplicates_sorted(lst):
    """
    Given a list of numbers, return a new list with all of the duplicates removed while maintaining the original order.
    """
    
    return lst[:]

# Test your function
print(remove_duplicates_sorted([1,1,1,2,2,3]))
</cell>
<text>
Expected output
[1, 3, 2, 3]

</text>
<text>
Write a function that counts the number of items in a list that aren’t in a second list. For example, given [1,2,3,4,5,6] and [1,3,5,6], return [1,2].

This may look like an odd problem to write but there are many valid ways to do it. HINT: You can use the count() method of a list.


</text>
<cell>
def count_not_in(lst, lst2):
    """
    Given a list of numbers and a list of numbers, return a new list with the number of items in the first list that aren’t in the second.
    """
    
    return lst.count()

# Test your function
print(count_not_in([1,2,3,4,5,6], [1,3,5,6]))
</cell>
<text>
Expected output
1

</text>
<text>
Write a function that returns a list of numbers, such that duplicates are removed from the list and the list is sorted.

For example, given [1,2,3,4,5,6], return [1,2,4,5,6].

Use the sort() method of the list object.


</text>
<cell>
def remove_duplicates_sorted(lst):
    """
    Given a list of numbers, return a new list with all of the duplicates removed while maintaining the original order.
    """
    
    return lst.sort()

# Test your function
print(remove_duplicates_