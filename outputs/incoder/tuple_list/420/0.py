
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest last value.
    """
    lst = sorted(lst)
    return lst[-1][1]

# Write your extract_value function here
</cell>
<cell>
# Test your extract_value function below
assert extract_value([(3, 'a'), (2, 'b'), (1, 'c')]) == 'c'
assert extract_value([(3, 'a'), (2, 'b'), (2, 'c')]) == 'c'
assert extract_value([(3, 'a'), (2, 'b'), (3, 'c')]) == 'c'
assert extract_value([(3, 'a'), (2, 'b'), (3, 'c'), (2, 'd')]) == 'd'
assert extract_value([(3, 'a'), (2, 'b'), (3, 'c'), (2, 'd'), (1, 'e')]) == 'd'
assert extract_value([(3, 'a'), (2, 'b'), (3, 'c'), (2, 'd'), (1, 'e'), (4, 'f')]) == 'f'
</cell>
<text>
And finally, write an extract_all function that takes a list and returns a list of all the values in the list.
For example [1,5,10,2,3,6,8,0] returns [5,6,8,10].


</text>
<cell>
def extract_all(lst):
    """
    Given a list of tuples, write a function that returns all the values in the list.
    """
    return lst
</cell>
<cell>
# Test your extract_all function below
assert extract_all([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]) == ['a', 'b', 'c', 'd']
assert extract_all([(3, 'a'), (2, 'b'), (3, 'c'), (2, 'd'), (4, 'e')]) == ['a', 'b', 'c', 'd', 'e']
</cell>
<text>
Great! Now you have a complete function that can act on a single list.


</text>
<cell>
def extract_all(lst):
    """
    Given a list of tuples, write a function that returns all the values in the list.
    """
    return sorted(lst)
</cell>
<text>
And now let's test your function


</text>
<cell>
assert extract_all([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]) == ['a', 'b', 'c', 'd']
assert extract_all([(3, 'a'), (2, 'b'), (3, 'c'), (2, 'd'), (4, 'e')]) == ['a', 'b', 'c', 'd', 'e']
</cell>
<text>
Finally, write a function that takes a list and returns a tuple where the first element is the smallest last value of the tuples in the list, and the second element is the largest last value of the tuples in the list.
For example, if the input list is [(2, 2), (4, 4), (6, 6), (8, 8)], the output should be (2, 8).


</text>
<cell>
def largest_last(lst