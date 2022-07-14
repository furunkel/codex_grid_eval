from problems.default import default_generate

TARGET = 'checksum'
INPUTS = ["123", "abc", "ffjeojf3rfh4hg4uihg438gh4hf,.,.,.rf43"]
ORIGIN = 'gpsbs'

TEXT = """
def checksum(string):
    \"\"\"
    Given a string, convert each character in the string into its integer ASCII value, sum them,
    take the sum modulo {mod}, add the integer value of {offset_char}, and then convert that integer back
    into its corresponding character (the checksum character).
    The program must print "Check sum is X", where X is replaced by the correct checksum character.
    \"\"\"
"""

GRID = {
    'offset_char': ['the space character', 'the newline character', 'uppercase X', 'lowercase u', 'an exclamation mark', 'a question mark'],
    'mod': [64, 128, 256],
}

OFFSET_CHAR_TABLE = {
    'the space character': ord(' '),
    'the newline character': ord("\n"),
    'uppercase X': ord('X'),
    'lowercase u': ord('u'),
    'an exclamation mark': ord('!'),
    'a question mark': ord('?'),
}

def oracle_(input, mod, offset_char):
    sm = 0
    sm = sum([ord(c) for c in input])
    sm = sm % mod
    sm += OFFSET_CHAR_TABLE[offset_char]
    return chr(sm)

def oracle(vars, input):
    return oracle_(input=input, **dict((k, vars[k]) for k in ('mod', 'offset_char')))

def render(**vars):
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
