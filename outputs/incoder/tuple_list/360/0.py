
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[-1][1]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([('E', 5), ('Frank', 8), ('I', 7)]) == 7
</cell>
<text>
For this question, extract the value from the second element in the tuple.


</text>
<cell>
# Extract value from second element in the tuple
extract_value(lst)
</cell>
<text>
Now write a function that returns a list of all the tuples with the first element equal to the passed in value.
For example, if the passed in value is 4, the returned value would be a list of all the tuples where the first element was 4.


</text>
<cell>
def extract_multiple(val, lst):
    """
    Given a list and a value, your code should return a list of all the tuples where the first element == the passed in value.
    """
    
    lst = sorted(lst)
    
    return [i for i in lst if i[0] == val]
</cell>
<cell>
# Test your extract_multiple function below.
assert extract_multiple(4, [(1, 'Male'), (2, 'Female'), (4, 'Male')]) == [(1, 'Male')]
</cell>
<text>
For this question, extract all the male tuples from the list.


</text>
<cell>
# Extract all the male tuples from the list
extract_multiple(4, lst)
</cell>
<text>
Great job!

</text>
<text>
Extra question: In one sentence, describe the process of sorting a list by the last element in the tuple. For example, given this list of tuples:

[(1, 2), (4, 5), (7, 1), (9, 3)]
your function should return this:

[(1, 2), (4, 5), (7, 1), (9, 3)]
The tuple with the smallest last element should go first.


</text>
<cell>
# Write your extract_multiple function here
</cell>
<text>
Solution
Solution notebook


</text>
<text>
Extra question: Write a function that returns a list of all the tuples with the largest first element. For example, given this list of tuples:

[(1, 2), (4, 5), (7, 1), (9, 3)]
your function should return this:

[(9, 3), (4, 5), (7, 1), (1, 2)]
The tuple with the largest first element should go first.


</text>
<cell>
# Write your extract_multiple function here
</cell>
<text>
Solution
Solution notebook


</text>
<text>
Extra question: Write a function that returns a list of all the tuples with the largest last element. For example, given this list of tuples:

[(1, 2), (4, 5), (7, 1), (9, 3)]
your function should 