
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest first value.
    """
    return max(lst, key=lambda x: x[0])[1]

print(some_func([(1, 2), (10, 20), (100, 200)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2), (1, 2)]))
print(some_func([(1, 2), (10, 20), (100, 200), (1, 2), (1, 2), (1, 2