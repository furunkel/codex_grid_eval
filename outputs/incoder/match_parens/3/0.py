
def match_brackets(lst):
    '''
    You are given a list of two strings, both strings consist of open
    brackets '<' or close brackets '>' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all brackets in S
    are balanced. For example: the string '<<>><>' is good, while the string
    '<>>' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['<><', '>']) == 'Yes'
    match_parens(['>', '>']) == 'No'
    '''
    lst = list(lst)
    stack = []
    for x in lst:
        if x == '<':
            stack.append(x)
        elif x == '>':
            if len(stack) == 0:
                return 'No'
            stack.pop()
        else:
            if len(stack) == 0:
                return 'No'
            stack.append(x)
    if len(stack) != 0:
        return 'No'
    return 'Yes'


def match_parens(lst):
    '''
    You are given a list of two strings, both strings consist of open
    parenthesis '(' or close parenthesis ')' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all parenthesis in S
    are balanced. For example: the string '(()())' is good, while the string
    '()(())' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '(', '