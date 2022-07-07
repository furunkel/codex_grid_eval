
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[-1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuples with the second value equal to 1.
    """
    return [x[-1] for x in text if x[1] == 1]


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of tuples where all the duplicates are removed.
    """
    return list(set(text))


def convert_to_dictionary(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    """
    return dict(text)


def convert_to_dictionary_of_lists(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    If there is more than one tuple with the same first item, append the second item to the list of values for that key.
    """
    return {k: [x[1] for x in g] for k, g in groupby(sorted(text), key=lambda x: x[0])}


def convert_to_dictionary_of_sets(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    If there is more than one tuple with the same first item, add the second item to the set of values for that key.
    """
    return {k: set(x[1] for x in g) for k, g in groupby(sorted(text), key=lambda x: x[0])}


def convert_to_dictionary_of_counts(text):
    """
    Given a list of tuples, write a function that returns a dictionary where the first tuple item is the key and the second is the value.
    If there is more than one tuple with the same first item, increment the count of values for that key.
