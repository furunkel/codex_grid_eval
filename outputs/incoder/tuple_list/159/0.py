
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest second value.
    """
    return min(lst)[2]

# Test your function
print(some_func([(3, 'a'), (2, 'b'), (1, 'c'), (9, 'd')]))
</cell>
<text>
Problem 4
Use a Python library to calculate the volume of a sphere given its radius.


</text>
<cell>
def sphere_volume(radius):
    """
    Calculate the volume of a sphere given its radius.
    """
    return 4/3 * math.pi * radius * radius * radius
</cell>
<cell>
# Test your function
print(sphere_volume(5))
</cell>
<text>
Problem 5
Use a Python library to calculate the surface area of a cylinder given its radius and height.


</text>
<cell>
def cylinder_area(radius, height):
    """
    Calculate the surface area of a cylinder given its radius and height.
    """
    return 0.5 * math.pi * (radius ** 2) * height
</cell>
<cell>
# Test your function
print(cylinder_area(8, 4))
</cell>
<text>
Problem 6
Write a function that takes in a list of 3-tuples and returns a list of their sum. If the list is empty, return 0


</text>
<cell>
def sum_of_three_tuples(list_of_tuples):
    """
    Given a list of 3-tuples, return a list with the sum of all numbers.
    """
    return sum(list_of_tuples)
</cell>
<cell>
# Test your function
print(sum_of_three_tuples([(7, 4, 9), (5, 2, 8), (3, 6, 7)]))
</cell>
<text>
Problem 7
Write a function that returns a list of numbers, such that duplicates are removed from the list. For example, if the list is [3, 3, 3, 3, 4, 4, 4, 4], then your function should return [3, 4, 4, 4].


</text>
<cell>
def remove_duplicates(lst):
    """
    Given a list of numbers, return a list without duplicates.
    """
    return list(set(lst))
</cell>
<cell>
# Test your function
print(remove_duplicates([3, 3, 3, 3, 4, 4, 4, 4]))
</cell>
<text>
Problem 8
Write a function that returns a default value if the provided argument is None. Otherwise, return the provided argument.


</text>
<cell>
def return_if_none(value):
    """
    Given a value, return a default value if the value is None.
    """
    return value if value is not None else 'No Value'
</cell>
<cell>
# Test your function
print(return_if_none(None))
</cell>
<text>
Problem 9
Write a Python function that takes a list, a value, and a default 