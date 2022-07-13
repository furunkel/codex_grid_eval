
def f(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[2][2]
</cell>
<cell>
# Test your code
lst = [(1, 2), (4, 5), (7, 8), (10, 11)]
print(f(lst))
</cell>
<text>
(OPTIONAL) More on Lambda Expressions
A lambda expression is a concise way to define a function inline. 
It looks like this: lambda x: expression
The expression can be any valid Python expression. 
It could be a statement or an expression.
It could even be a whole function definition. 
Lambda expressions come in handy when you want to quickly define a function but don't want to clutter your code.

Here's an example of lambda expressions:


</text>
<cell>
# Defining a function called 'f' that takes one argument
def f(x):
    return x**2

# Defining a function called 'g' that takes one argument and multiplies it by 2
g = lambda x: x*2

# Defining a function called 'h' that takes one argument and adds 3 to it
h = lambda x: x + 3

# Defining a function called 'i' that takes one argument and subtracts 5 from it
i = lambda x: x - 5

# Defining a function called 'j' that takes one argument and returns the value of x squared
j = lambda x: x ** 2
</cell>
<text>
Now let's test our functions:


</text>
<cell>
# Test your function
print(f(3))
print(g(3))
print(h(3))
print(i(3))
print(j(3))
</cell>
<text>
Great! Now you know how to use lambda expressions.

</text>
<text>
(OPTIONAL) More on List Comprehensions
List comprehensions provide a concise way to create lists. 
They are faster than regular loops.
They are also more memory efficient.
They are often faster than regular loops.

Here's an example:


</text>
<cell>
# Defining a function called 'f' that returns a list of squares of numbers less than 10
def f(x):
    return [x**2 for x in x if x < 10]

# Defining a function called 'g' that returns a list of squares of numbers less than 10
def g(x):
    return [x**2 for x in x if x < 100]

# Defining a function called 'h' that returns a list of squares of numbers less than 10
def h(x):
    return [x**2 for x in x if x < 1000]
</cell>
<text>
Now let's test our functions:


</text>
<cell>