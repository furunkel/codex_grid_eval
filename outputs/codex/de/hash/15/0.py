
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der md-5-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == 'cfcd208495d565ef66e7dff9f98764da'
    """
    if text == '':
        return None
    else:
        return hashlib.md5(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein md-5-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('cfcd208495d565ef66e7dff9f98764da') == '0'
    """
    if hash == '':
        return None
    else:
        for i in range(0, 10):
            if zeichenkette_zu_hash(str(i)) == hash:
                return str(i)
        return None


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der md-5-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('0', '0') == 'c4ca4238a0b923820dcc509a6f75849b'
    """
    if text == '':
        return None
    else:
        return hashlib.md5((text + salt).encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein md-5-Hash 'hash' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll die Zeichenkette, die diesen Hash erzeugt hat.
    Ist 'hash'