
def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == 'e2d4d570e508d98b24596f019b862b1c76fca9bfc79d62fa6111147c65b6bc8ae5662705693f2d7f1dc68e5c98c8e049'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hallo welt')
    0
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('Hallo welt')
    False
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('Hallo welt')
    datetime.datetime(1977, 6, 20, 0, 0)
    """

def string_to_date(text):
    """
    Given a string 'text', return its date equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_date('Hallo welt')
    datetime.date(1977, 6, 20)
    """

def string_to_time(text):
    """
    Given a string 'text', return its time equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_time('Hallo welt')
    datetime.time(0, 0, 0)
    """

def string_to_datetime_with_timezone(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime_with_timezone('Hallo welt')
    datetime.datetime(1977, 6, 20, 0,