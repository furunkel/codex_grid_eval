
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test case
print(extract_value([(1, 2), (2, 3), (3, 4)]))
</cell>
<text>
Problem 5
Write a function that returns a list of all the integers from 1 to n that are divisible by 3.


</text>
<cell>
def divisible_by_three(n):
    """
    Given a number n, return a list of all the integers from 1 to n that are divisible by 3.
    """
    
    # Your code here
    
    return list(range(1, n+1))

# Test case
print(divisible_by_three(10))
</cell>
<text>
Problem 6
Write a function that returns a list of all the integers from 1 to n that are divisible by 5.


</text>
<cell>
def divisible_by_five(n):
    """
    Given a number n, return a list of all the integers from 1 to n that are divisible by 5.
    """
    
    # Your code here
    
    return list(range(1, n+1))

# Test case
print(divisible_by_five(10))
</cell>
<text>
Problem 7
Write a function that returns a list of all the integers from 1 to n that are divisible by both 3 and 5.


</text>
<cell>
def divisible_by_three_and_five(n):
    """
    Given a number n, return a list of all the integers from 1 to n that are divisible by both 3 and 5.
    """
    
    # Your code here
    
    return list(range(1, n+1))

# Test case
print(divisible_by_three_and_five(10))
</cell>
<text>
Problem 8
Write a function that returns a list of all the integers from 1 to n that are divisible by either 3 or 5.


</text>
<cell>
def divisible_by_either_3_or_five(n):
    """
    Given a number n, return a list of all the integers from 1 to n that are divisible by either 3 or 5.
    """
    
    # Your code here
    
    return list(range(1, n+1))

# Test case
print(divisible_by_either_3_or_five(10))
</cell>
<text>
Problem 9
Write a function that returns a list of all the integers from 1 to n that are divisible by 3 or 5.


</text>
<cell>
def divisible_by_3_or_five(n):
    """
    Given a number n, return a list of all the integers from 1 to n that are divisible by 3 or 5.
    """
    
    # Your code here
    
    return list(range(1, n+1))

# Test case
print(divisible_by_3_or_five(10))
</cell>
<text>
Problem 10