
def f(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[12]

def g(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]

def h(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]

def i(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[1]

def j(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[0]

def k(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[0]

def l(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[1]

def m(text):
    """
    Given a list of tuples, write a function that returns the third value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[2]

def n(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest fourth value.
    """
    return min(text, key=lambda x: x[3])[0]

def o(text):
    """
    Given a list of tuples, write a function that returns the second value of the