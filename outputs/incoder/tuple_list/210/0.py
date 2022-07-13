
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst)[2]

# Test Cases
assert extract_value([]) == None
assert extract_value([(1,2,3)]) == 3
assert extract_value([(1,2,3), (4,5,6)]) == 6
assert extract_value([(1,2,3), (4,5,6), (7,8,9)]) == 9
assert extract_value([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == 12
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list with the first two values of the tuple with the largest last value.


</text>
<cell>
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst)[:2]

# Test Cases
assert extract_value([]) == None
assert extract_value([(1,2,3)]) == [2,3]
assert extract_value([(1,2,3), (4,5,6)]) == [5,6]
assert extract_value([(1,2,3), (4,5,6), (7,8,9)]) == [8,9]
assert extract_value([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == [11,12]
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list with the first two values of the tuple with the largest last value.


</text>
<cell>
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst)[:2]

# Test Cases
assert extract_value([]) == None
assert extract_value([(1,2,3)]) == [2,3]
assert extract_value([(1,2,3), (4,5,6)]) == [5,6]
assert extract_value([(1,2,3), (4,5,6), (7,8,9)]) == [8,9]
assert extract_value([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == [11,12]
</cell>
<text>
Problem 5
Write a function that takes a list as an argument and returns a list with the first two values of the tuple with the largest last value.


</text>
<cell>
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the largest last value.
    """
    return max(lst)[:2]

# Test Cases
assert extract_value([]) == None
assert extract_value([(1,2,3)]) == [2,3]
assert extract_value([(1,2,3), (4,5,6)]) == [5,6]
assert extract_value([(1,2,3), (4,5,6), (7,8,9)]) == [8,9]
assert extract_