
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der blake2s-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == '652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de'
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein blake2s-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == '0'
    """
    if hash == '':
        return None
    else:
        return blake2s(bytes.fromhex(hash)).hexdigest()


def hash_zu_zahl(hash):
    """
    Geben sei ein blake2s-Hash 'hash'. Zurückgegen werden soll die Zahl,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zahl('652e530edee5893b576f72b875ea1c918e85e29d859e7e3fa78b623d8abca3de') == 0
    """
    if hash == '':
        return None
    else:
        return int(hash, 16)


def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der blake2s-Hash
    dieser Zahl (wiederum als Zeichenkette).
    Ist 'zahl' eine negative Zahl, soll None zurückgegeben werden.

    >>> zahl_zu_hash(0) == '652e530edee5893b576f72b875ea1c918e