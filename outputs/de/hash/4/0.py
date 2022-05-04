
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der md5-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('sha1') == '74a89174426b40307102e165374ab8ab'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha1(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha1('sha1') == 'f8c7e9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_sha256(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_sha256('sha256') == 'f8c7e9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9c9b8a8f8e9f9c9b9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def zeichenkette_zu_