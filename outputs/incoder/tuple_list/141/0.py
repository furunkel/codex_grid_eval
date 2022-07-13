
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest last value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x: x[-1])[1]
</cell>
<cell>
# Test your code
some_func([(2, 'a'), (3, 'b'), (4, 'c')])
</cell>
<text>
The key thing to notice is that the key argument to max is a function that returns a tuple. The first element of the tuple is the value you are looking for, and the second element is the tuple itself. So the key function needs to return the first element of the tuple that you are looking for.

For this problem, the key function is just the last element of the tuple.


</text>
<text>
Problem 4: Finding the second largest value
Write a function that takes a list of numbers and returns the second largest value.

If there is no second largest value, return None.

If the list contains less than two values, return None.


</text>
<cell>
def second_largest_value(lst):
    """
    Given a list of numbers, find the second largest value.
    
    Your code here
    
    return second_largest_value
</cell>
<cell>
# Test your code
second_largest_value([4, 5, 3, 2])
</cell>
<text>
Problem 5: Finding the third largest value
Write a function that takes a list of numbers and returns the third largest value.

If there is no third largest value, return None.

If the list contains less than three values, return None.


</text>
<cell>
def third_largest_value(lst):
    """
    Given a list of numbers, find the third largest value.
    
    Your code here
    
    return third_largest_value
</cell>
<cell>
# Test your code
third_largest_value([4, 5, 3, 2])
</cell>
<text>
Problem 6: Finding the largest value
Write a function that takes a list of numbers and returns the largest value.

If there is no largest value, return None.

If the list contains less than three values, return None.


</text>
<cell>
def largest_value(lst):
    """
    Given a list of numbers, find the largest value.
    
    Your code here
    
    return largest_value
</cell>
<cell>
# Test your code
largest_value([4, 5, 3, 2])
</cell>
<text>
Problem 7: Finding the average value
Write a function that takes a list of numbers and returns the average value.

If there is no average value, return None.

If the list contains less than three values, return None.


</text>
<cell>
def average_value(lst):
    """
    Given a list of numbers, find the average value.
    
    Your code here
    
    return average_value
</cell>
<cell>
# Test your code
average_value([4, 5, 3, 