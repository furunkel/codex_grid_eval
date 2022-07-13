
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst)[-1]

# Test the function
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
The function above is called a lambda function, and it can be called just like a normal function. The only difference is that it takes no arguments and it returns a value.

Lambda functions are useful because they can save you from having to define a function before you actually call it. They also allow you to pass functions as arguments to other functions. Let's see how we can use them in our own functions.


</text>
<text>
Exercise 3
Write a function that takes a list of tuples as an argument and returns the last value of the tuple with the largest twelfth value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst)[-1]

# Test the function
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Now let's see how we can use lambda functions to make our code more concise.


</text>
<text>
Exercise 4
Write a function that takes a list of tuples as an argument and returns the last value of the tuple with the largest twelfth value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key = lambda t: t[-1])[-1]

# Test the function
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Now let's see how we can use lambda functions to make our code more concise.


</text>
<text>
Exercise 5
Write a function that takes a list of tuples as an argument and returns the last value of the tuple with the largest twelfth value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key = lambda t: t[-1])[-1]

# Test the function
some_func([(1,2,3), (4,5,6)])
</cell>
<text>
Now let's see how we can use lambda functions to make our code more concise.


</text>
<text>
Exercise 6
Write a function that takes a list of tuples as an argument and returns the last value of the tuple with the largest twelfth value.


</text>
<cell>
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest twelfth value.
    """
    return max(lst, key = lambda t: t[-1])[-1]

# 