
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha3-512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha3_512(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha3-512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha3_512(hash.encode()).hexdigest()

def hash_zu_zahl(hash):
    """
    Geben sei ein sha3-512-Hash 'hash'. Zurückgegen werden soll die Zahl,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return int(hash, 16)

def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der sha3-512-Hash
    dieser Zahl (wiederum als Zeichenkette).
    Ist 'zahl' eine leere Zahl, soll None zurückgegeben werden.
    """
    if zahl == "":
        return None
    else:
        return hashlib.sha3_512(str(zahl).encode()).hexdigest()

def zahl_zu_zeichenkette(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll die Zeichenkette,
    die diese Zahl erzeugt hat.
    Ist 'zahl' eine leere Zahl, soll None zurückgegeben werden.
