
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der blake2s-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return blake2s(text.encode()).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein blake2s-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return blake2s(hash.encode()).hexdigest()


def hash_zu_zahl(hash):
    """
    Geben sei ein blake2s-Hash 'hash'. Zurückgegen werden soll die Zahl,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return int(blake2s(hash.encode()).hexdigest(), 16)


def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der blake2s-Hash
    dieser Zahl (wiederum als Zeichenkette).
    Ist 'zahl' eine leere Zahl, soll None zurückgegeben werden.
    """
    if zahl == 0:
        return None
    else:
        return blake2s(str(zahl).encode()).hexdigest()


def zahl_zu_zeichenkette(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll die Zeichenkette,
    die diese Zahl erzeugt hat.
    Ist 'zahl' eine leere Zahl, soll None zurückgegeben werden.