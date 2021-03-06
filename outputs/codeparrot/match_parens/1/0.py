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
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return lst[0] == '{'
    if len(lst) == 2:
        return lst[0] == '}'
    return False


def match_braces_and_paren(lst):
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
    match_braces_and_paren(['{}{', '}']) == 'Yes'
    match_braces_and_paren(['{', '}']) == 'No'
    '''
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return lst[0] == '{'
    if len(lst) == 2:
        return lst[0] == '}'
    return False


def match_braces_and_paren_and_close(lst):
    '''
    You are given a list of two strings, both strings consist of open
    braces '{' or close braces '}' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be