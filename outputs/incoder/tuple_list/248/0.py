
def f(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest third value.
    """
    lst = sorted(lst)
    return lst[-2][2]

print(f([(1, 2), (3, 4), (5, 6)]))
</cell>
<text>
Exercise 2
Write a function that takes a list as input and returns the sum of the elements of the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the sum of the numbers in the list.
    """
    lst = sorted(lst)
    return sum(lst)

print(f([10, 20, 30]))
</cell>
<text>
Exercise 3
Write a function that takes a list as input and returns the product of the elements of the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the product of the numbers in the list.
    """
    lst = sorted(lst)
    return lst[-1] * lst[-2] * lst[-3]

print(f([10, 20, 30]))
</cell>
<text>
Exercise 4
Write a function that takes a list as input and returns the largest element of the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the largest number in the list.
    """
    lst = sorted(lst)
    return lst[-1]

print(f([10, 20, 30]))
</cell>
<text>
Exercise 5
Write a function that takes a list as input and returns the smallest element of the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the smallest number in the list.
    """
    lst = sorted(lst)
    return lst[0]

print(f([10, 20, 30]))
</cell>
<text>
Exercise 6
Write a function that takes a list as input and returns the number of elements in the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list.
    """
    lst = sorted(lst)
    return len(lst)

print(f([10, 20, 30]))
</cell>
<text>
Exercise 7
Write a function that takes a list as input and returns the number of elements in the list that are greater than the element in the list.


</text>
<cell>
def f(lst):
    """
    Given a list of numbers, write a function that returns the number of elements in the list that are greater than the element in the list.
    """
    lst = sorted(lst)
    return len([x for x in lst if x > lst[-1]])

print(f([10, 20, 30]))
</cell>
<text>
Exercise 8
Write a function that takes a list as input and returns the number of elements in the list that are less than the element in the list.


</text>
<cell>