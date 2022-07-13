
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    
    lst = sorted(lst)
    
    return lst[-2][2]
</cell>
<cell>
# Test your extract_value function below.
assert extract_value([(3, 'hi'), (2, 'bye'), (1, 'one')]) == 'one'
assert extract_value([(3, 'hi'), (5, 'bye'), (1, 'one')]) == 'hi'
assert extract_value([(2, 'hi'), (3, 'bye'), (1, 'one')]) == 'hi'
assert extract_value([(2, 'hi'), (3, 'bye'), (5, 'one')]) == 'bye'
</cell>
<text>
Problem 3: Given a string, return a list containing only unique characters. Uniqueness across multiple strings is not guaranteed (i.e., ((...), (...)) is not the same as ((...), (...))).

</text>
<cell>
def extract_unique_chars(s):
    """
    Given a string, return a list containing only unique characters. Uniqueness across multiple strings is not guaranteed (i.e., ((...), (...)) is not the same as ((...), (...))).
    """
    
    lst = []
    
    for char in s:
        if char not in lst:
            lst.append(char)
            
    return lst
</cell>
<cell>
# Test your extract_unique_chars function below.
assert extract_unique_chars('hello') == ['h', 'e', 'l', 'l', 'o']
assert extract_unique_chars('hello ') == ['h', 'e', 'l', 'l', 'o', ' ']
assert extract_unique_chars('no repeats') == ['n', 'o', 'r', 'e', 'a', 't']
</cell>
<text>
Problem 4: Given a string, return a list containing only the characters that are in the string and their counts. You can do this with a for loop (i.e., not the map function which would work differently in Python 2 and Python 3).

</text>
<cell>
def extract_chars_and_counts(s):
    """
    Given a string, return a list containing only the characters that are in the string and their counts. You can do this with a for loop (i.e., not the map function which would work differently in Python 2 and Python 3).
    """
    
    lst = []
    
    for char in s:
        if char in lst:
            lst[char] += 1
        else:
            lst.append(char)
            
    return lst
</cell>
<cell>
# Test your extract_chars_and_counts function below.
assert extract_chars_and_counts('hello') == ['h', 1, 'e', 1, 'l', 2, 'l', 1, 'o', 1]
assert extract_chars_and_counts('hello ') == ['h', 1, 'e', 1, 'l', 