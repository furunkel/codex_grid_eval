
def f(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return lst[-1][1]

# Test your function
print(f([(1, 2), (3, 4)]))
</cell>
<text>
Exercise 3
Write a function that returns the first element of the tuple passed to it.


</text>
<cell>
def f(tup):
    """
    Given a tuple, write a function that returns the first element of the tuple.
    """
    return tup[0]

# Test your function
print(f((5, 4)))
</cell>
<text>
Exercise 4
Write a function that returns a list of all the even numbers in the list passed to it.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns a list of all the even numbers in the list.
    """
    return [x for x in lst if x % 2 == 0]

# Test your function
print(f([2, 6, 9, 12, 15]))
</cell>
<text>
Exercise 5
Write a function that returns a list of all the numbers between 1 and 100 (both included) which do not divide evenly into another number.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns a list of all the numbers between 1 and 100 (both included) which do not divide evenly into another number.
    """
    return [x for x in lst if x % 1 != 0]

# Test your function
print(f([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]))
</cell>
<text>
Exercise 6
Write a function that returns a list of all the numbers between 1 and 100 (both included) which do not divide evenly into another number and whose sum is evenly divisible by three.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns a list of all the numbers between 1 and 100 (both included) which do not divide evenly into another number and whose sum is evenly divisible by three.
    """
    return [x for x in lst if x % 1 != 0 and sum(x) % 3 == 0]

# Test your function
print(f([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48, 50, 52, 54, 56, 58, 60, 62, 64, 66, 68, 70, 72, 74, 76, 78, 80, 82, 84, 86, 88, 90, 92, 94, 96, 98, 100]))
</cell>
<text>
Exercise 7