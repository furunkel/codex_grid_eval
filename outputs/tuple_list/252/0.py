
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the twelfth value of the tuple with the smallest twelfth value.
    """
    return min(text, key=lambda x: x[11])[11]

def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == extract_value(text)]

def extract_values_2(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_3(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_4(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_5(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_6(text):
    """
    Given a list of tuples, write a function that returns a list of the twelfth values of the tuples with the smallest twelfth values.
    """
    return [x[11] for x in text if x[11] == min(text, key=lambda x: x[11])[11]]

def extract_values_