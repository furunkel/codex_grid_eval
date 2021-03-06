
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    
    return max(lst, key=lambda x:x[1])[0]

# Test Cases
assert fibonacci([(3,4), (5,6), (7,8)]) == 8
assert fibonacci([(3,4), (5,6), (7,8), (9,10)]) == 10
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12)]) == 13
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14)]) == 14
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16)]) == 15
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18)]) == 17
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20)]) == 19
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22)]) == 21
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24)]) == 23
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24), (25,26)]) == 25
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24), (25,26), (27,28)]) == 27
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24), (25,26), (27,28), (29,30)]) == 29
assert fibonacci([(3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24), (25,26), (27,28), (29,30), (31,32)]) == 31
assert fibonacci([(3,4), (5,6), (7,