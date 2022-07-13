
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """

def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent integer.
    If 'text' is an empty string, return None.

    >>> string_to_int('0') == 0
    True
    """

def string_to_float(text):
    """
    Given a string 'text', return its float equivalent float.
    If 'text' is an empty string, return None.

    >>> string_to_float('0.5') == 0.5
    True
    """

def string_to_bool(text):
    """
    Given a string 'text', return its boolean equivalent boolean.
    If 'text' is an empty string, return None.

    >>> string_to_bool('true') == True
    True
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent datetime.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('2015-01-01T00:00:00') == datetime.datetime(2015, 1, 1, 0, 0)
    True
    """

def string_to_date(text):
    """
    Given a string 'text', return its date equivalent datetime.
    If 'text' is an empty string, return None.

    >>> string_to_date('2015-01-01') == datetime.date(2015, 1, 1)
    True
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent datetime.
    If 'text' is an empty string, return None.

    >>> string_to_time('2015-01-01T00:00:00') == datetime.time(12, 0, 0)
    True
    """

def string_to_datetime_with_timezone(text):
    """
    Given a string 'text', return its datetime equivalent datetime.
    If 'text' is an empty string, return None.

    >>> string_to_datetime