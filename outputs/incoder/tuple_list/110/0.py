
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest twelfth value.
    """
    return min(lst)[1]

# Test your function
print(f([(3, 'a'), (2, 'b'), (1, 'c'), (9, 'd')]))
</cell>
<text>
Exercise 3
Write a function that takes a list and returns a new list with each value repeated three times.

For example, f(['a', 'b', 'c', 'd']) should return ['aaa', 'aab', 'aac', 'aad', 'aba', 'abb', 'abc', 'abd', 'aca', 'acb', 'acc', 'acd', 'baa', 'bab', 'bac', 'bad', 'bba', 'bbb', 'bbc', 'bbd'] which should be a list of length 25

Hint: you can use the * operator to do this

</text>
<cell>
def f(lst):
    """
    Given a list of strings, write a function that returns a new list with each value repeated three times.
    """
    return [lst]*3

# Test your function
print(f(['a', 'b', 'c', 'd']))
</cell>
<text>
Exercise 4
Write a function that takes a list and returns a new list with each value repeated twice as the first value.

For example, f(['a', 'b', 'c', 'd']) should return ['aaa', 'aab', 'aac', 'aad', 'abb', 'baa', 'bab', 'bac', 'bba', 'bbb', 'bbc', 'bbd', 'bca', 'bcb', 'bcc', 'bcd', 'cba', 'cbb', 'cbc', 'cbd', 'cca', 'ccb', 'ccc', 'ccd'] which should be a list of length 25

Hint: you can use the * operator to do this

</text>
<cell>
def f(lst):
    """
    Given a list of strings, write a function that returns a new list with each value repeated twice as the first value.
    """
    return [lst]*2

# Test your function
print(f(['a', 'b', 'c', 'd']))
</cell>
<text>
Exercise 5
Write a function that takes a list and returns a new list with each value repeated twice as the last value.

For example, f(['a', 'b', 'c', 'd']) should return ['aaa', 'aab', 'aac', 'aad', 'abb', 'bba', 'bab', 'bca', 'bcb', 'bcc', 'bcd', 'caa', 'cab', 'cac', 'cba', 'cbb', 'cbc', 'cca', 'ccb', 'ccc', 'cca', 'ccb', 'ccc', 'ccd'] which should be a list of length 25

Hint: you can use the * operator to do this

</text>
<cell>
def f(lst):
    """
    Given a list of strings, write a function that returns a new list with each value repeated twice as the last value.
    """
    return [lst]*2

# Test your function
print(f(['a', 'b', 'c', 'd']))
</cell>
<text>
Exercise 6
Write a function that takes a list and returns a new list with each value repeated three times as the middle 