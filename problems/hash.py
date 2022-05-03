from problems.default import default_generate
import hashlib
import re

TARGET = 'string_to_hash'
INPUTS = ["Hello world", "A B C", "password", ""]
TEST_IMPORTS = ['hashlib']

TEXT = """
def string_to_hash(text):
    \"\"\"
    Given a string 'text', return its {transformed_hash_type} hash equivalent string.
    If 'text' is an empty string, return None.

    >>> string_to_hash('Hello world') == '{hash_value}'
    \"\"\"
"""

GRID = {
    'hash_type': [
        'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512', 'blake2b', 'blake2s', 'sha3_512'
    ],
    'transform': ['none', 'uppercase', 'dash'],
}

def filter(vars):
    return True

def oracle_(input, hash_type):
    if not input: return None
    f = hashlib.new(hash_type)
    f.update(input.encode('ascii'))
    return f.hexdigest()

def oracle(vars):
    return oracle_(**dict((k, vars[k]) for k in ('input', 'hash_type')))

def render(**vars):
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
    vars['hash_value'] = oracle_('Hello world', ht)

    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, filter_func=filter, **kwargs)
