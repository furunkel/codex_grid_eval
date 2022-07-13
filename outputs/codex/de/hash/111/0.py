
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der blake2b-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == 'e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7'
    """
    if text == '':
        return None
    else:
        return blake2b(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein blake2b-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == '0'
    """
    if hash == '':
        return None
    else:
        return blake2b(bytes.fromhex(hash)).hexdigest()


def hash_zu_zahl(hash):
    """
    Geben sei ein blake2b-Hash 'hash'. Zurückgegen werden soll die Zahl, die
    diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zahl('e9f11462495399c0b8d0d8ec7128df9c0d7269cda23531a352b174bd29c3b6318a55d3508cb70dad9aaa590185ba0fef4fab46febd46874a103739c10d60ebc7') == 0
    """
    if hash == '':
        return None
    else:
        return int(blake2b(bytes.fromhex(hash)).hexdigest(), 16)


def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen w