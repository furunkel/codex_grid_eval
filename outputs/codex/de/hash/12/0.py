
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der md-5-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.md5(text.encode()).hexdigest()

def zeichenkette_zu_sha1(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha1(text.encode()).hexdigest()

def zeichenkette_zu_sha256(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha256-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha256(text.encode()).hexdigest()

def zeichenkette_zu_sha512(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.
    """
    if text == "":
        return None
    else:
        return hashlib.sha512(text.encode()).hexdigest()

def zeichenkette_zu_sha3_256(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha3_256-Hash
    dieser Zeichenkette (wiederum