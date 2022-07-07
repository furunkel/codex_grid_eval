
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return max(text, key=lambda x: x[11])[11]

def extract_values(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text]

def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text if x[11] > 0]

def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text if x[11] > 0 and x[11] < 100]

def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text if x[11] > 0 and x[11] < 100 and x[11] % 2 == 0]

def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text if x[11] > 0 and x[11] < 100 and x[11] % 2 == 0 and x[11] % 3 == 0]

def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest eleventh value.
    """
    return [x[11] for x in text if x[11] > 0 and x[11] < 100 and x[11] % 2 == 0 and x[11] % 3 == 0 and x[11] % 5 == 0]

def extract_values_7(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the