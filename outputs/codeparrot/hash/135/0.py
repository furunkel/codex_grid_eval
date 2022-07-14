def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if not text:
        return None
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
        return text[10:-1]
    if text[-1] == '2':
        return text[11:-1]
    if text[-1] == '3':
        return text[12:-1]
    if text[-1] == '4':
        return text[13:-1]
    if text[-1] == '5':
        return text[14:-1]
    if text[-1] == '6':
        return text[15:-1]
    if text[-1] == '7':
        return text[16:-1]
    if text[-1] == '8':
        return text[17:-1]
    if text[-1] == '9':
        return text[18:-1]
    if text[-1] == '0':
        return None
    return text

def get_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>>