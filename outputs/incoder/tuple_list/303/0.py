
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return lst[11]
</cell>
<cell>
# Test your code
some_func([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd'), (5, 'e')])
</cell>
<text>
Dictionaries
Next up, we learn about dictionaries, which are unordered collections of key-value pairs. In Python, they are created using the dict keyword.


</text>
<cell>
# Sample dictionary
d = {'cat': 'cute', 'dog': 'furry'}
</cell>
<text>
The keys in a dictionary are accessed and stored using the key name, separated by a colon:


</text>
<cell>
# Print the keys in `d`
print(d.keys())
</cell>
<cell>
# Print the values in `d`
print(d.values())
</cell>
<cell>
# Print the items in `d`
print(d.items())
</cell>
<text>
We can also use methods like get and set to access values by their keys. For example, we can get the first value for a key using the get method:


</text>
<cell>
# Print the value for the key 'cat'
print(d.get('cat'))
</cell>
<text>
If we do not know the key name, we can use the in keyword to check whether a key is in the dictionary:


</text>
<cell>
print('cat' in d)
</cell>
<text>
We can also add new key-value pairs to dictionaries. For example, we can add a new key-value pair to d using the set method:


</text>
<cell>
# Create a new key-value pair with the key 'fish' and value 'fleas'
d.update({'fish': 'fleas'})
</cell>
<text>
We can add multiple key-value pairs to d at once:


</text>
<cell>
# Create a new key-value pair with the key 'fish' and value 'fleas'
d.update({'cat': 'cute', 'fish': 'fleas'})
</cell>
<text>
We can delete key-value pairs from d using the pop method:


</text>
<cell>
# Create a new key-value pair with the key 'fish' and value 'fleas'
d.update({'cat': 'cute', 'fish': 'fleas'})
</cell>
<cell>
# Print the key-value pairs in `d`
print(d.items())
</cell>
<cell>
# Delete the key 'fish' from the dictionary
d.pop('fish')
</cell>
<cell>
# Print the key-value pairs in `d`
print(d.items())
</cell>
<text>
