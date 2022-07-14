def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '619a15b0f4dd21ef4bd626a9146af64561caf1325b21bccf755e4d7fbc31a65f'
    """
    if not text:
        return None
    if not isinstance(text, str):
        raise TypeError('text must be a string')
    if not text:
        raise ValueError('text cannot be empty')
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == 'L':
        return text[1:-1]
    if text[-1] == 'K':
        return text[2:-1]
    if text[-1] == 'M':
        return text[3:-1]
    if text[-1] == 'G':
        return text[4:-1]
    if text[-1] == 'T':
        return text[5:-1]
    if text[-1] == 'P':
        return text[6:-1]
    if text[-1] == 'E':
        return text[7:-1]
    if text[-1] == 'Z':
        return text[8:-1]
    if text[-1] == 'Y':
        return text[9:-1]
    if text[-1] == '1':
        return None
    raise ValueError('invalid string')


def string_to_int(text):
    """
    Given a string 'text', return its BLAKE2S int equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_int('Hello world') == 0
    >>> string_to_int('Hello world')
    0
    >>> string_to_int('')
    0
    >>> string_to_int('0')
    0
    >>> string_to_int('1')
    1
    >>> string_to_int('2')
    2
    >>> string_to_int('3')
    3
    >>> string_to_int('4')
    4
    >>> string_to_int('5')
    5
    >>> string_to_int('6')
    6
    >>> string_to