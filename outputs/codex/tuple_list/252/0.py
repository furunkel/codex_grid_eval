
def extract_value(lst):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    return min(lst, key=lambda x: x[11])[11]

def extract_values(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == extract_value(lst)]

def extract_values_2(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == min(lst, key=lambda x: x[11])[11]]

def extract_values_3(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == min(x[11] for x in lst)]

def extract_values_4(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == min(x[11] for x in lst)]

def extract_values_5(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == min(x[11] for x in lst)]

def extract_values_6(lst):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in lst if x[11] == min(x[11] for x in lst)]

def extract_values_7