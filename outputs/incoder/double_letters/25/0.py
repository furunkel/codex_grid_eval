
def double_letters(string):
    """
    Given a string, return the string, doubling every lower-case letter character, and tripling every number.
    All other characters should be output a single time each.
    """
    return ''.join(
        c if c.islower() else c.upper() * (2 if c.isdigit() else 1) for c in string
    )


@given('the string "{string}" is {length} characters long')
def string_length(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length]


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length] + ' ' + string[length:]


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length] + ' ' + string[length:] + '\n'


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_end(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length] + ' ' + string[length:] + '\n'


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_beginning(string, length):
    """
    Given a string, return the string, of length length.
    """
    return ' ' + string[:length] + ' ' + string[length:] + '\n'


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_middle(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length] + ' ' + string[length:] + '\n' + string[length:]


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_beginning_and_end(string, length):
    """
    Given a string, return the string, of length length.
    """
    return ' ' + string[:length] + ' ' + string[length:] + '\n' + string[length:]


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_middle_and_end(string, length):
    """
    Given a string, return the string, of length length.
    """
    return string[:length] + ' ' + string[length:] + '\n' + string[length:]


@given('the string "{string}" is {length} characters long')
def string_length_with_spaces_and_newlines_at_beginning_and_middle_and_end(string, length):
    """
    Given a string, return the string, of length length.
    """