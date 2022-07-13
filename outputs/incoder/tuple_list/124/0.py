
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest eleventh value.
    """
    lst = sorted(lst)
    return lst[1]

# Test Cases
print(fibonacci([(3,), (1,), (2,), (5,), (8,), (13,), (21,), (34,), (55,), (89,), (144,), (233,), (377,), (610,), (987,), (1597,), (2584,), (4181,), (6765,), (10946,), (17711,), (28657,), (46368,), (75025,), (121393,), (196418,), (317811,), (514229,), (832040,), (1346269,), (2178309,), (3524578,), (5702887,), (9227465,), (14930352,), (24157817,), (39088169,), (63245986,), (102334155,), (165580141,), (267914296,), (433494437,)]))
print(fibonacci([(3,), (1,), (2,), (5,), (8,), (13,), (21,), (34,), (55,), (89,), (144,), (233,), (377,), (610,), (987,), (1597,), (2584,), (4181,), (6765,), (10946,), (17711,), (28657,), (46368,), (75025,), (121393,), (196418,), (317811,), (514229,), (832040,), (1346269,), (2178309,), (3524578,), (5702887,), (9227465,), (14930352,), (24157817,), (39088169,), (63245986,), (102334155,), (165580141,), (267914296,), (433494437,)]))
print(fibonacci([(3,), (1,), (2,), (5,), (8,), (13,), (21,), (34,), (55,), (89,), (144,), (233,), (377,), (610,), (987,), (1597,), (2584,), (4181,), (6765,), (10946,), (17711,), (28657,), (46368,), (75025,), (121393,), (196418,), (317811,), (514229,), (832040,), (1346269,), (2178309,), (3524578,), (5702887,), (9227465,), (14930352,), (24157817,), (39088169,), (63245986,), (102334155,), (165580141,), (267914296,