
def string_to_hash(text):
    """
    Given a string 'text', return its sha-256 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '3ebff31b62c0637c54d4ffa990d5c100ea359994b35f4b342ff49797542148cd'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('md5')
    0
    >>> string_to_int('md5')
    1
    >>> string_to_int('md5')
    Traceback (most recent call last):
    ValueError: the string 'md5' is not a valid integer
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('md5')
    0
    >>> string_to_bool('md5')
    1
    >>> string_to_bool('md5')
    Traceback (most recent call last):
    ValueError: the string 'md5' is not a valid boolean
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('md5')
    datetime.datetime(2012, 1, 1, 0, 0)
    >>> string_to_datetime('md5')
    Traceback (most recent call last):
    ValueError: the string 'md5' is not a valid datetime
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('md5')
    datetime.time(12, 34, 56, 34)
    >>> string_to_time('md5')
    Traceback (most recent call last):
    ValueError: the string 'md5' is not a valid time
    """

def string_to_datetime_tz(text):
    """
    Given a string '