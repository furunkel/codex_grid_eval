
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha512(hash.encode()).hexdigest()

def hash_zu_datei(hash, dateiname):
    """
    Geben sei ein SHA512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha512(hash.encode()).hexdigest()

def datei_zu_hash(dateiname):
    """
    Geben sei ein SHA512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha512(hash.encode()).hexdigest()

def datei_zu_zeichenkette(dateiname):
    """
    Geben sei ein SHA512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":