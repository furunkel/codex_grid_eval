from problems.default import default_generate

INPUTS = [
    "AsDf",
    "As?Df",
    "As??Df",
    "1234",
    "1?234",
    "a1?234",
    "a1?2?34",
    "#a@C",
    "#a?C",
    "6@2",
    "#$a^D",
    "#?a^D",
    "#?a^?D",
    "#ccc",
    "#c?c",
    "#c??c",
]

EXAMPLES = [
    "1234",
    "1234?",
    "ab",
    "#a@C",
]
ORIGIN = 'humaneval'

TARGET = "solve"

TEXT = """
def solve(s):
    \"\"\"You are given a string s.
    if s[i] is a {case_cond}, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains {reverse_cond}, reverse the string.
    The function should return the resulted string.
    Examples
    solve("{example_input1}") = "{example_output1}"
    solve("{example_input2}") = "{example_output2}"
    solve("{example_input3}") = "{example_output3}"
    solve("{example_input4}") = "{example_output4}"
    \"\"\"
"""

GRID = {
    'case_cond': ['letter', 'vowel', 'consonant'],
    'reverse_cond': ['no letters', 'letters', 
                     'exactly one question mark',
                     'more than one question mark',
                     'no question marks',
                     'one or more question marks']
}

def oracle_(input, case_cond, reverse_cond):
    idx = 0
    new_str = list(input)

    letter_count = 0
    question_mark_count = 0

    for i in input:
        is_alpha = i.isalpha()
        if is_alpha: letter_count += 1
        if i == '?': question_mark_count += 1

        if case_cond == 'letter':
            cond = is_alpha
        elif case_cond == 'vowel':
            cond = i in 'aeiou'
        elif case_cond == 'consonant':
            cond = i in 'bcdfghjklmnpqrstvwxysBCDFGHJKLMNPQRSTVWXYS'
        else:
            raise ValueError(f"invalid condition '{case_cond}'")

        if cond:
            new_str[idx] = i.swapcase()
        idx += 1
    s = ""
    for i in new_str:
        s += i

    if reverse_cond == 'no letters':
        reverse = letter_count == 0
    elif reverse_cond == 'letters':
        reverse = letter_count > 0
    elif reverse_cond == 'exactly one question mark':
        reverse = question_mark_count == 1
    elif reverse_cond == 'more than one question mark':
        reverse = question_mark_count > 1
    elif reverse_cond == 'no question marks':
        reverse = question_mark_count == 0
    elif reverse_cond == 'one or more question marks':
        reverse = question_mark_count > 0
    else:
        raise ValueError(f"invalid condition '{reverse_cond}'")

    if reverse:
        return s[len(s)::-1]
    return s


def oracle(vars):
    return oracle_(vars['input'], vars['case_cond'], vars['reverse_cond'])

def render(**vars):
    for i, e in enumerate(EXAMPLES):
        vars[f'example_input{i+1}'] = e
        vars[f'example_output{i+1}'] = oracle_(e, vars['case_cond'], vars['reverse_cond'])
    return TEXT.format(**vars)
            
def generate(*args, **kwargs):
    yield from default_generate(GRID, INPUTS, render, *args, **kwargs)
