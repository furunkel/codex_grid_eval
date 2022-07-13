
def some_func(lst):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest second value.
    """
    return max(lst, key=lambda t: t[1])[0]


# Test Cases
def test_some_func():
    assert some_func([(1, 2), (2, 3), (3, 4)])[0] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)])[2] == 4


def test_some_func_with_lambda():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[0] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[2] == 4


def test_some_func_with_lambda2():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[2] == 3


def test_some_func_with_lambda3():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[2] == 3


def test_some_func_with_lambda4():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[0] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[1] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[2] == 4


def test_some_func_with_lambda5():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[2] == 3


def test_some_func_with_lambda6():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[0] == 1
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[1] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[0])[2] == 3


def test_some_func_with_lambda7():
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[0] == 2
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[1] == 3
    assert some_func([(1, 2), (2, 3), (3, 4)], lambda t: t[1])[2] == 4


def test_some_func_with_lambda8():
    assert some_func([(1, 2), (2, 3), (3, 