
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '2d44da53f305ab94b6365837b9803627ab098c41a6013694f9b468bccb9c13e95b3900365eb58924de7158a54467e984efcfdabdbcc9af9a940d49c51455b04c'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('0') == 0
    True
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('0') == False
    True
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('0') == datetime.datetime(1970, 1, 1, 0, 0, 0)
    True
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('0') == datetime.time(0, 0)
    True
    """

def string_to_datetime_with_milliseconds(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime_with_milliseconds('0') == datetime.datetime(1970, 1, 1, 0, 0, 0)
    True
    """

def string_to_time_with_milliseconds(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time_with_milliseconds('0') == datetime.time