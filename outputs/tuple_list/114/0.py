
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the largest twelfth value.
    """
    return max(text, key=lambda x: x[11])[1]

def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return list(map(lambda x: x[1], filter(lambda x: x[11] > 0, text)))

def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract_values_7(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple with a twelfth value greater than zero.
    """
    return [x[1] for x in text if x[11] > 0]

def extract