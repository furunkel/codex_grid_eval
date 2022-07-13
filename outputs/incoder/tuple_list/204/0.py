
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest last value.
    """
    
    lst = sorted(lst)
    return lst[2]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([(3, 'a'), (2, 'b'), (1, 'c')]) == 'c'
assert extract_value([(3, 'a'), (2, 'b'), (8, 'c')]) == 'c'
assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (8, 'd')]) == 'd'
</cell>
<cell>
# Define a function that takes in a list of tuples, and returns a list of all second elements from each tuple.
# For example, if the given list contains [(1, 2), (3, 4), (5, 6)], then the function should return [2, 3, 4].
def extract_second_value(lst):
    """
    Given a list of tuples, return a list containing the second element from each tuple.
    """
    
    lst = sorted(lst)
    return [lst[1] for lst in lst]
</cell>
<cell>
# Test your extract_second_value function below.
assert extract_second_value([(1, 2), (3, 4), (5, 6)]) == [2, 3, 4]
assert extract_second_value([(1, 2), (3, 4), (5, 'a')]) == [2, 3, 4]
</cell>
<cell>
# Define a function that takes in a list of tuples, and returns a list of all but the first element from each tuple.
# For example, if the given list contains [(1, 2), (3, 4), (5, 6)], then the function should return [(3, 4), (5, 6)].
def extract_all_but_first_value(lst):
    """
    Given a list of tuples, return a list containing all but the first element from each tuple.
    """
    
    lst = sorted(lst)
    return [lst[1:] for lst in lst]
</cell>
<cell>
# Test your extract_all_but_first_value function below.
assert extract_all_but_first_value([(1, 2), (3, 4), (5, 6)]) == [(3, 4), (5, 6)]
assert extract_all_but_first_value([(1, 2), (3, 4), (5, 'a')]) == [(3, 4), (5, 'a')]
</cell>
<text>
Great Job!

</text>
<text>


</text>
<text>
Extra Challenge
Can you write a single line of code that can extract all but the last element in a tuple? You might find the pop function useful.


</text>
<cell>
# Write your solution below:
</cell>
<text>


</text>
<text>
Extra Challenge
Can you write a single line of code that can extract all but the first element in a tuple? You might find the pop function useful.


</text>
<cell>
# Write your solution below:
</cell>