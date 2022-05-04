
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA224-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode()).hexdigest()

def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA224-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha224(hash.encode()).hexdigest()

def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein SHA224-Hash 'hash' und ein Salt 'salt'. Zurückgegen werden soll
    die zugehörige Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.
    """
    if hash == "":
        return None
    else:
        return hashlib.sha224(hash.encode() + salt.encode()).hexdigest()

def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und ein Salt 'salt'. Zurückgegen werden
    soll der SHA224-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha224(text.encode() + salt.encode()).hexdigest()

def zeichenkette_zu_hash_mit_salt_und_iterationen(text, salt, iterationen):
    """
    Geben sei eine Zeichenkette 'text', ein Salt 'salt' und eine