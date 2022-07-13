
def double_letters(string):
    """
    Given a string, return the string, doubling every question mark character, and tripling every consonant (lower-case or upper-case).
    All other characters should be output a single time each.
    """
    return re.sub(r'([?])', lambda m: m.group()*2, string)

# ______________________________________________________________________________
# Miscellaneous functions

def flatten(listOfLists):
    "Flatten one level of nesting"
    return chain.from_iterable(listOfLists)

def repeatString(s, n):
    """
    Return the string repeated n times.
    """
    return s*n

def iterNTimes(f, times):
    """
    Iterate f() n times, yielding each iteration's result
    """
    return imap(f, range(times))

def argmin(seq, key=lambda x:x):
    """
    Return the minimum item in the given non-empty iterable using key
    (or identity).
    """
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-minimum-value-of-a-list-in-python
    # This is faster than a sort-based solution, but requires keeping a running min.
    # Thanks to Eric S. Raymond for the idea.
    # http://stackoverflow.com/questions/12165200/python-min-vs-lambda
    return min(seq, key=key)

def argmin_list(seq, key=lambda x:x):
    """
    Return the minimum item in the given non-empty iterable using key
    (or identity) and the items' position in the iterable.
    This is faster than the functional equivalent of argmin in Python 2.7
    """
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-minimum-value-of-a-list-in-python
    # This is faster than a sort-based solution, but requires keeping a running min.
    # Thanks to Eric S. Raymond for the idea.
    # http://stackoverflow.com/questions/12165200/python-min-vs-lambda
    return min(enumerate(seq), key=key)

def argmax(seq, key=lambda x:x):
    """
    Return the maximum item in the given non-empty iterable using key
    (or identity).
    """
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-minimum-value-of-a-list-in-python
    # This is faster than a sort-based solution, but requires keeping a running min.
    # Thanks to Eric S. Raymond for the idea.
    # http://stackoverflow.com/questions/12165200/python-min-vs-lambda
    return max(seq, key=key)

def argmax_list(seq, key=lambda x:x):
    """
    Return the maximum item in the given non-empty iterable using key
    (or identity) and the items' position in the iterable.
    This is faster than the functional equivalent of argmin in Python 2.7
    """
    # http://stackoverflow.com/questions/3071415/efficient-method-to-calculate-the-minimum-value-of-a-list-in-python
    # This is faster than a sort-based solution, but 