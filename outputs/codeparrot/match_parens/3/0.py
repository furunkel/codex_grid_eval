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
    if len(lst) == 0:
        return False
    if len(lst) == 1:
        return lst[0] == lst[0]
    if len(lst) == 2:
        return lst[0] == lst[1] and lst[0] == lst[1]
    if len(lst) == 3:
        return lst[0] == lst[1] and lst[0] == lst[2]
    if len(lst) == 4:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 5:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 6:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 7:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 8:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 9:
        return lst[0] == lst[1] and lst[0] == lst[2] and lst[1] == lst[3]
    if len(lst) == 10:
        return lst[0] == lst[1]