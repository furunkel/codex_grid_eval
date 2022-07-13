
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    
    # Your code here
    
    return min(lst)[1]

# Test your code
lst = [(1, 2), (3, 1), (4, 5), (7, 9)]
print(some_func(lst))
</cell>
<text>
Problem 3
Use a for loop to iterate through the list below and print the result of the function call:

[(1, 2), (3, 1), (4, 5), (7, 9)]

</text>
<cell>
lst = [(1, 2), (3, 1), (4, 5), (7, 9)]

# Your code here
</cell>
<text>
Problem 4
Create a function that returns a list of numbers that sum to 100. For example, sum([1, 6, 3]) should return [3, 7, 10].

Hint: This is pretty easy with list comprehensions:

def sum_to(N):
    return [i * i for i in range(1, N + 1)]
Try it out yourself first.


</text>
<cell>
def sum_to(N):
    return [i * i for i in range(1, N + 1)]

# Test your code
print(sum_to(100))
</cell>
<text>
Problem 5
Create a function that returns a list of numbers that sum to 100. For example, sum([1, 6, 3]) should return [3, 7, 10].

Hint: This is pretty easy with list comprehensions:

def sum_to(N):
    return [i * i for i in range(1, N + 1)]
Try it out yourself first.


</text>
<cell>
def sum_to(N):
    return [i * i for i in range(1, N + 1)]

# Test your code
print(sum_to(100))
</cell>
<text>
Problem 6
Create a function that returns a list of numbers that sum to 100. For example, sum([1, 6, 3]) should return [3, 7, 10].

Hint: This is pretty easy with list comprehensions:

def sum_to(N):
    return [i * i for i in range(1, N + 1)]
Try it out yourself first.


</text>
<cell>
def sum_to(N):
    return [i * i for i in range(1, N + 1)]

# Test your code
print(sum_to(100))
</cell>
<text>
Problem 7
Create a function that returns a list of numbers that sum to 100. For example, sum([1, 6, 3]) should return [3, 7, 10].

Hint: This is pretty easy with list comprehensions:

def sum_to(N):
    return [i * i for i in range(1, N + 1)]
Try it out yourself first.


</text>
<cell>
def sum_to(N):
    return [i * i for i in range(1, N + 1)]

# Test your code
print(sum_to(100))
</cell>
<text>
Problem 8
Create a function that returns a list of numbers that sum to 100. For example, sum([1, 6, 3]) should return [3, 7, 10