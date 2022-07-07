
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest second value.
    """
    return max(text, key=lambda x: x[1])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuples based on the value of the
    first item in the tuple.
    """
    return [x[1] for x in text if x[0] == 'a']


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of tuples with duplicate values removed.
    """
    return list(set(text))


def convert_to_dictionary(text):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple being the key
    and the second item in each tuple being the value.
    """
    return dict(text)


def convert_to_dictionary_with_counter(text):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple being the key
    and the second item in each tuple being the value. If there is more than one tuple with the same first value, add
    a counter to the end of the key to differentiate the keys.
    """
    return {x[0] + str(i): x[1] for i, x in enumerate(text)}


def convert_to_dictionary_with_sum(text):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple being the key
    and the second item in each tuple being the value. If there is more than one tuple with the same first value, add
    the values in the second item together.
    """
    return {x[0]: sum(y[1] for y in text if y[0] == x[0]) for x in text}


def convert_to_dictionary_with_sum_and_counter(text):
    """
    Given a list of tuples, write a function that returns a dictionary with the first item in each tuple being the key
    and the second item in each tuple being the value. If there is more than one tuple with the same