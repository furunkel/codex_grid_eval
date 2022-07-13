
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-384-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha384(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-384-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha384(hash.encode()).hexdigest()

def zeichenkette_zu_hash_und_zurueck(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll die Zeichenkette,
    die den sha-384-Hash von 'text' erzeugt hat.
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha384(text.encode()).hexdigest()

def hash_zu_zeichenkette_und_zurueck(hash):
    """
    Geben sei ein sha-384-Hash 'hash'. Zurückgegen werden soll der sha-384-Hash
    der Zeichenkette, die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha384(hash.encode()).hexdigest()

def zeichenkette_zu_hash_und_zurueck_und_zurueck(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll die Zeichenkette,
    die den