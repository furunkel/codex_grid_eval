def string_to_hash(text):
    """
    Given a string 'text', return its blake2s hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if not text:
        return None
    text = text.strip()
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == 'L':
        return None
    if text[-1] == 'K':
        return None
    if text[-1] == 'M':
        return None
    if text[-1] == 'G':
        return None
    if text[-1] == 'T':
        return None
    if text[-1] == 'P':
        return None
    if text[-1] == 'E':
        return None
    if text[-1] == 'Z':
        return None
    if text[-1] == 'Y':
        return None
    if text[-1] == '1':
        return None
    if text[-1] == '2':
        return None
    if text[-1] == '3':
        return None
    if text[-1] == '4':
        return None
    if text[-1] == '5':
        return None
    if text[-1] == '6':
        return None
    if text[-1] == '7':
        return None
    if text[-1] == '8':
        return None
    if text[-1] == '9':
        return None
    if text[-1] == '0':
        return None
    if text[-1] == '1':
        return None
    if text[-1] == '2':
        return None
    if text[-1] == '3':
        return None
    if text[-1] == '4':
        return None
    if text[-1] == '5':
        return None
    if text[-1] == '6':
        return None
    if text[-1] == '7':
        return None
    if text[-1] == '8':
        return None
    if text[-1] == '9':
        return None
   