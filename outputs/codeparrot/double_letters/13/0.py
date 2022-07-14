def double_letters(string):
    """
    Given a string, return the string, doubling every number character, and tripling every question mark.
    All other characters should be output a single time each.
    """
    return "".join([char for char in string if char.isalpha()])


def get_random_string(length):
    """
    Returns a random string of length length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length(length):
    """
    Returns a random string of length length.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)])


def get_random_string_with_length_and_question_mark(length, question_mark):
    """
    Returns a random string of length length and question mark.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)]) + question_mark


def get_random_string_with_length_and_question_mark_and_length(length, question_mark, length_question_mark):
    """
    Returns a random string of length and question mark and length question mark and length question mark and length question mark.
    """
    return ''.join([random.choice(string.letters) for _ in range(length)]) + question_mark + length_question_mark + length


def get_random_string_with_length_and_question_mark_and_question_mark_and_length_and_question_mark(length, question_mark, length_question_mark, length_question_mark_and_length):
    """
    Returns a random string of length and question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length question mark and length