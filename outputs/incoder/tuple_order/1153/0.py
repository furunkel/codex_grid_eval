
def make_tuple(a, b):
    """
    Given two integers a and b, return a tuple where:
    The second element contains the product of the two numbers.
    The third element contains the sum of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    """
    product = int(a) * int(b)
    sum = int(a) + int(b)
    difference = int(a) - int(b)
    return (product, sum, difference)


# Tests
def test_make_tuple():
    assert make_tuple(1, 2) == (1, 4, 2)
    assert make_tuple(2, 1) == (2, 3, 1)
    assert make_tuple(2, 2) == (2, 4, 2)
    assert make_tuple(2, 3) == (2, 5, 3)
    assert make_tuple(3, 2) == (3, 6, 2)
    assert make_tuple(3, 3) == (3, 7, 3)
    assert make_tuple(4, 3) == (4, 8, 3)
    assert make_tuple(5, 3) == (5, 9, 3)
    assert make_tuple(6, 3) == (6, 10, 3)
    assert make_tuple(7, 3) == (7, 11, 3)
    assert make_tuple(8, 3) == (8, 12, 3)
    assert make_tuple(9, 3) == (9, 13, 3)
    assert make_tuple(10, 3) == (10, 14, 3)
    assert make_tuple(11, 3) == (11, 15, 3)
    assert make_tuple(12, 3) == (12, 16, 3)
    assert make_tuple(13, 3) == (13, 17, 3)
    assert make_tuple(14, 3) == (14, 18, 3)
    assert make_tuple(15, 3) == (15, 19, 3)
    assert make_tuple(16, 3) == (16, 20, 3)
    assert make_tuple(17, 3) == (17, 21, 3)
    assert make_tuple(18, 3) == (18, 22, 3)
    assert make_tuple(19, 3) == (19, 23, 3)
    assert make_tuple(20, 3) == (20, 24, 3)
    assert make_tuple(21, 3) == (21, 25, 3)
    assert make_tuple(22, 3) == (22, 26, 3)
    assert make_tuple(23, 3) == (23, 27, 3)
    assert make_tuple(24, 3) == (24, 28, 3)
    assert make_tuple(25, 3) == (25, 29, 3)
    assert make_tuple(26, 3) == (26, 30, 3)
    assert make_tuple(27, 3) == (27, 31, 3)
    assert make_tuple(28, 3) == (28, 32, 3)
    assert make_tuple(29, 3) == (29, 33, 3)
    assert make_tuple(30, 3) == (30, 34, 3)
    assert make_tuple(31, 3) == (31, 35, 3)
    assert make_tuple(32, 3) == (32, 36, 3)
    assert make_tuple(33, 3) == (33, 37, 3)
    assert make_tuple(34, 3) == (34, 38, 3)
    assert make_tuple(35, 3) == (35, 39, 3)
    assert make_tuple(36, 3) == (36, 40, 3)
    assert make_tuple(37, 3) == (37, 41, 3)
    assert make_tuple(38, 3) == (