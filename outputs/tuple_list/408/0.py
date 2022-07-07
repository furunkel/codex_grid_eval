
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest eleventh value.
    """
    return min(text, key=lambda x: x[11])[-1]

def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return min(text, key=lambda x: x[11])

def extract_values_list(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return [x[-1] for x in text]

def extract_values_list_2(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return [x[-1] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_list_3(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return [x[-1] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_list_4(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return [x[-1] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_list_5(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
    """
    return [x[-1] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_list_6(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuple with the smallest eleventh value.
   