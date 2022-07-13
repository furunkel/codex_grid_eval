
def string_to_hash(text):
    """
    Given a string 'text', return its SHA3_512 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('md5') == '7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de'
    """

def string_to_int(text):
    """
    Given a string 'text', return its int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('md5')
    0
    >>> string_to_int('7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de')
    """

def string_to_bool(text):
    """
    Given a string 'text', return its bool equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bool('md5')
    False
    >>> string_to_bool('7e82fff92f72d30033578cf1a2d3ab6a55bf4e5f7523a4708ccf6a6ff440e50a1423f6f9f103b9280724649eedecfcb2b63d942801a8b6f7e3478bebc93bc0de')
    """

def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('md5')
    datetime.datetime(2013, 6, 6, 0, 0)
    >>> string_to_datetime('7e82fff92f72d30033578cf1a2d3ab