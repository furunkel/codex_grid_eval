
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(lst, key=lambda t: t[1])[11]

# Test your function
print(some_func([(7, 0), (3, 9), (2, 8), (5, 1), (8, 2), (4, 7), (6, 3), (9, 6)]))
</cell>
<text>
The second function above is called a list comprehension, and is often more efficient than using a for loop to iterate over a list. List comprehensions allow you to easily construct lists using a for loop, and are often faster than using a for loop to iterate over a list.

List comprehensions look very similar to for loops, but they differ in that instead of iterating over each element in a list, they iterate over each element in the list and then create a new list using the for loop. For example:


</text>
<cell>
# Example list comprehension
squares = []
for x in [1,2,3,4,5]:
    squares.append(x**2)
print(squares)
</cell>
<text>
They are also very useful for filtering lists:


</text>
<cell>
# Example list comprehension
even_squares = [x**2 for x in [1,2,3,4,5] if x % 2 == 0]
print(even_squares)
</cell>
<text>
They can also be used to construct dictionaries:


</text>
<cell>
# Example dictionary comprehension
{x: x**2 for x in [1,2,3,4,5]}
</cell>
<text>
They can also be used to construct sets:


</text>
<cell>
# Example set comprehension
{x for x in range(10)}
</cell>
<text>
They can also be used to construct tuples:


</text>
<cell>
# Example tuple comprehension
{(x, x**2) for x in range(10)}
</cell>
<text>
They can also be used to construct sets of sets:


</text>
<cell>
# Example set of sets comprehension
{frozenset([x]) for x in range(10)}
</cell>
<text>
They can also be used to construct dictionaries of dictionaries:


</text>
<cell>
# Example dictionary of sets comprehension
{frozenset(x.items()) for x in [{'a':1}, {'b':2}]}
</cell>
<text>
They can also be used to construct dictionaries of lists:


</text>
<cell>
# Example dictionary of lists comprehension
{frozenset(x.items()) for x in [{'a':1}, {'b':2}].values()}
</cell>
<text>
They can also be used to construct a numpy array from a list:


</text>
<cell>
# Example numpy array comprehension
np.array([x**2 for x in [1,2,3,4,5]])
</cell>
<text>
They can also be used to construct a numpy array from a dictionary:


</text>