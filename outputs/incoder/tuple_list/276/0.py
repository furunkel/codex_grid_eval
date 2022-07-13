
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest last value.
    """
    lst = sorted(lst)
    return lst[-2][1]

# Test Cases
# Test Case 1
assert extract_value([]) == None
assert extract_value([1]) == 1
assert extract_value([(1,1)]) == 1
assert extract_value([(2,1),(1,1)]) == 2
assert extract_value([(2,1),(1,2),(3,4)]) == 4
assert extract_value([(2,1),(1,2),(3,4),(5,6)]) == 6
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8)]) == 8
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10)]) == 10
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12)]) == 12
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14)]) == 14
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16)]) == 16
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18)]) == 18
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20)]) == 20
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22)]) == 22
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24)]) == 24
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26)]) == 26
assert extract_value([(2,1),(1,2),(3,4),(5,6),(7,8),(9,10),(11,12),(13,14),(15,16),(17,18),(19,20),(21,22),(23,24),(25,26),