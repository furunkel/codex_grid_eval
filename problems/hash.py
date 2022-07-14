from problems.default import default_generate
import hashlib
import re

TARGET = {'': 'string_to_hash', 'de': 'zeichenkette_zu_hash', 'tlh': 'ghop_D_hash' }
INPUTS = ["Hello world", "A B C", "password", ""]
TEST_IMPORTS = ['hashlib']
ORIGIN = "humaneval"

TEXT = """
def string_to_hash(text):
    \"\"\"
    Given a string 'text', return its {transformed_hash_type} hash equivalent string.
    If 'text' is an empty string, return None.{example}
    \"\"\"
"""

EXAMPLE = "\n\n    >>> {target_name}('{example_input}') == '{example_output}'"

TEXT_DE = """
def zeichenkette_zu_hash(text):
    \"\"\"
    Geben sei eine Zeichenkette 'text'. Zurückgegen werden soll der {transformed_hash_type}-Hash
    dieser Zeichenkette (wiederum als Zeichenkette).
    Ist 'text' eine leere Zeichenkette, soll None zurückgegeben werden.{example}
    \"\"\"
"""

TEXT_TLH = """
def ghop_D_hash(vIdaj):
    \"\"\"
    Ach batlh ghIlghameS 'vIdaj' neH {transformed_hash_type} hash ghopDu.
    qaSbe'chugh, vaj 'vIdaj' po'vaD qaS wanI'vam.{example}
    \"\"\"
"""

TEXTS = {
    'tlh': TEXT_TLH,
    'de': TEXT_DE,
    '': TEXT
}

GRID = {
    'hash_type': [
        'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', 'sha3_512'
    ],
    'transform': ['none', 'uppercase', 'dash'],
    'example_input': [None, 'Hello world', 'Hallo welt', '0', 'sha1', 'md5']
}

def filter(vars):
    return True

def oracle_(input, hash_type):
    if not input: return None
    f = hashlib.new(hash_type)
    f.update(input.encode('ascii'))
    return f.hexdigest()

def oracle(vars, input):
    return oracle_(input=input, hash_type=vars['hash_type'])

def render(lang, **vars):
    t = vars['transform']
    ht = vars['hash_type']

    if t == 'uppercase':
        tht = ht.upper()
    elif t == 'dash':
        if '_' in ht:
            tht = ht.replace('_', '-')
        else:
            tht = re.sub(r"(\d+)$", "-\\1", ht)
    elif t == 'none':
        tht = ht

    vars['transformed_hash_type'] = tht
    example_input = vars['example_input']
    if example_input:
        example_output = oracle_(example_input, ht)
        vars['example'] = EXAMPLE.format(target_name=TARGET[lang], example_input=example_input, example_output=example_output)
    else:
        vars['example'] = ''

    return TEXTS[lang].format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
