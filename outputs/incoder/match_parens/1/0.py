
def match_braces(lst):
    '''
    You are given a list of two strings, both strings consist of open
    braces '{' or close braces '}' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all braces in S
    are balanced. For example: the string '{{}}{}' is good, while the string
    '{}}' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['{}{', '}']) == 'Yes'
    match_parens(['}', '}']) == 'No'
    '''
    stack = []
    for c in lst:
        if c == '{':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0:
                return 'No'
            elif stack.pop() != '{':
                return 'No'
    return 'Yes'


def match_parentheses(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parentheses '(' or close parentheses ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parentheses in S
    are balanced. For example: the string '({{}})' is good, while the string
    '({})' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['({})', '({})']) == 'Yes'
    match_parens(['({}', '({}']) == 'No'
    '''
    stack = []
    for c in lst:
        if c == '(':
            stack.append(c)
        elif c == ')':
            if len(stack) == 0:
                return 'No'
            elif stack.pop() != '(':
                return 'No'
    return 'Yes'


def match_curly_braces(lst):
    '''
    You are given a list of two strings, both strings consist of open
    curly braces '{' or close curly braces '}' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all curly braces in S
    are balanced. For example: the string '{{}}{}' is good, while the string
    '{}}' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_curly_braces(['{{}}', '{}}']) == 'Yes'
    match_curly_braces(['{}}', '{}}']) == 'No'
    '''
    stack = []
    for c in lst:
        if c == '{':
            stack.append(c)
        elif c == '}':
            if len(stack) == 0:
                return 'No'
            elif stack.pop() != '{':
                return 'No'
    return 'Yes'


def match_angle_braces(lst):
    '''
    You are given a list of two strings, both strings consist of open
    angle braces '<' or close angle braces '>' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S