
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the first value of the tuple with the smallest third value.
    """
    return min(text, key=lambda x: x[2])[0]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of values from the tuples with the smallest third value.
    """
    return [x[0] for x in text if x[2] == min(text, key=lambda x: x[2])[2]]


def count_words(text):
    """
    Given a string, write a function that returns a dictionary that has a key for each word in the string, with the value
    being how many times that word appears in the string.
    """
    return {x: text.count(x) for x in text.split()}


def unique_words(text):
    """
    Given a string, write a function that returns a list of words from the string with no duplicates.
    """
    return list(set(text.split()))


def count_unique(text):
    """
    Given a string, write a function that returns the count of unique words in the string.
    """
    return len(set(text.split()))


def common_items(list1, list2):
    """
    Given two lists, write a function that returns a list of the common items shared between the lists.
    """
    return list(set(list1) & set(list2))


def uncommon_items(list1, list2):
    """
    Given two lists, write a function that returns a list of the uncommon items shared between the lists.
    """
    return list(set(list1) ^ set(list2))


def common_items_count(list1, list2):
    """
    Given two lists, write a function that returns a dictionary with a key for each unique word in both lists, with the
    value being how many times that word appears in both lists.
    """
    return {x: list1.count(x) + list2.count(x) for x in set(list1) & set(list2)}


def common_items_count_sorted(list1, list2):
    """
    Given two lists, write a function that returns a dictionary