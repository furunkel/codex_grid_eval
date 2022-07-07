
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest second value.
    """
    return min(text, key=lambda x: x[1])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values in the tuples with the second value greater than 1.
    """
    return [x[0] for x in text if x[1] > 1]


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of tuples with the duplicates removed.
    """
    return list(set(text))


def intersect(text1, text2):
    """
    Given two lists of tuples, write a function that returns a list of tuples that are in both lists.
    """
    return [x for x in text1 if x in text2]


def union(text1, text2):
    """
    Given two lists of tuples, write a function that returns a list of tuples that are in either list.
    """
    return list(set(text1 + text2))


def not_in(text1, text2):
    """
    Given two lists of tuples, write a function that returns a list of tuples that are in the first list but not the second.
    """
    return [x for x in text1 if x not in text2]


def most_frequent(text):
    """
    Given a list of tuples, write a function that returns the most frequent value.
    """
    return max(text, key=lambda x: x[1])[0]


def least_frequent(text):
    """
    Given a list of tuples, write a function that returns the least frequent value.
    """
    return min(text, key=lambda x: x[1])[0]


def most_frequent_n(text, n):
    """
    Given a list of tuples, write a function that returns the n most frequent values.
    """
    return sorted(text, key=lambda x: x[1], reverse=True)[:n]


def least_frequent_n(text, n):
    """
    Given a list of tuples, write