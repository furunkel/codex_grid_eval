
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "house" if n >= 2 (and None if -100 <= n < 2).
    """
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    else:
        return None


@njit
def small_or_large_with_if(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    else:
        return None


@njit
def small_or_large_with_if_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    else:
        return "dog"


@njit
def small_or_large_with_if_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    else:
        return "dog"


@njit
def small_or_large_with_if_elif_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    elif n >= 3:
        return "dog"
    else:
        return "cat"


@njit
def small_or_large_with_if_elif_elif_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    elif n >= 3:
        return "dog"
    elif n >= 4:
        return "cat"
    else:
        return "fish"


@njit
def small_or_large_with_if_elif_elif_elif_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    elif n >= 3:
        return "dog"
    elif n >= 4:
        return "cat"
    elif n >= 5:
        return "fish"
    else:
        return "turtle"


@njit
def small_or_large_with_if_elif_elif_elif_elif_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    elif n >= 3:
        return "dog"
    elif n >= 4:
        return "cat"
    elif n >= 5:
        return "fish"
    elif n >= 6:
        return "turtle"
    else:
        return "horse"


@njit
def small_or_large_with_if_elif_elif_elif_elif_elif_elif_else(n):
    if n < 0:
        return "mouse"
    elif n <= 2:
        return "house"
    elif n >= 3:
        return "dog"
    elif n >= 4:
        return "cat"
    elif n >= 5:
        return "fish"
    elif n >= 6:
        return "turtle"
    elif n >= 7:
        return "horse"
    else:
        return "monkey"


@njit
def small_or_large_with_if_elif_elif_elif_elif_elif_elif_elif_else(n):
