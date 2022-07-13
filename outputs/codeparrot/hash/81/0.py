
def string_to_hash(text):
    """
    Given a string 'text', return its SHA384 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '5f91550edb03f0bb8917da57f0f8818976f5da971307b7ee4886bb951c4891a1f16f840dae8f655aa5df718884ebc15b'
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

def string_to_date(text):
    """
    Given a string 'text', return its date equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_date('0') == datetime.date(1970, 1, 1)
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
   