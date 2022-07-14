def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of uppercase letters joined with a minus and True otherwise.
    """
    return text.upper().replace(' ', '')


def get_all_text(text):
    """
    Return a list of all the text in the given text.
    """
    return [x.strip() for x in text.split()]


def get_all_text_list(text):
    """
    Return a list of all the text in the given text.
    """
    return [x.strip() for x in text.split()]


def get_all_text_list_with_upper(text):
    """
    Return a list of all the text in the given text with the upper case letters removed.
    """
    return [x.upper() for x in text.split()]


def get_all_text_list_with_lower(text):
    """
    Return a list of all the text in the given text with the lower case letters removed.
    """
    return [x.lower() for x in text.split()]


def get_all_text_list_with_upper_and_lower(text):
    """
    Return a list of all the text in the given text with the upper and lower case letters removed.
    """
    return [x.upper() for x in text.split()]


def get_all_text_list_with_lower_and_upper(text):
    """
    Return a list of all the text in the given text with the lower and upper case letters removed.
    """
    return [x.lower() for x in text.split()]


def get_all_text_list_with_upper_and_lower_and_upper(text):
    """
    Return a list of all the text in the given text with the upper and lower and lower case letters removed.
    """
    return [x.upper() for x in text.split()]


def get_all_text_list_with_lower_and_upper_and_lower(text):
    """
    Return a list of all the text in the given text with the lower and upper and lower case letters removed.
    """
    return [x.lower() for x in text.split()]


def get_all_text_list_with_upper_and_lower_and