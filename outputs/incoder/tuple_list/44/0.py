
def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[2])[2]
</cell>
<cell>
# Test your code
lst = [(1, 2), (3, 4), (1, 3), (2, 4), (3, 5), (4, 5)]
print(f(lst))
</cell>
<text>
Tuples
A tuple is similar to a list, but only supports immutable objects. Tuples are created with parentheses instead of brackets.


</text>
<cell>
# Create a tuple
tup = 1, 2, 3
</cell>
<cell>
# Print the type
print(type(tup))
</cell>
<cell>
# Print the value
print(tup)
</cell>
<cell>
# Indexing - get the first value
print(tup[0])
</cell>
<cell>
# Indexing - get the first value
print(tup[-1])
</cell>
<cell>
# Slicing - get the first 2 values
print(tup[0:2])
</cell>
<cell>
# Slicing - get the first 2 values
print(tup[1:])
</cell>
<cell>
# Slicing - get the first 2 values
print(tup[:-1])
</cell>
<cell>
# Slicing - get the first 2 values
print(tup[:])
</cell>
<cell>
# Tuple unpacking - get the first value from the tuple
x, y = tup
print(x)
</cell>
<cell>
# Tuple unpacking - get the first value from the tuple
x, y, z = tup
print(x)
print(y)
print(z)
</cell>
<text>
Sets
A set is an unordered collection of unique elements. As a result, it cannot contain duplicate elements.


</text>
<cell>
# Create a set
my_set = set()
</cell>
<cell>
# Print the type
print(type(my_set))
</cell>
<cell>
# Print the value
print(my_set)
</cell>
<cell>
# Add an element to the set
my_set.add('Python')
</cell>
<cell>
# Print the set
print(my_set)
</cell>
<cell>
# Add another element to the set
my_set.add('R')
</cell>
<cell>
# Print the set
print(my_set)
</cell>
<cell>
# Remove an element from the set
my_set.remove('Python')
</cell>
<cell>
# Print 