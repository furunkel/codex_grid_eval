
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    
    # Your code here
    
    return twelfth_of_smallest_tuple
</cell>
<cell>
# Test your code
some_func([(7, 8), (2, 3), (5, 6)])
</cell>
<text>
If you did it right, you should expect to see:

2
3
5

</text>
<text>
Part 3: Finding the second minimum
Write a function that returns the second smallest element in a list.


</text>
<cell>
def second_smallest_element(lst):
    """
    Given a list of numbers, find the second smallest number
    """
    
    # Your code here
    
    return second_smallest_number
</cell>
<cell>
# Test your code
second_smallest_element([7, 8, 1, 5])
</cell>
<text>
If you did it right, you should expect to see:

1
1

</text>
<text>
Part 4: Finding the third minimum
Write a function that returns the third smallest element in a list.


</text>
<cell>
def third_smallest_element(lst):
    """
    Given a list of numbers, find the third smallest number
    """
    
    # Your code here
    
    return third_smallest_number
</cell>
<cell>
# Test your code
third_smallest_element([7, 8, 1, 5])
</cell>
<text>
If you did it right, you should expect to see:

1
1
1

</text>
<text>
Part 5: Finding the largest and smallest numbers in a list
Write a function that returns a tuple containing the largest and smallest numbers in a list.


</text>
<cell>
def largest_and_smallest_numbers(lst):
    """
    Given a list of numbers, return two tuples, containing
    the largest and smallest numbers
    """
    
    # Your code here
    
    return largest_number, smallest_number
</cell>
<cell>
# Test your code
largest_and_smallest_numbers([7, 8, 1, 5])
</cell>
<text>
If you did it right, you should expect to see:

(7, 1)
(8, 1)

</text>
<text>
Part 6: Finding the second largest and smallest numbers in a list
Write a function that returns a tuple containing the second largest and smallest numbers in a list.


</text>
<cell>
def second_largest_and_smallest_numbers(lst):
    """
    Given a list of numbers, return two tuples, containing
    the second largest and smallest numbers
    """
    
    # Your code here
    
    return second_largest_number, second_smallest_number
</