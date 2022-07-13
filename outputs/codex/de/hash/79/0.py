
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA384-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hello world') == '9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1'
    """
    if text == '':
        return None
    else:
        return hashlib.sha384(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA384-Hash 'hash'. Zurückgegen werden soll die zugehörige
    Zeichenkette.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('9203b0c4439fd1e6ae5878866337b7c532acd6d9260150c80318e8ab8c27ce330189f8df94fb890df1d298ff360627e1') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha384(bytes.fromhex(hash)).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der SHA384-Hash von 'text' und 'salt' (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('Hello world', 'salt') == 'f8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f