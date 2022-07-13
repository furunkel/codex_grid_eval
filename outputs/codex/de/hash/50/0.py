
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hallo welt') == 'fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-224-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('fa69fc6cbf7cb57890a921eae546e4b002472f7162eb68fbcb1cbf31') == 'Hallo welt'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha224(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha-224-Hash von 'text' und 'salt' (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('Hallo welt', 'salt') == 'f8f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9f9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224((text + salt).encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein sha-224-Hash 'hash' und eine Ze