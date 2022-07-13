
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    
    # Your code here
    
    return lst[-1][1]
</cell>
<cell>
# Test your function against a known result
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Great job!

</text>
<text>
Dictionaries
Next up, we briefly mention that Python dictionaries are mappings between keys and values. This means we can use them to store information in our code. To create a dictionary, we start by using the curly brackets {}. Like lists, we can also use them to store multiple values against a single key. Try googling "Python dictionary tutorial" to learn more.

To initialize a dictionary, we pass in a list of key-value pairs separated by commas. Try googling "Python dictionary examples" to learn more.


</text>
<cell>
# Create a dictionary with some data
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
</cell>
<text>
Now that we have created this dictionary, we can access its values by calling them using its keys. Try googling "Python dictionary access" to learn more.


</text>
<cell>
# Print the dictionary
my_dict
</cell>
<cell>
# Print the value stored against 'key2'
my_dict['key2']
</cell>
<text>
We can also add new key-value pairs to this dictionary by using the update() method. Try googling "Python dictionary update" to learn more.


</text>
<cell>
# Update 'my_dict' with 'new_key1':'new_value1'
my_dict.update({'new_key1':'new_value1'})
</cell>
<cell>
# Print the updated dictionary
my_dict
</cell>
<text>
Now try googling "Python dictionary delete key" to learn more.


</text>
<cell>
# Delete the key 'key2' from the dictionary
del my_dict['key2']
</cell>
<cell>
# Print the updated dictionary
my_dict
</cell>
<text>
Now try googling "Python dictionary popitem" to learn more.


</text>
<cell>
# Print the popped key-value pair
my_dict.popitem()
</cell>
<text>
Now try googling "Python dictionary pop" to learn more.


</text>
<cell>
# Print the popped value
my_dict.pop('key2')
</cell>
<text>
Now try googling "Python dictionary clear" to learn more.


</text>
<cell>
# Print the cleare