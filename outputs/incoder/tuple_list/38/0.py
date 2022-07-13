
def f(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest twelfth value.
    """
    
    smallest_twelfth = lst[0][2]
    
    for tup in lst:
        if tup[2] < smallest_twelfth:
            smallest_twelfth = tup[2]
    
    return smallest_twelfth
</cell>
<cell>
# Test your code
lst = [(1, 2), (4, 5), (7, 3)]
print(f(lst))
</cell>
<text>
Tuples
A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:


</text>
<cell>
# Tuple with mixed types
tp = (1, 2.0, "text")
print(tp)
</cell>
<text>
Sets
A set is an unordered collection of distinct elements. As a simple example, consider the following:


</text>
<cell>
# Create a set
s1 = {1, 2, 3}
s2 = {4, 5, 6}
s3 = {1, 2, 4, 5}
print(s1)
print(s2)
print(s3)
</cell>
<text>
As you may have noticed, sets do not allow duplicate entries. This is one way in which they are similar to lists, except that they have no index to access individual elements. Here is an example of a set that does allow duplicate entries:


</text>
<cell>
# Create a set
s1 = {1, 2, 2, 2, 3}
s2 = {4, 5, 6}
s3 = {1, 2, 4, 5}
print(s1)
print(s2)
print(s3)
</cell>
<text>
Finally, note that sets do not allow duplicate entries. For example:


</text>
<cell>
# Create a set
s1 = {1, 2, 2, 2, 3}
s2 = {4, 5, 6}
s3 = {1, 2, 4, 5}
print(s1)
print(s2)
print(s3)
</cell>
<text>
Dictionaries
A dictionary stores (key, value) pairs, similar to a Map in Java or an object in Python.

A dictionary is an (unordered) set of key: value pairs. A key can be any immutable object (integer, string, float, tuple) or a user-defined object. The value can be of any type.

The keys in a dictionary must be unique.

A dictionary comprehension creates a dictionary by providing a list of key-value pairs to dict():


</text>
<cell>
# Create a new dictionary with some specified key-value pairs
d1 = {1: "One", 2: "Two", 3: "Three"}
print(d1)
</cell>
<text>
You can 