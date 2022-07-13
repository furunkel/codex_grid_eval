
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest twelfth value.
    """
    lst = sorted(lst)
    return lst[-1][-1]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([(3, 'hi'), (2, 'bye'), (1, 'one')]) == 'one'
assert extract_value([(3, 'hi'), (2, 'bye'), (2, 'two')]) == 'two'
assert extract_value([(3, 'hi'), (2, 'bye'), (3, 'three')]) == 'three'
assert extract_value([(3, 'hi'), (2, 'bye'), (4, 'four')]) == 'four'
</cell>
<text>
Great! Now you have a function that can return the last element of a list with the smallest value of a specific key.

</text>
<text>
Problem 3: Find the 3 element with the smallest key value.
Write a function that returns a list of 3 tuples with the smallest key values from a list of tuples.

For example, given the list of tuples below, the function should return a list of 3 tuples that contains each of the smallest key values, (2, 'bye'), (3, 'three'), (4, 'four').

[(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]


</text>
<cell>
# YOUR CODE HERE
def extract_smallest_value(lst):
    """
    Given a list of tuples, write a function that returns a list of 3 tuples with the smallest key values.
    """
    lst = sorted(lst)
    return lst[:3]
</cell>
<cell>
# Test your extract_smallest_value function below.
assert extract_smallest_value([(3, 'hi'), (2, 'bye'), (1, 'one')]) == [(1, 'one'), (2, 'bye'), (3, 'three')]
assert extract_smallest_value([(3, 'hi'), (2, 'bye'), (2, 'two')]) == [(2, 'two'), (3, 'hi'), (2, 'bye')]
assert extract_smallest_value([(3, 'hi'), (2, 'bye'), (3, 'three')]) == [(3, 'three'), (2, 'bye'), (3, 'hi')]
assert extract_smallest_value([(3, 'hi'), (2, 'bye'), (4, 'four')]) == [(4, 'four'), (3, 'hi'), (2, 'bye')]
</cell>
<text>
Great! Now you have a function that can return the 3 tuples with the smallest key values.

</text>
<text>
Problem 4: Given a list of tuples, return a list with the 3 tuples with the largest key values.
Write a function that returns a list of 3 tuples with the largest key values from a list of tuples.

For example, given the list of tuples below, the function should return a list of 3 tuples that contains each of the largest key values, (3, 'three'), (4, 'four'), (