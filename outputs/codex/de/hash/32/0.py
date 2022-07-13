
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hallo welt') == '93b5dfe630dec53d4b7aa222499c63e546fee185'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-1-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('93b5dfe630dec53d4b7aa222499c63e546fee185') == 'Hallo welt'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha1(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha-1-Hash von 'text' und 'salt' (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('Hallo welt', 'salt') == 'b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8') + salt.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein sha-1-Hash 'hash' und eine Zeichenkette 'salt'. Zurückgegen
   