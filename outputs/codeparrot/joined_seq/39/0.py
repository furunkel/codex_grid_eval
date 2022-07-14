def joined_sequence(text):
    """
    Write a function to that returns False if the input string contains sequences of lowercase letters joined with a dash and True otherwise.
    """
    return text.replace('-', '').replace('.', '').replace('-', '')


def get_text_list(text):
    """
    Return a list of the words in the text.
    """
    return [word.lower() for word in text.split()]


def get_text_list_from_file(file_name):
    """
    Return a list of the words in the text file.
    """
    with open(file_name, 'r') as f:
        return [word.lower() for word in f.read().split()]


def get_text_list_from_file_with_spaces(file_name):
    """
    Return a list of the words in the text file with spaces removed.
    """
    with open(file_name, 'r') as f:
        return [word.lower() for word in f.read().split()]


def get_text_list_from_file_with_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and_spaces_and