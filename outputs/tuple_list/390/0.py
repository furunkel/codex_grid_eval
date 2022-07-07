
def extract_value(text):
    """
    Given a list of tuples, write a function that returns the last value of the tuple with the largest third value.
    """
    return max(text, key=lambda x: x[2])[-1]


def extract_full_name(text):
    """
    Given a list of dictionaries, write a function that returns a list of values for the key name.
    """
    return [d['name'] for d in text]


def create_class_book(text):
    """
    Given a list of dictionaries, write a function that returns a dictionary with keys of the student's first name and
    values of their last name.
    """
    return {d['first_name']: d['last_name'] for d in text}


def create_class_book_reverse(text):
    """
    Given a list of dictionaries, write a function that returns a dictionary with keys of the student's last name and
    values of their first name.
    """
    return {d['last_name']: d['first_name'] for d in text}


def sort_by_last_letter_of_word(text):
    """
    Given a list of strings, write a function that sorts the list by the last letter of the word.
    """
    return sorted(text, key=lambda x: x[-1])


def sort_by_number_of_vowels(text):
    """
    Given a list of strings, write a function that sorts the list by the number of vowels in each word.
    """
    return sorted(text, key=lambda x: sum(c in 'aeiou' for c in x))


def sort_by_number_of_a(text):
    """
    Given a list of strings, write a function that sorts the list by the number of a's in each word.
    """
    return sorted(text, key=lambda x: x.count('a'))


def sort_by_number_of_consonants(text):
    """
    Given a list of strings, write a function that sorts the list by the number of consonants in each word.
    """
    return sorted(text, key=lambda x: sum(c not in 'aeiou' for c in x))


def sort_by_number_of_vowels_and