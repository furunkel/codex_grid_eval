
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der BLAKE2B-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('sha1') == 'ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1'
    """
    if text == '':
        return None
    else:
        return blake2b(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein BLAKE2B-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('ba1e2bf21c9191e5634d19d8878df04b62c5062fa5989311888bec25e0e6ceda1b7562ef6d4fec6e9643856f5297dcf0e12eb69a3c44dc51aef1d5114219f7d1') == 'sha1'
    """
    if hash == '':
        return None
    else:
        return blake2b(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der BLAKE2B-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('sha1', 'salt') == 'b9f9d8c8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d8d8f9b9c9f9d