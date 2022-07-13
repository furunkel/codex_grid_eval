
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return twelfth_val
</cell>
<cell>
# Test your code
some_func([(7, 4), (3, 8), (2, 5), (5, 1), (8, 6)])
</cell>
<text>
Tuples are immutable
A tuple is immutable - it cannot be changed.  But you can create a new tuple with the changed value.


</text>
<cell>
# Tuple with some values
my_tuple = (7, 4)
</cell>
<text>
Let's look at what happens when you try to change one of those values:


</text>
<cell>
# Try to change one of the values
my_tuple[0] = 100
</cell>
<text>
This is not allowed!  Remember that tuples are immutable, so this will not change the tuple in place, but instead will return a brand new tuple.

Now let's look at what happens when we try to create a new tuple:


</text>
<cell>
# Create a new tuple
my_new_tuple = my_tuple
</cell>
<text>
We get the same error as before!  This is because tuples are immutable, so you can't change them in-place.

Now let's see what happens when we try to replace the old tuple with the new tuple:


</text>
<cell>
# Replace the old tuple with the new tuple
my_tuple = my_new_tuple
</cell>
<text>
Now this works.  We didn't actually change anything.  We just created a new tuple.  But now we have two names for the same thing.  One name points to the original tuple, and the other name points to the new tuple.  So now we have multiple names for the same thing.

This is confusing and can cause confusion.  So don't do this!


</text>
<text>
Now let's see what happens when we try to append the new tuple to the old tuple:


</text>
<cell>
# Append the new tuple to the old tuple
my_tuple + my_new_tuple
</cell>
<text>
This doesn't work either.  Remember that tuples are immutable, so this will not change the tuple in place, but instead will return a brand new tuple.

So what happened is that when we tried to append the new tuple to the old tuple, we actually created a new tuple, and then tried to replace the old tuple with the new tuple.  This doesn't work because tuples are immutable, so you can't change them in-place.

Instead, let's try something else:


</text>
<cell>
# Create a new tuple
my_new_tuple = (1, 2, 3)
</cell>
<text>
Now let's see what happens when we try to replace the old tuple with the new tuple:


</text>
<cell>
# Replace the old tuple with the new tuple
my_tuple