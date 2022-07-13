
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(lst, key=lambda t: t[2])[2]


# Test Cases
def test_some_func():
    assert some_func([(1, 2), (2, 3), (3, 4)])[0] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)])[1] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)])[2] == 4


def test_some_func_2():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_3():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_4():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_5():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_6():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_7():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_8():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[2])[2] == 3


def test_some_func_9():
    assert some_func([(1, 2), (2, 3), (3, 4)], key=lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (