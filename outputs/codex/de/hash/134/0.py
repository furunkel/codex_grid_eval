
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der BLAKE2S-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hallo welt') == '0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c'
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein BLAKE2S-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('0968ad866aa17fd901a1ac45fdd3dd52bf04e3fc3ea5c76d2197c2f32420c85c') == 'Hallo welt'
    """
    if hash == '':
        return None
    else:
        return blake2s(bytes.fromhex(hash)).hexdigest()


def zeichenkette_zu_hash_mit_salt(text, salt):
    """
    Geben sei eine Zeichenkette 'text' und eine Zeichenkette 'salt'. Zurückgegen
    werden soll der BLAKE2S-Hash dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_mit_salt('Hallo welt', 'salt') == 'b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9b8f9'
    """
    if text == '':
        return None
    else:
        return blake2s(text.encode('utf-8'), salt=salt.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette_mit_salt(hash, salt):
    """
