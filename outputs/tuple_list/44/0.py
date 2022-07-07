
def f(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest twelfth value.
    """
    return max(text, key=lambda x: x[11])[0]

def g(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple.
    """
    return sum(x[11] for x in text)

def h(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple,
    but only if the first value of the tuple is 'red'.
    """
    return sum(x[11] for x in text if x[0] == 'red')

def i(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple,
    but only if the first value of the tuple is 'red' and the seventh value is greater than 100.
    """
    return sum(x[11] for x in text if x[0] == 'red' and x[6] > 100)

def j(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple,
    but only if the first value of the tuple is 'red' and the seventh value is greater than 100.
    """
    return sum(x[11] for x in text if x[0] == 'red' and x[6] > 100)

def k(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple,
    but only if the first value of the tuple is 'red' and the seventh value is greater than 100.
    """
    return sum(x[11] for x in text if x[0] == 'red' and x[6] > 100)

def l(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of each tuple,
    but only if the first value of the tuple is 'red' and the seventh value is greater than 100.
    """
    return sum(x[11] for x in text if x[0] == 'red' and x[6] >