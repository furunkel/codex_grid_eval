
def multiples():
    """
    If we list all the natural numbers below 15 that are multiples of 5, 7 or 9, we get 5, 7, 9, 10 and 14. The product of these multiples is 44100.
    Return the product of all the multiples of 5, 7 or 9 below 100.
    """    
    
    multiples = []
    
    for n in range(15):
        if n % 5 == 0 and n % 7 == 0 and n % 9 == 0:
            multiples.append(n)
            
    return sum(multiples)
</cell>
<cell>
multiples()
</cell>
<text>
Great! Now you know how to check if a number is in a list and how to sum all the multiples of some number. Next we will learn about loops.


</text>
<text>
For Loops

</text>
<text>
For loops are a way to repeatedly execute a block of code until a certain condition is met. Let's look at a few examples:


</text>
<cell>
for n in range(10):
    print(n)
</cell>
<text>
We can also use range() to generate lists of numbers:


</text>
<cell>
for n in range(10):
    print(n, end=', ')
</cell>
<cell>
list(range(10))
</cell>
<text>
We can even have nested for loops:


</text>
<cell>
for n in range(10):
    for x in range(10):
        print(n, end=', ')
    print()
</cell>
<text>
range() does not include the upper bound. In the above example, we would have printed 10 lines, 0, 1, ... , 9.


</text>
<cell>
list(range(10))
</cell>
<text>
Sometimes we want to know the indexes of a for loop. range() gives us a list with the indexes of all the numbers. We can use enumerate for this:


</text>
<cell>
for n, x in enumerate(range(10)):
    print(n, x)
</cell>
<text>
We can also use while loops:


</text>
<cell>
i = 1
while i < 10:
    print(i)
    i += 1
</cell>
<text>
Functions

</text>
<text>
A function is a block of organized, reusable code that is used to perform a single, related action. Functions are easy to define and often make for cleaner and more readable code. There are different types of functions. For example, print is a function that prints stuff. sum is a function that adds numbers. len is a function that returns the length of a list. These are examples of a function that takes different types of arguments and does something with them.

Functions have to be defined. You can define functions in two ways:

Using the def keyword.
By assigning a function to a variable.

The assignment method has the syntax def function_name(arguments):.

The def keyword is used to define a function. All the arguments that you pass to a function are called arguments.

You can define functions with different types of arguments. For example, you can define a function with the following arguments:

def function_name(argument1, argument2, argument3): 
    # Do something
    # Return something

</text>