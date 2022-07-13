
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der sha-1-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein sha-1-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('b6589fc6ab0dc82cf12099d1c2d40ab994e8410c') == '0'
    """
    if hash == '':
        return None
    else:
        for i in range(0, len(hash)):
            if zeichenkette_zu_hash(str(i)) == hash:
                return str(i)


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der sha-1-Hash von 'text' und 'salt' (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('0', '0') == 'b6589fc6ab0dc82cf12099d1c2d40ab994e8410c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha1((text + salt).encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
    Geben sei ein sha-1-Hash 'hash' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll die Zeichenkette, die dies