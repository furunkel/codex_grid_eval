
def zeichenkette_zu_hash(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der SHA3_512-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash('Hello world') == 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c'
    """
    if text == '':
        return None
    else:
        return hashlib.sha3_512(text.encode('utf-8')).hexdigest()


def hash_zu_zeichenkette(hash):
    """
    Geben sei ein SHA3_512-Hash 'hash'. Zurückgegen werden soll die Zeichenkette,
    die diesen Hash erzeugt hat.
    Ist 'hash' ein leerer String, soll None zurückgegeben werden.

    >>> hash_zu_zeichenkette('e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c') == 'Hello world'
    """
    if hash == '':
        return None
    else:
        return hashlib.sha3_512(hash.encode('utf-8')).hexdigest()


def zeichenkette_zu_hash_liste(text):
    """
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll eine Liste von
    SHA3_512-Hashes, die aus 'text' erzeugt wurden.
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.

    >>> zeichenkette_zu_hash_liste('Hello world') == ['e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0cf3433f94fc427ec0b9bebb12f327a3240021053db6091196576d5e6d9bd8fac71c0c', 'e2e1c9e522efb2495a178434c8bb8f11000ca23f1fd679058b7d7e141f0