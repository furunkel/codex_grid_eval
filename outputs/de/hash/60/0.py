
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA256-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha256(hash.encode()).hexdigest()

def hash_zu_zeichenkette_mit_laenge(hash, laenge):
    """
    Geben sei ein SHA256-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha256(hash.encode()).hexdigest()[:laenge]

def zeichenkette_zu_hash_mit_laenge(text, laenge):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()[:laenge]

def zeichenkette_zu_hash_mit_laenge_und_salt(text, laenge, salt):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA256-Hash
    dieser