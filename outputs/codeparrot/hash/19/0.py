
def string_to_hash(text):
    """
    Given a string 'text', return its sha1 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '7b502c3a1f48c8609ae212cdfb639dee39673f5e'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hello world') == 0
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('Hello world') == 'true'
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('Hello world') == datetime.datetime(1970, 1, 1)
    """

def string_to_date(text):
    """
    Given a string 'text', return its date equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_date('Hello world') == datetime.date(1970, 1, 1)
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('Hello world') == datetime.time(0, 0)
    """

def string_to_datetime_with_milliseconds(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime_with_milliseconds('Hello world') == datetime.datetime(1970, 1, 1, 0, 0)
    """

def string_to_time_with_milliseconds(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time_with_milliseconds('Hello world