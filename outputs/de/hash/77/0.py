
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha384-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('md5') == '86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha384-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('86264e50a98c4f4493859aad71fb0ccdd35413ddaf36a594eb133334d0b9f773426310cac10739911c2cc76d94731c3d') == 'md5'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha384(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_und_zurueck(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll die Zeichenkette,
    die den sha384-Hash von 'text' erzeugt hat.
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_und_zurueck('md5') == 'md5'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_und_zurueck(hash):
    """
    Geben sei ein sha384-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die den sha384-Hash von 'hash' erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückge