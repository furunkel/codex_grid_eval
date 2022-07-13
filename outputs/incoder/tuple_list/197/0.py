
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest eleventh value.
    """
    
    smallest = lst[0][2]
    largest = lst[0][2]
    
    for x in lst:
        if x[2] < smallest:
            smallest = x[2]
        if x[2] > largest:
            largest = x[2]
    
    return smallest, largest
</cell>
<cell>
# Test your code
lst = [(1, 2), (4, 5), (7, 3)]
print(min_max(lst))
</cell>
<text>
Great job!

</text>
<text>
Dictionaries
A dictionary consists of a key and a value.  You can create a dictionary by calling dict(). 
The keys in a dictionary are unique and can contain any data type.
The value in a dictionary can be of any data type.


</text>
<cell>
# Example dictionary
my_dict = {'key1':'value1', 'key2':[1,2,3], 'key3':True}
</cell>
<text>
You can access a dictionary by using the key and the index position of that key in the dictionary.


</text>
<cell>
# Print the value stored at index position 1
my_dict['key1']
</cell>
<text>
You can also access a dictionary by using the key and the value assigned to that key in the dictionary.


</text>
<cell>
# Print the value stored at key 'key2'
my_dict['key2']
</cell>
<text>
You can also access a dictionary by using the key in a conditional statement.


</text>
<cell>
# Print the key 'key2' if 'key1' is stored at index position 0
if 'key1' in my_dict:
    print(my_dict['key1'])
</cell>
<text>
You can also use the in keyword to check if a key is stored in a dictionary.


</text>
<cell>
# Print the key 'key2' if 'key1' is stored at index position 0
if 'key1' in my_dict:
    print('key1 exists')
else:
    print('key1 does not exist')
</cell>
<text>
Looping Dictionaries
Looping through a dictionary is similar to looping through a list.


</text>
<cell>
# Create a dictionary
my_dict = {'key1':1, 'key2':2, 'key3':3}
</cell>
<cell>
# Loop through the dictionary
for key in my_dict:
    print(key)
</cell>
<text>
Looping through a dictionary is similar to looping through a list.


</text>
<cell>
# Loop through the dictionary
for key in my_dict:
    print(key)
</cell>
<text>
Looping through a dictionary is similar to looping through a list.


</text>
<cell