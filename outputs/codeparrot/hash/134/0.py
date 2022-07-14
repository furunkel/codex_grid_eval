def string_to_hash(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == 'L':
        return text[1:-1]
    if text[0] == '1':
        return text[1:]
    return None


def get_hash_from_text(text):
    """
    Given a string 'text', return its BLAKE2S hash equivalent string.
    If 'text' is an empty string, return None.

    >>> get_hash_from_text('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if not text:
        return None
    if len(text) == 0:
        return None
    if text[0] == '0':
        return None
    if text[-1] == 'L':
        return text[1:-1]
    if text[0] == '1':
        return text[1:]
    return None


def get_hash_from_file(path):
    """
    Given a path to a file, return its BLAKE2S hash equivalent string.
    If 'path' is an empty string, return None.

    >>> get_hash_from_file('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if not path:
        return None
    if len(path) == 0:
        return None
    if path[0] == '0':
        return None
    if path[-1] == 'L':
        return path[1:-1]
    if path[0] == '1':
       