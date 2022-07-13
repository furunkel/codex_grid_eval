
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == '5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9'
    """
    if text == '':
        return None
    else:
        return hashlib.sha256(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA256-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9') == '0'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha256(hash.encode('utf-8')).hexdigest()


def hash_zu_zahl(hash):
    """
    Geben sei ein SHA256-Hash 'hash'. Zurückgegen werden soll die Zahl, die
    diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zahl('5feceb66ffc86f38d952786c6d696c79c2dbc239dd4e91b46729d73a27fb57e9') == 0
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der SHA256-Hash dieser
    Zahl (wiederum als Zeichenkette).
    Ist 'zahl' eine negative Zahl, soll None zurückgegeben werden.

    >>> zahl_zu_hash(0) == '5feceb66ffc86f38d952786c6d696