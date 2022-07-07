
def f(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest eleventh value.
    """
    return min(text, key=lambda x: x[11])[12]

def g(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of the tuple with the smallest eleventh value.
    """
    return sum(x[12] for x in text)

def h(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of the tuple with the smallest eleventh value.
    """
    return sum(x[12] for x in text if x[11] == min(text, key=lambda x: x[11])[11])

def i(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of the tuple with the smallest eleventh value.
    """
    return sum(x[12] for x in text if x[11] == min(text, key=lambda x: x[11])[11] and x[10] == max(text, key=lambda x: x[10])[10])

def j(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of the tuple with the smallest eleventh value.
    """
    return sum(x[12] for x in text if x[11] == min(text, key=lambda x: x[11])[11] and x[10] == max(text, key=lambda x: x[10])[10] and x[9] == min(text, key=lambda x: x[9])[9])

def k(text):
    """
    Given a list of tuples, write a function that returns the sum of the twelfth value of the tuple with the smallest eleventh value.
    """
    return sum(x[12] for x in text if x[11] == min(text, key=lambda x: x[11])[11] and x[10] == max(text, key=lambda x: x[10])[10] and x[9] == min(text, key=lambda x: x[9])[9] and x[8] == max(text