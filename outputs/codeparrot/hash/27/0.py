
def string_to_hash(text):
    """
    Given a string 'text', return its SHA1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('0') == 0
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('0') == False
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('0') == datetime.datetime(1970, 1, 1)
    """

def string_to_date(text):
    """
    Given a string 'text', return its date equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_date('0') == datetime.date(1970, 1, 1)
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('0') == datetime.time(0, 0)
    """

def string_to_datetime_with_milliseconds(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime_with_milliseconds('0') == datetime.datetime(1970, 1, 1, 0, 0)
    """

def string_to_time_with_milliseconds(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time_with_milliseconds('0') == datetime.time(0, 0