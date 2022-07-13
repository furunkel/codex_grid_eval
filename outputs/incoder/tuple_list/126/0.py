
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest eleventh value.
    """
    
    return max(lst, key=lambda x:x[1])[11]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([(3, 'hi'), (2, 'bye'), (1, 'one')]) == 'one'
assert extract_value([(3, 'hi'), (2, 'bye'), (5, 'one')]) == 'hi'
</cell>
<text>
List Comprehensions
List comprehensions provide a concise way to create lists. You can use these to create new lists where each element is the result of some operations applied to each member of another list.

For example here is a function that creates a list of all even numbers from 0 to nine.


</text>
<cell>
def even_numbers(n):
    """
    Returns an `n`-element list of numbers from 0 to `n` where each number
    is evenly divisible by 2.
    """
    
    return [x*2 for x in xrange(n) if x%2==0]
</cell>
<text>
Now here is how the function can be used with a list comprehension.


</text>
<cell>
even_numbers(10)
</cell>
<text>
For a function that returns multiple values you can use a tuple to unpack them. Here is an example of a function that returns multiple values.


</text>
<cell>
def odd_numbers(n):
    """
    Returns an `n`-element list of numbers from 0 to `n` where each number
    is odd and is evenly divisible by 3.
    """
    
    return [x*3 for x in xrange(n) if x%2==0]
</cell>
<text>
Now here is how the function can be used with a list comprehension.


</text>
<cell>
odd_numbers(10)
</cell>
<text>
Dictionaries
Dictionaries are a common and useful data structure in programming. Dictionaries are created with curly brackets {}. Dictionaries are used to store data where the keys are unique strings and the values are the values associated with those keys.

You can create a dictionary by placing values inside of curly brackets {}. Note that the order that you specify the key-value pairs matters. Dictionaries are unordered collections of key-value pairs. Here is how we create a dictionary with a single key-value pair.


</text>
<cell>
# Create a dictionary with one key-value pair.
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
</cell>
<text>
Now let's look at what this dictionary looks like.


</text>
<cell>
my_dict
</cell>
<text>
Accessing dictionary values
You can access dictionary values by using square brackets and the key name of the value. 