
def fibonacci(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    lst = sorted(lst)
    return lst[0][1]

# Test Cases
assert fibonacci([(0, 0), (2, 1), (3, 3)]) == 2
assert fibonacci([(0, 0), (2, 1), (3, 4)]) == 3
assert fibonacci([(0, 0), (2, 1), (3, 5)]) == 5
assert fibonacci([(0, 0), (2, 1), (3, 6)]) == 8
assert fibonacci([(0, 0), (2, 1), (3, 7)]) == 13
assert fibonacci([(0, 0), (2, 1), (3, 8)]) == 21
assert fibonacci([(0, 0), (2, 1), (3, 9)]) == 34
assert fibonacci([(0, 0), (2, 1), (3, 10)]) == 55
assert fibonacci([(0, 0), (2, 1), (3, 11)]) == 89
assert fibonacci([(0, 0), (2, 1), (3, 12)]) == 144
assert fibonacci([(0, 0), (2, 1), (3, 13)]) == 233
assert fibonacci([(0, 0), (2, 1), (3, 14)]) == 377
assert fibonacci([(0, 0), (2, 1), (3, 15)]) == 610
assert fibonacci([(0, 0), (2, 1), (3, 16)]) == 987
assert fibonacci([(0, 0), (2, 1), (3, 17)]) == 1597
assert fibonacci([(0, 0), (2, 1), (3, 18)]) == 2584
assert fibonacci([(0, 0), (2, 1), (3, 19)]) == 4181
assert fibonacci([(0, 0), (2, 1), (3, 20)]) == 6765
assert fibonacci([(0, 0), (2, 1), (3, 21)]) == 10946
assert fibonacci([(0, 0), (2, 1), (3, 22)]) == 17711
assert fibonacci([(0, 0), (2, 1), (3, 23)]) == 28657
assert fibonacci([(0, 0), (2, 1), (3, 24)]) == 46368
assert fibonacci([(0, 0), (2, 1), (3, 25)]) == 75025
assert fibonacci([(0, 0), (2, 1), (3, 26)]) == 121393
assert fibonacci([(0, 0), (2, 1), (3, 27)]) == 196418
assert fibonacci([(0, 0), (2, 1), (3, 28)]) == 317811
assert fibonacci([(0, 0), (2, 1), (3, 29)]) == 514229
assert fibonacci([(0, 0), (2, 1), (3, 30)]) == 832040
assert fibonacci([(0, 0), (2, 1), (3, 31)]) == 1346269
assert fibonacci([(0, 0), (2, 1), (3, 32