
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest eleventh value.
    """
    
    # Your code here
    
    return min(lst)[1]
</cell>
<cell>
# Test your code
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Dictionaries
Dictionaries are very useful data structures to store data that you want to access by key. Dictionaries are created with curly brackets {}. Dictionaries are also very useful when you want to store multiple values against a single key. Let's see some examples:


</text>
<cell>
# Create a dictionary with some data
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
</cell>
<cell>
# Access a value from a dictionary
my_dict['key1']
</cell>
<cell>
# Update a value
my_dict['key1'] = 'new value'
</cell>
<cell>
# Delete a value
del my_dict['key1']
</cell>
<cell>
# Print out all the keys and values from the dictionary
print(my_dict)
</cell>
<text>
Now let's see how we can use dictionaries to replace if-else statements in our code. Let's start by defining a function called get_info that takes in an info parameter and prints out some information about the person in our list.


</text>
<cell>
def get_info(info):
    """
    Given an info parameter, print out some information about that person.
    """
    
    # Your code here
    
    print(info)
</cell>
<text>
Now let's see how we can call this function on every person in our list. Let's start by creating an empty dictionary called my_dict_info.


</text>
<cell>
my_dict_info = {}
</cell>
<text>
Now let's call the get_info function on every person in our list. Remember that in Python, indentation is very important and should be kept consistent.


</text>
<cell>
for person in people:
    get_info(person)
</cell>
<text>
Now let's see how we can use dictionaries to replace if-else statements in our code. Let's start by defining a function called get_info that takes in an info parameter and prints out some information about the person in our list.


</text>
<cell>
def get_info(info):
    """
    Given an info parameter, print out some information about that person.
    """
    
    # Your code here
    
    print(info)
</cell>
<text>
Now let's see how we can call this function on every person in our list. Let's start by creating an empty dictionary called my_