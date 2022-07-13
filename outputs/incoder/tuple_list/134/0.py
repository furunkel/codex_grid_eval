
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')]))
</cell>
<text>
Great Job!

</text>
<text>


</text>
<text>
Refactoring Code

</text>
<text>
Let's refactor our code. First, we don't need an argument for the function anymore, so let's remove it:


</text>
<cell>
def f():
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]
</cell>
<text>
Now let's see what happens when we call it:


</text>
<cell>
f()
</cell>
<text>
It doesn't work. Why? Because we didn't tell it what list to find the min of. Let's add that argument:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')]))
</cell>
<text>
Now it works. We passed the list we wanted to find the min of!

But we could have also passed the list directly:


</text>
<cell>
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')], lst=[(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')]))
</cell>
<text>
Better yet, we can give the function the list to find the min of, and it will then use that list to find the min of (which itself will be the second value of the tuple with the smallest last value):


</text>
<cell>
def f(lst, lst2):
    """
    Given a list of tuples and a second list, write a function that returns the second value of the tuple with the smallest last value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')], [(3, 'a'), (2, 'b'), (1, 'c'), (5, 'd')]))
</cell>
<text>