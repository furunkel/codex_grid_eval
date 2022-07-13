
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest second value.
    """
    
    # Your code here
    
    return max(lst, key=lambda x:x[1])[2]
</cell>
<cell>
# Test your code
assert fibonacci([0,1,1,2,3]) == 3, "fibonacci([0,1,1,2,3]) should return 3"
assert fibonacci([2,0,1,0,1]) == 1, "fibonacci([2,0,1,0,1]) should return 1"
assert fibonacci([2,0,1,0,1]) == 2, "fibonacci([2,0,1,0,1]) should return 2"
</cell>
<text>
Problem 8
Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. For example, fibonacci([0,1,1,2,3]) should return [0,1,4,9,16].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of numbers, return a list where each number is the square of the number at that index.
    """
    
    # Your code here
    
    return [i**2 for i in lst]
</cell>
<cell>
# Test your code
assert fibonacci([0,1,1,2,3]) == [0,1,4,9,16], "fibonacci([0,1,1,2,3]) should return [0,1,4,9,16]"
</cell>
<text>
Problem 9
Write a function that returns a set of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. For example, fibonacci([0,1,1,2,3]) should return {0,1,4,9,16}.


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of numbers, return a set where each number is the square of the number at that index.
    """
    
    # Your code here
    
    return {i**2 for i in lst}
</cell>
<cell>
# Test your code
assert fibonacci([0,1,1,2,3]) == {0,1,4,9,16}, "fibonacci([0,1,1,2,3]) should return {0,1,4,9,16}"
</cell>
<text>
Problem 10
Write a function that returns a list of numbers, such that $x_i=i^2$, for $1\leq i \leq n$. For example, fibonacci([0,1,1,2,3]) should return [0,1,4,9,16].


</text>
<cell>
def fibonacci(lst):
    """
    Given a list of numbers, return a list where each number is the square of the number at 