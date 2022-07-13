
def tuple_extract(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest twelfth value.
    """
    
    # Your code here
    
    return max(lst, key=lambda t: t[2])[2]
</cell>
<cell>
# Test your code
lst = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
print(tuple_extract(lst))
</cell>
<text>
If you did it right, you should expect to see [8, 8, 8].


</text>
<text>
Functions as Arguments
Now let's see how we can use functions as arguments. We'll start with a function that adds one to its argument:


</text>
<cell>
def adder(n):
    """
    Add one to a number.
    """
    
    # Your code here
    
    return n + 1
</cell>
<text>
We can now call this function to add 1 to our number:


</text>
<cell>
print(adder(1))
</cell>
<text>
But we can also define a function inside another function:


</text>
<cell>
def adder_function(n):
    """
    Add one to a number.
    """
    
    def incrementor(n):
        """
        Add one to a number.
        """
        
        # Your code here
        
        return n + 1
    
    return incrementor(n)
</cell>
<text>
Now we can call this function to add 1 to our number:


</text>
<cell>
print(adder_function(1))
</cell>
<text>
Functions as Arguments
Now let's see how we can use functions as arguments. We'll start with a function that adds one to its argument:


</text>
<cell>
def adder(n):
    """
    Add one to a number.
    """
    
    # Your code here
    
    return n + 1
</cell>
<text>
We can now call this function to add 1 to our number:


</text>
<cell>
print(adder(1))
</cell>
<text>
But we can also define a function inside another function:


</text>
<cell>
def adder_function(n):
    """
    Add one to a number.
    """
    
    def incrementor(n):
        """
        Add one to a number.
        """
        
        # Your code here
        
        return n + 1
    
    return incrementor(n)
</cell>
<text>
Now we can call this function to add 1 to our number:


</text>
<cell>
print(adder_function(1))
</cell>
<text>
Functions as Arguments
Now let's see how we can use functions as arguments. We'll start with a function that adds one to its argument:


</text>
<cell>
def adder(n):
    """
    Add one to a 