
def f(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the largest twelfth value.
    """
    return max(lst)[2]
</cell>
<cell>
# Test your code
f(lst)
</cell>
<text>
Write a function that takes a list and returns a new list with only the elements that satisfy some condition. For example, given [1,2,3,4,5,6] and condition is_even it should return [2,4,6].


</text>
<cell>
# Fill in the code below
def f(lst):
    """
    Given a list of numbers, return a list containing only the even numbers.
    """
    return [x for x in lst if x % 2 == 0]
</cell>
<cell>
# Test your code
f(lst)
</cell>
<text>
Write a function that takes a list and returns a new list with only the elements that do not satisfy some condition. For example, given [1,2,3,4,5,6] and condition is_even it should return [1,2,5,6].


</text>
<cell>
# Fill in the code below
def f(lst):
    """
    Given a list of numbers, return a list containing only the odd numbers.
    """
    return [x for x in lst if x % 2 != 0]
</cell>
<cell>
# Test your code
f(lst)
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers that satisfy some condition. For example, given [1,2,3,4,5,6] and condition is_even it should return [2,4,6].


</text>
<cell>
# Fill in the code below
def f(lst):
    """
    Given a list of numbers, return a list containing all the numbers.
    """
    return [x for x in lst if x > 0]
</cell>
<cell>
# Test your code
f(lst)
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers that do not satisfy some condition. For example, given [1,2,3,4,5,6] and condition is_even it should return [1,2,5,6].


</text>
<cell>
# Fill in the code below
def f(lst):
    """
    Given a list of numbers, return a list containing all the numbers.
    """
    return [x for x in lst if x < 0]
</cell>
<cell>
# Test your code
f(lst)
</cell>
<text>
Write a function that takes a list and returns a new list with all the numbers that satisfy some condition and another list with all the numbers that do not satisfy that condition. For example, given [1,2,3,4,5,6] and condition is_even it should return [2,4,6] and [1,2,5,6].


</text>
<cell>
# Fill in the code below
def f(lst, lst2):
    """
    Given a list of numbers, return a list containing all the 