
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der BLAKE2B-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return blake2b(text.encode(), digest_size=32).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein BLAKE2B-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' None, soll None zurückgegeben werden.
    """
    if hash == None:
        return None
    else:
        return blake2b(digest_size=32).update(hash.encode()).hexdigest()


def hash_zu_int(hash):
    """
    Geben sei ein BLAKE2B-Hash 'hash'. Zurückgegen werden soll die Zahl,
    die diesen Hash erzeugt hat.
    Ist 'hash' None, soll None zurückgegeben werden.
    """
    if hash == None:
        return None
    else:
        return int(hash, 16)


def int_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der BLAKE2B-Hash
    dieser Zahl (wiederum als Zeichenkette).
    Ist 'zahl' None, soll None zurückgegeben werden.
    """
    if zahl == None:
        return None
    else:
        return blake2b(digest_size=32).update(str(zahl).encode()).hexdigest()


def hash_zu_bytes(hash):
    """
    Geben sei ein BLAKE2B-Hash 'hash'. Zurückgegen werden soll die Bytes,
    die diesen Hash erzeugt hat.
    Ist 'hash' None, soll None zurückgegeben werden.
    """
    if hash == None:
       