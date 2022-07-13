
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[-1][1]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([(3, 'hi'), (2, 'bye'), (1, 'one')]) == 'one'
assert extract_value([(3, 'hi'), (2, 'bye'), (5, 'one')]) == 'one'
assert extract_value([(3, 'hi'), (2, 'bye'), (3, 'one')]) == 'hi'
assert extract_value([(3, 'hi'), (2, 'bye'), (3, 'one'), (2, 'test')]) == 'hi'
</cell>
<text>
Putting it all together: Filtering tuples
Now write a function that uses filter() to return a tuple where the second element equals 'hi' and the first element equals 1.

The function should only require a single line of code, and should not use any loops.


</text>
<cell>
def filter_function(lst):
    """
    Given a list of tuples, return a list containing the tuples where the first element equals 'hi' and the second element equals 1.
    """
    
    return list(filter(lambda tup: tup[1] == 'hi' and tup[0] == 1, lst))
</cell>
<cell>
# Test your filter_function function below.
assert filter_function([(3, 'hi'), (2, 'bye'), (1, 'one'), (5, 'one')]) == [(3, 'hi'), (2, 'bye')]
assert filter_function([(3, 'hi'), (2, 'bye'), (3, 'one'), (2, 'test')]) == [(3, 'hi'), (2, 'bye')]
</cell>
<text>
Extra challenge: Finding the most common element
Write a function that returns a list of tuples with the most common element in the list.

The first element in the tuple should be the element that appears most number of times in the list. The second element in the tuple should be the count of that element.

For example, if the list contains [1, 1, 2, 3, 4, 4, 2, 2] your function should return [(1, 2), (3, 4), (2, 2)].

The list itself should not be sorted!


</text>
<cell>
def most_common(lst):
    """
    Given a list of tuples, return a list containing the tuples with the most common element in the list.
    """
    
    lst = sorted(lst)
    
    return list(zip(lst, list(map(lambda tup: tup[0], lst))).most_common())
</cell>
<cell>
# Test your most_common function below.
assert most_common([(3, 'hi'), (2, 'bye'), (1, 'one'), (5, 'one'), (3, 'hi'), (2, 'bye'), (3, 'one'), (2, 'test')]) == [(1, 2), (