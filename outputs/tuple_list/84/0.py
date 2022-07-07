
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the second value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuples.
    """
    return [x[1] for x in text]


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of tuples with the duplicates removed.
    """
    return list(set(text))


def swap_elements(text):
    """
    Given a list of tuples, write a function that swaps the order of the values in the tuples.
    """
    return [(x[1], x[0]) for x in text]


def add_to_dictionary(text):
    """
    Given a list of tuples, write a function that adds the last value of each tuple to a dictionary as a key, if the key does not already exist.
    """
    return {x[1]: x[0] for x in text}


def count_words(text):
    """
    Given a list of tuples, write a function that counts the number of occurrences of each word in the list.
    """
    return {x: text.count(x) for x in text}


def count_words_advanced(text):
    """
    Given a list of tuples, write a function that counts the number of occurrences of each word in the list.
    """
    return {x: text.count(x) for x in set(text)}


def generate_pairs(text):
    """
    Given a list of tuples, write a function that returns a list of tuples with the first item in each tuple being the second item of the tuple with the smallest first item.
    """
    return [(x[1], y[1]) for x in text for y in text if x[0] == min(text, key=lambda x: x[0])[0]]


def sort_by_key(text):
    """
    Given a list of tuples, write a function that returns a list of tuples sorted by the second item in each tuple.
    """
    return