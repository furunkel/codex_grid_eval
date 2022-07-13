
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(lst)[1]

# Test your extract_value function above
assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]) == 'd'
</cell>
<text>
Problem 4
Using max, find the value with the highest number of keys.


</text>
<cell>
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the highest number of keys.
    """
    return max(lst, key=len)[1]

# Test your extract_value function above
assert extract_value([(3, 'a'), (2, 'b'), (1, 'c'), (4, 'd')]) == 'd'
</cell>
<text>
Problem 5
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $0\leq i \leq 30$ (that is 30, 1, 32, ... , 30).

HINT: You can use a combination of range(n) and map/filter/list comprehensions to do this.


</text>
<cell>
def squares(max_num):
    """
    Generate a list of squares between 0 and max_num.
    
    For example, if
    max_num = 10
    Then the output should be
    [0, 4, 16, 36, 64]
    """
    
    # Your code here
    
    return [i**2 for i in range(max_num)]

# Test your squares function above
assert squares(10) == [0, 4, 16, 36, 64]
</cell>
<text>
Problem 6
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $0\leq i \leq 30$ (that is 30, 1, 32, ... , 30).

This function is very similar to the squares function you wrote earlier.


</text>
<cell>
def squares2(max_num):
    """
    Generate a list of squares between 0 and max_num.
    
    For example, if
    max_num = 10
    Then the output should be
    [0, 4, 16, 36, 64]
    """
    
    # Your code here
    
    return [i**2 for i in range(max_num)]

# Test your squares function above
assert squares2(10) == [0, 4, 16, 36, 64]
</cell>
<text>
Problem 7
Write a function that returns a list of numbers, such that $x_i=i^2$, for all $0\leq i \leq 30$ (that is 30, 1, 32, ... , 30).

This function is very similar to the squares function you wrote earlier.


</text>
<cell>
def squares3(max_num):
    """
    Generate a list of squares between 0 and max_