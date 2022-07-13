
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(lst, key=lambda x:x[2])[-1]

# Test Cases
assert extract_value([]) == None
assert extract_value([(1,2,3), (4,5,6)]) == 6
assert extract_value([(1,2,3), (4,5,6), (7,8,9)]) == 9
assert extract_value([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == 12
assert extract_value([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)]) == 15
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list with all the even numbers in that list. For example, if the argument was [1,2,3,4,5,6,7,8,9], the function should return [2,4,6,8]. Make sure the function handles the case where the list passed in is empty.


</text>
<cell>
def extract_evens(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return list(filter(lambda x:x%2==0, lst))

# Test Cases
assert extract_evens([]) == []
assert extract_evens([(1,2,3), (4,5,6)]) == [2,4,6]
assert extract_evens([(1,2,3), (4,5,6), (7,8,9)]) == [2,4,6,8]
assert extract_evens([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == [2,4,6,8,10]
assert extract_evens([(1,2,3), (4,5,6), (7,8,9), (10,11,12), (13,14,15)]) == [2,4,6,8,10,12]
</cell>
<text>
Problem 4
Write a function that takes a list as an argument and returns a list with all the odd numbers in that list. For example, if the argument was [1,2,3,4,5,6,7,8,9], the function should return [1,3,5,7,9].


</text>
<cell>
def extract_odds(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return list(filter(lambda x:x%2!=0, lst))

# Test Cases
assert extract_odds([]) == []
assert extract_odds([(1,2,3), (4,5,6)]) == [1,3,5,7]
assert extract_odds([(1,2,3), (4,5,6), (7,8,9)]) == [1,3,5,7,9]
assert extract_odds([(1,2,3), (4,5,6), (7,8,9), (10,11,12)]) == [1,3,5,7,9,11]
assert extract_odds([(1,2,3), (4,5,6), (7,8,9), (10,11,