
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    
    # Your code here
    
    return twelfth_val
</cell>
<cell>
# Test your code
some_func([(7, 4), (3, 2), (8, 1), (9, 0)])
</cell>
<text>
Tuples
You may have noticed that the syntax for tuples is quite similar to lists. Actually, tuples are "immutable", which means that once they are created, they cannot be changed. This is different from how strings work in Python. For example:


</text>
<cell>
# Tuple assignments without a tuple
first_name = "Chris"
last_name = "Kent"

# Tuple assignments with a tuple
first_name_tuple = ("Chris",)
last_name_tuple = ("Kent",)

# Unpacking a tuple
first_name, last_name = first_name_tuple
</cell>
<text>
Exercise
Write a function that takes a list and returns a tuple with two elements: the sum of the first elements of the list and the sum of the second elements of the list.


</text>
<cell>
def sum_of_first_and_second_elements(lst):
    """
    Given a list of numbers, return a tuple with two elements: the sum of the first elements of the list and the sum of the second elements of the list.
    """
    
    # Your code here
    
    return sum_of_first_elements, sum_of_second_elements
</cell>
<cell>
# Test your code
sum_of_first_and_second_elements([1, 2, 3, 4])
</cell>
<text>
Dictionaries
Dictionaries are very similar to lists. To create a dictionary, you use curly brackets and separate the keys and values by commas. For example:


</text>
<cell>
# Dictionary example
my_dict = {
    "key1": "value1",
    "key2": "value2",
    "key3": "value3"
}
</cell>
<text>
Exercise
Write a function that takes a dictionary as an input and returns a tuple with two elements: the sum of the values of the dictionary and the sum of the keys of the dictionary.


</text>
<cell>
def sum_of_dict_values(dictionary):
    """
    Given a dictionary, return a tuple with two elements: the sum of the values of the dictionary and the sum of the keys of the dictionary.
    """
    
    # Your code here
    
    return sum_of_values, sum_of_keys
</cell>
<cell>
# Test your code
sum_of_dict_values(my_dict)
</cell>
<text>
Exercise
Write a function that takes a dictionary as an input and returns a tuple with two elements: the sum of the values of the dictionary and the sum of the keys of the dictionary.


</text>
<cell>
def sum_of_dict_keys(dictionary):
    """
    Given a dictionary, 