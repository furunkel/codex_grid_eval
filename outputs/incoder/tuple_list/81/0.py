
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest first value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[0])[1]
</cell>
<cell>
# Test your code
some_func([(3, 'a'), (2, 'b'), (1, 'c')])
</cell>
<text>
Great job!

</text>
<text>
Exercise 3
Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. Make sure it handles the case where $n<1$ by raising a ValueError.


</text>
<cell>
def squares(n):
    """
    Returns a list of squares of numbers from 1 to n, such that the 
    ith element of the returned list equals i^2.
    """
    
    # Your code here
    
    return [i ** 2 for i in range(1, n + 1)]
</cell>
<cell>
# Test your code
squares(5)
</cell>
<cell>
squares(0)
</cell>
<cell>
squares(3)
</cell>
<cell>
squares(10)
</cell>
<cell>
squares(100)
</cell>
<text>
Great job!

</text>
<text>
Exercise 4
Write a function that returns the square root of the sum of the squares of the numbers from 1 to $n$. Your function should raise a ValueError if $n<1$.


</text>
<cell>
def sum_of_squares(n):
    """
    Compute the sum of the squares of numbers from 1 to n.
    
    When summing 1^2 + 2^2 + 3^2 + ... + n^2, the formula used 
    below is more efficient than the summation below:
    
    sum((n * (n + 1)) / 2
    
    sum(i * (i + 1) / 2 for i in range(1, n))
    
    """
    
    # Your code here
    
    return sum(i ** 2 for i in range(1, n + 1))
</cell>
<cell>
# Test your code
sum_of_squares(5)
</cell>
<cell>
sum_of_squares(0)
</cell>
<cell>
sum_of_squares(3)
</cell>
<cell>
sum_of_squares(10)
</cell>
<cell>
sum_of_squares(100)
</cell>
<cell>
sum_of_squares(1000)
</cell>
<cell>
sum_of_squares(10000)
</cell>
<cell>
sum_of_squares(