
def some_func(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[0]

print(some_func([(1,2), (3,4), (5,6)]))
print(some_func([(1,2), (3,4), (5,6), (7,8)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12), (13,14), (15,16), (17,18), (19,20), (21,22), (23,24)]))
print(some_func([(1,2), (3,4), (5,6), (7,8), (9,10), (11,12),