
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-224-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha224(hash.encode()).hexdigest()

def hash_zu_zeichenkette_mit_pruefung(hash):
    """
    Geben sei ein sha-224-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha224(hash.encode()).hexdigest()

def zeichenkette_zu_hash_mit_pruefung(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode()).hexdigest()

def hash_zu_zeichenkette_mit_pruefung_und_fehler(hash):
    """
    Geben sei ein sha-224-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt