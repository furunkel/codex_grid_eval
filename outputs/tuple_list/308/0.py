
def f(text):
    """
    Given a list of tuples, write a function that returns the eleventh value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[11]

def g(text):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple.
    """
    return sum(x[1] for x in text)

def h(text):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    except for the tuple with the largest second value.
    """
    return sum(x[1] for x in text if x[1] != max(text, key=lambda x: x[1])[1])

def i(text):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    except for the tuple with the largest second value and the tuple with the smallest second value.
    """
    return sum(x[1] for x in text if x[1] != max(text, key=lambda x: x[1])[1] and x[1] != min(text, key=lambda x: x[1])[1])

def j(text):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    except for the tuple with the largest second value and the tuple with the smallest second value.
    """
    return sum(x[1] for x in text if x[1] != max(text, key=lambda x: x[1])[1] and x[1] != min(text, key=lambda x: x[1])[1])

def k(text):
    """
    Given a list of tuples, write a function that returns the sum of the second value of each tuple,
    except for the tuple with the largest second value and the tuple with the smallest second value.
    """
    return sum(x[1] for x in text if x[1] != max(text, key=lambda x: x[1])[1] and x[1] != min(text, key=lambda x: x[1])[1])

def l(text):
    """
    Given a list of