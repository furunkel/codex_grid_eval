
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(3298)
    75
    """
    if n<0:
        return 0
    if n%1837==0 and n%13==0:
        return 1
    if n%1837!=0 and n%13!=0:
        return 0
    return fizz_buzz(n//10)
</cell>
<cell>
fizz_buzz(3298)
</cell>
<text>
Exercise 2
Write a function that takes a string and returns the number of times each character appears in the string.
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('')
{}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r': 2, 'b': 2, 'c': 1, 'd': 1}
>>> count_chars('abracadabra')
{'a': 2, 'r