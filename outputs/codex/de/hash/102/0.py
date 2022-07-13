
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha512(hash.encode()).hexdigest()

def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha-512-Hash von 'text' mit 'salt' als Salt (wiederum als
    Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha512((text + salt).encode()).hexdigest()

def hash_mit_salt_zu_zeichenkette(hash, salt):
    """
    Geben sei ein sha-512-Hash 'hash' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll die Zeichenkette, die diesen Hash mit 'salt' als Salt erzeugt
    hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha512((hash + salt).encode()).hexdigest()

def zeichenkette_zu_hash_mit_salt_und_iterationen(text, salt, iterationen