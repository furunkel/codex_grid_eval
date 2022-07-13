
def f(lst):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest last value.
    """
    return max(lst, key=lambda t: t[-1])[1]


# %%
# Write a function that takes a list as input and returns a new list with the first element of the list repeated n times.
def repeat_n(lst, n):
    """
    Given a list and a number n, write a function that returns a new list with the first element of the list repeated n times.
    """
    return [lst[0]] * n


# %%
# Write a function that takes a list as input and returns a new list with the first element of the list repeated n times,
# followed by the second element of the list repeated n times, and so on.
def repeat_n_2(lst, n):
    """
    Given a list and a number n, write a function that returns a new list with the first element of the list repeated n times,
    followed by the second element of the list repeated n times, and so on.
    """
    return [lst[0]] * n + [lst[1]] * n


# %%
# Write a function that takes a list as input and returns a new list with the first element of the list repeated n times,
# followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
def repeat_n_3(lst, n):
    """
    Given a list and a number n, write a function that returns a new list with the first element of the list repeated n times,
    followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
    """
    return [lst[0]] * n + [lst[1]] * n + [lst[2]] * n


# %%
# Write a function that takes a list as input and returns a new list with the first element of the list repeated n times,
# followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
def repeat_n_4(lst, n):
    """
    Given a list and a number n, write a function that returns a new list with the first element of the list repeated n times,
    followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
    """
    return [lst[0]] * n + [lst[1]] * n + [lst[2]] * n + [lst[3]] * n


# %%
# Write a function that takes a list as input and returns a new list with the first element of the list repeated n times,
# followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
def repeat_n_5(lst, n):
    """
    Given a list and a number n, write a function that returns a new list with the first element of the list repeated n times,
    followed by the second element of the list repeated n times, and so on, until the n-th element of the list is reached.
    """
