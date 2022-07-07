
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of each tuple.
    """
    return [x[1] for x in text]


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of tuples where each tuple contains only unique elements.
    """
    return list(set(text))


def swap_elements(text):
    """
    Given a list of tuples, write a function that returns a list of tuples where the elements within each tuple have been swapped.
    """
    return [x[::-1] for x in text]


def reverse_list(text):
    """
    Given a list of tuples, write a function that returns a list of tuples where the elements within each tuple have been reversed.
    """
    return [tuple(reversed(x)) for x in text]


def convert_to_dictionary(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    """
    return {x[0]: x[1] for x in text}


def convert_to_dictionary_of_lists(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    If there is more than one tuple with the same first item, append the second item to the list of values for this key.
    """
    return {x[0]: [x[1]] if x[0] not in text else text[x[0]] + [x[1]] for x in text}


def convert_to_dictionary_of_sets(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    If there is more than one tuple with the same first item, add the second item to the set of values for this key.
   