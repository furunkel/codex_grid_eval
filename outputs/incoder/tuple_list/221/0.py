
def min_max(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest first value.
    """
    
    smallest = lst[0]
    largest = lst[0]
    
    for tup in lst:
        if tup[0] < smallest[0]:
            smallest = tup
        elif tup[0] > largest[0]:
            largest = tup
    
    return largest[2]
</cell>
<cell>
# Test your code
lst = [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
print(min_max(lst))
</cell>
<text>
Tuples
A tuple is similar to a list, but only supports integers and strings. You can't change their values. When you create a tuple, it starts with parentheses instead of brackets.

The syntax for tuples is:

my_tuple = (x, y, z)
The values inside the parentheses are assigned to the variables x, y, and z. Tuple values can be of any type.

The values inside the parentheses are assigned to the variables x, y, and z. Tuple values can be of any type.

</text>
<cell>
# Create a tuple
t = (1, 2, 3)
</cell>
<cell>
# Assign values to x, y, z
x = y = z = 1
</cell>
<cell>
# Print out x, y, z
print(x,y,z)
</cell>
<text>
Strings
A string is a sequence of characters. In Python, we use the single quote (') to denote a string literal.

The syntax for strings is:

my_string = 'This is a string'
Strings are denoted by single quotes (') or double quotes (").

</text>
<cell>
# Create a string
t = 'This is a string'
</cell>
<cell>
# Print the type of t
print(type(t))
</cell>
<cell>
# Print the value of t
print(t)
</cell>
<cell>
# Print the value of t
print(type(t))
</cell>
<cell>
# Print the length of t
print(len(t))
</cell>
<cell>
# Print the first character of t
print(t[0])
</cell>
<cell>
# Print the last character of t
print(t[-1])
</cell>
<cell>
# Print the first two characters of t
print(t[:2])
</cell>
<cell>
# Print the value of t reversed
print(t[::-1])
</cell>
<cell>
# Print the first letter of t and assign it to a new variable
x = t[0]
</cell>
<cell>
# Print the first two letters of t and assign them to a new variables
(x, y) = t[0: