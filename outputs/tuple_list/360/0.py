
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the smallest first value.
    """
    return min(text, key=lambda x: x[0])[1]


def extract_values(text):
    """
    Given a list of tuples, write a function that returns a list of the second values of the tuples.
    """
    return [x[1] for x in text]


def remove_duplicates(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples with the duplicates removed.
    """
    return list(set(text))


def swap_first_last(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples with the first and last items swapped.
    """
    return [(x[-1], x[1:-1], x[0]) for x in text]


def sort_by_last_letter(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples sorted by the last item in the tuple.
    """
    return sorted(text, key=lambda x: x[-1])


def sort_by_length(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples sorted by the length of the tuple.
    """
    return sorted(text, key=lambda x: len(x))


def sort_by_second_letter(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples sorted by the second item in the tuple.
    """
    return sorted(text, key=lambda x: x[1])


def sort_by_last_three_letters(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples sorted by the last three items in the tuple.
    """
    return sorted(text, key=lambda x: x[-3:])


def sort_by_first_letter(text):
    """
    Given a list of tuples, write a function that returns a list of the tuples sorted by the first item in the tuple.
    """
    return sorted(text, key=lambda x: