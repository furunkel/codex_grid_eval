
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha384-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha384(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha384-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha384(hash.encode()).hexdigest()

def hash_zu_zeichenkette_mit_laenge(hash, laenge):
    """
    Geben sei ein sha384-Hash 'hash' und eine natürliche Zahl 'laenge'.
    Zurückgegen werden soll die Zeichenkette, die diesen Hash erzeugt hat,
    jedoch nur die ersten 'laenge' Zeichen.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha384(hash.encode()).hexdigest()[:laenge]

def hash_zu_zeichenkette_mit_laenge_und_vorzeichen(hash, laenge):
    """
    Geben sei ein sha384-Hash 'hash' und eine natürliche Zahl 'laenge'.
    Zurückgegen werden soll die Zeichenkette, die diesen Hash erzeugt hat,
    jedoch nur die ersten 'laenge' Zeichen.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha384(hash.encode()).hexdigest()[:laenge]

def hash_zu_z