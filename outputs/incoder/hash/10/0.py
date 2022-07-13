
def string_to_hash(text):
    """
    Given a string 'text', return its MD5 hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if text:
        return hashlib.md5(text.encode('utf-8')).hexdigest()
    else:
        return None


def string_to_bytes(text):
    """
    Given a string 'text', return its bytes-like object equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_bytes('sha1') == b'74a89174426b40307102e165374ab8ab'
    """
    if text:
        return text.encode('utf-8')
    else:
        return None


def string_to_int(text):
    """
    Given a string 'text', return its integer equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('42') == 42
    """
    if text:
        return int(text)
    else:
        return None


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('42') == [42]
    """
    if text:
        return text.split(',')
    else:
        return None


def string_to_boolean(text):
    """
    Given a string 'text', return its boolean equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_boolean('True') == True
    """
    if text:
        return text.lower() in ['true', 'yes', '1']
    else:
        return None


def string_to_date(text):
    """
    Given a string 'text', return its date equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_date('2015-01-01') == date(2015, 1, 1)
    """
    if text:
        return datetime.strptime(text, '%Y-%m-%d').date()
    else:
        return None


def string_to_datetime(text):
    """
    Given a string 'text', return its datetime equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_datetime('2015-01-01T00:00:00') == datetime(2015, 1, 1)
    """
    if text:
        return datetime.strptime(text, '%Y-%m-%dT%H:%M:%S')
    else:
        return None


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list('42') == [42]
    """
    if text:
        return text.split(',')
    else:
        return None


def string_to_dict(text):
    """
    Given a string 'text', return its dict equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_dict('42') == {'a': 42}
    """
    if text:
        return json.loads(text)
    else:
        return None


def string_to_list(text):
    """
    Given a string 'text', return its list equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_list