
def f(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
    return min(text, key=lambda x: x[11])[-1]

def g(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the largest eleventh value.
    """
    return max(text, key=lambda x: x[11])[0]

def h(text):
    """
    Given a list of tuples, write a function that returns the sum of the eleventh values of all tuples.
    """
    return sum(x[11] for x in text)

def i(text):
    """
    Given a list of tuples, write a function that returns the sum of the eleventh values of all tuples with the first value equal to 'A'.
    """
    return sum(x[11] for x in text if x[0] == 'A')

def j(text):
    """
    Given a list of tuples, write a function that returns the sum of the eleventh values of all tuples with the first value equal to 'A' and the second value equal to 'B'.
    """
    return sum(x[11] for x in text if x[0] == 'A' and x[1] == 'B')

def k(text):
    """
    Given a list of tuples, write a function that returns the sum of the eleventh values of all tuples with the first value equal to 'A' and the second value equal to 'B' and the third value equal to 'C'.
    """
    return sum(x[11] for x in text if x[0] == 'A' and x[1] == 'B' and x[2] == 'C')

def l(text):
    """
    Given a list of tuples, write a function that returns the sum of the eleventh values of all tuples with the first value equal to 'A' and the second value equal to 'B' and the third value equal to 'C' and the fourth value equal to 'D'.
    """
    return sum(x[11] for x in text if x[0] == 'A' and x[1] == 'B' and x[2] == 'C' and x[3]