
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[-11]
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10), (11, 12), (13, 14), (15, 16)]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed.

For example, given [1, 1, 2, 3, 4, 4, 4, 4] it should return [1, 2, 3, 4].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element appears only once.
    """
    
    # Your code here
    
    return list(set(lst))
</cell>
<cell>
# Test your code
lst = [1, 1, 2, 3, 4, 4, 4, 4]
print(f(lst))
</cell>
<text>
Write a function that returns a new list with all of the duplicates removed and is sorted.

For example, given [1, 1, 2, 3, 4, 4, 4, 4] it should return [1, 1, 2, 3, 4, 4].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element appears only once and in sorted order.
    """
    
    # Your code here
    
    return sorted(list(set(lst)))
</cell>
<cell>
# Test your code
lst = [1, 1, 2, 3, 4, 4, 4, 4]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed and is sorted in ascending order.

For example, given [1, 1, 2, 3, 4, 4, 4, 4] it should return [1, 2, 3, 4].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element appears only once and in sorted order.
    """
    
    # Your code here
    
    return sorted(list(set(lst)), key=int)
</cell>
<cell>
# Test your code
lst = [1, 1, 2, 3, 4, 4, 4, 4]
print(f(lst))
</cell>
<text>
Write a function that takes a list and returns a new list with all of the duplicates removed and is sorted in descending order.

For example, given [1, 1, 2, 3, 4, 4, 4, 4] it should return [4, 4, 4, 3, 2, 1].


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, return a list where each element appears only once and in sorted order.
    """
    
    # Your code here
    
    return sorted(list(set(lst)), key=int)[::-1]
</cell>
<cell>
# Test your code
lst = [1, 1, 