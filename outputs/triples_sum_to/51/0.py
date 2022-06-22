
def doubles_sum_to_two(l: list):
    """
    doubles_sum_to_two takes a list of integers as an input.
    it returns True if there are 2 distinct elements in the list that
    sum to two, and False otherwise.

    >>> doubles_sum_to_two([1])
    False
    """
    # YOUR CODE HERE
    if len(l) < 2:
        return False
    for i in range(len(l)):
        for j in range(i+1, len(l)):
            if l[i] + l[j] == 2:
                return True
    return False


def is_palindrome(s: str):
    """
    is_palindrome takes a string as an input.
    it returns True if the string is a palindrome, and False otherwise.

    >>> is_palindrome("racecar")
    True
    """
    # YOUR CODE HERE
    for i in range(len(s)//2):
        if s[i] != s[len(s)-1-i]:
            return False
    return True


def is_palindrome_recursive(s: str):
    """
    is_palindrome_recursive takes a string as an input.
    it returns True if the string is a palindrome, and False otherwise.

    >>> is_palindrome_recursive("racecar")
    True
    """
    # YOUR CODE HERE
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome_recursive(s[1:-1])


def is_palindrome_recursive_helper(s: str, i: int):
    """
    is_palindrome_recursive_helper takes a string and an integer as inputs.
    it returns True if the string is a palindrome, and False otherwise.

    >>> is_palindrome_recursive_helper("racecar", 0)
    True
    """
    # YOUR CODE HERE
    if i >= len(s)//2:
        return True
    if s[i] != s[len(s)-1-i]:
        return False
    return is_palindrome_recursive_helper(s, i+1)


def is_palindrome_recursive_helper_2(s: str, i: int, j: int):
    """
    is_palindrome_recursive