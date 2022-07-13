
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der BLAKE2S-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return blake2s(text.encode()).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein BLAKE2S-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return blake2s(bytes.fromhex(hash)).hexdigest()


def hash_zu_zahl(hash):
    """
    Geben sei ein BLAKE2S-Hash 'hash'. Zurückgegen werden soll die Zahl, die
    diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return int(hash, 16)


def zahl_zu_hash(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll der BLAKE2S-Hash dieser
    Zahl (wiederum als Zeichenkette).
    Ist 'zahl' eine negative Zahl, soll None zurückgegeben werden.
    """
    if zahl < 0:
        return None
    else:
        return blake2s(zahl.to_bytes(32, byteorder='big')).hexdigest()


def zahl_zu_zeichenkette(zahl):
    """
    Geben sei eine Zahl 'zahl'. Zurückgegen werden soll die Zeichenkette, die
    diese Zahl erzeugt hat.
    Ist 'zahl' eine negative Zahl, soll None zurückgegeben werden.
    """
   