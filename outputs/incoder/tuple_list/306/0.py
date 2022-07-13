
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    
    return max(lst, key=lambda x:x[1])[11]

#Test Cases
assert extract_value([]) == None
assert extract_value([1]) == 1
assert extract_value([(1,1)]) == 1
assert extract_value([(1,2), (1,1)]) == 2
assert extract_value([(1,2), (1,3), (1,1)]) == 3
assert extract_value([(1,2), (1,3), (1,4), (1,1)]) == 4
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,1)]) == 5
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,1)]) == 6
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,1)]) == 7
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,1)]) == 8
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,1)]) == 9
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,1)]) == 10
assert extract_value([(1,2), (1,3), (1,4), (1,5), (1,6), (1,7), (1,8), (1,9), (1,10), (1,11), (1,1)]) == 11
</cell>
<text>
Problem 3
Write a function that takes a list as an argument and returns a list where each element is the sum of the squares of the first and last elements in the list.


</text>
<cell>
def squares(lst):
    """
    Given a list of numbers, return a list where each element is the sum of the squares of the first and last elements in the list.
    """
    
    return [x**2 for x in lst] + [lst[-1]**2]

#Test Cases
assert squares([]) == []
assert squares([1]) == [1]
assert squares([1,1]) == [1,1]
assert squares([1,2,3]) == [6,9]
assert squares([1,2,3,4]) == [6,9,12]
assert squares([1,2,3,4,5]) == [6,9,12,15]
assert squares([1,2,3,4,5,6]) == [6,9,12,15,18]
assert squares([1,2,3,4,5,6,7]) == [6,9,12,15,18,21]
assert squares([1,2,3,4,5,6,7,8]) == [6,9,12,15,18,21,24]
assert squares([1,2,3,4,5,6,7,8,9]) == [6,9,12,15,18,21,24,27]
assert 