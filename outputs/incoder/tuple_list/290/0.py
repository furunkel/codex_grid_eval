
def f(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest first value.
    """
    
    lst = sorted(lst)
    
    return lst[11][1]
</cell>
<cell>
# Test your code
lst = [(1, 2), (4, 5), (7, 8), (10, 11)]
print(f(lst))
</cell>
<text>
Tuples
A tuple is an (immutable) ordered list of values. A tuple is in many ways similar to a list; one of the most important differences is that tuples can be used as keys in dictionaries and as elements of sets, while lists cannot. Here is a trivial example:


</text>
<cell>
# Tuple example
tp = (1, 2, 3)
print(tp)
</cell>
<text>
Exercise
Write a function that returns a tuple with three elements: the first element is the sum of the elements of the argument tuple; the second element is the product of the elements of the argument tuple; and the third element is the maximum of the elements of the argument tuple.


</text>
<cell>
# Experiment with creating tuples and returning the results
def f(tup):
    """
    Given a tuple of numbers, return a new tuple with three elements:
    the sum of the numbers in the tuple; the product of the numbers in the tuple; and the maximum of the numbers in the tuple.
    """
    
    # YOUR CODE HERE
    
    return sum(tup), prod(tup), max(tup)
</cell>
<cell>
# Test your code
tup = (1, 2, 3)
print(f(tup))
</cell>
<text>
Dictionaries
A dictionary stores (key, value) pairs, similar to a Map in Java or an object in Python. If you have never used a dictionary before, it is worth your time to learn about them. Here is a trivial example:


</text>
<cell>
# Dictionary example
d = {'cat': 'cute', 'dog': 'furry'}
print(d['cat'])
</cell>
<text>
Exercise
Write a function that returns a dictionary with two keys: one for each element of the argument dictionary. The value for the corresponding key is the sum of the numbers in the argument dictionary that have that key.


</text>
<cell>
# Experiment with creating dictionaries and returning the results
def f(dic):
    """
    Given a dictionary of numbers, return a dictionary with two keys:
    the sum of the numbers in the dictionary that have key 'cute'; and the sum of the numbers in the dictionary that have key 'furry'.
    """
    
    # YOUR CODE HERE
    
    return {'cute': sum(v for k, v in dic.items() if k == 'cute'), 'furry': sum(v for k, v in dic.items() if k == '