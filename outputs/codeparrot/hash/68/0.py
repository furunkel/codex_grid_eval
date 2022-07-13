
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'a1401e39ea9735fdcebc52013babcc1143ff56664e025cae31b4323382e16e57'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hallo welt') == 0
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('Hallo welt') == 'false'
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('Hallo welt') == datetime.datetime(1977, 6, 12, 0, 0)
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('Hallo welt') == datetime.time(12, 0)
    """

def string_to_datetime_with_milliseconds(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime_with_milliseconds('Hallo welt') == datetime.datetime(1977, 6, 12, 0, 0)
    """

def string_to_time_with_milliseconds(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time_with_milliseconds('Hallo welt') == datetime.time(12, 0)
    """

def string_to_time_with_milliseconds