
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('sha1') == 'bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA224-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('bedb87f662c96d4ae159dab7c55a49ea268f92099d198bdad0f72c35') == 'sha1'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha224(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und ein Salt 'salt'. Zurückgegen werden
    soll der SHA224-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('sha1', 'salt') == 'b8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8f8'
    """
    if text == '':
        return None
    else:
        return hashlib.sha224(text.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein SHA224-Hash 'hash' und ein Salt 'salt'. Zurückgegen w