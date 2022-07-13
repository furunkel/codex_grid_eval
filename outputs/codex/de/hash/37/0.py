
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hello world') == 'ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha224-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('ac230f15fcae7f77d8f76e99adf45864a1c6f800655da78dea956112') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha224(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha224-Hash von 'text' und 'salt' (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('Hello world', 'salt') == 'b8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein sha224-Hash 'hash' und eine Zeichenkette 'salt'. Zur