
def f(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the smallest eleventh value.
    """
    return min(text, key=lambda x: x[10])[10]

def g(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest eleventh value.
    """
    return max(text, key=lambda x: x[10])[10]

def h(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the second smallest eleventh value.
    """
    return sorted(text, key=lambda x: x[10])[1][10]

def i(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the second largest eleventh value.
    """
    return sorted(text, key=lambda x: x[10], reverse=True)[1][10]

def j(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the third smallest eleventh value.
    """
    return sorted(text, key=lambda x: x[10])[2][10]

def k(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the third largest eleventh value.
    """
    return sorted(text, key=lambda x: x[10], reverse=True)[2][10]

def l(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fourth smallest eleventh value.
    """
    return sorted(text, key=lambda x: x[10])[3][10]

def m(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fourth largest eleventh value.
    """
    return sorted(text, key=lambda x: x[10], reverse=True)[3][10]

def n(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the fifth smallest eleventh value.
    """
    return sorted