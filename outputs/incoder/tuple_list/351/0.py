
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest last value.
    """
    
    return min(lst)[1]
</cell>
<cell>
some_func([(3,4), (1,2), (5,6)])
</cell>
<text>
Problem 7
Write a function that returns the number of times a value appears in a list. For example, your function should work like this:

>>> count_elements([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3])
6
>>> count_elements([1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1, 2, 3, 1])
0
>>> count_elements([])
0
>>> count_elements([1])
1
>>> count_elements(['a', 'b', 'c', 'b'])
2
>>> count_elements({'a': 1, 'b': 2, 'c': 3})
2
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4})
0
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})
1
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6})
2
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12})
3
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15})
4
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16})
5
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17})
6
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18})
7
>>> count_elements({'a': 1, 'b': 2, 'c': 3, 'd': 4, '