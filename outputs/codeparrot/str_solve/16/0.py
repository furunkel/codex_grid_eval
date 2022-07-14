def solve(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "1234?"
    solve("ab") = "Ba"
    solve("#a@C") = "c@a#"
    """
    if not s:
        return s
    if s[0] == s[-1] == '"':
        return s[1:-1]
    else:
        return s[1:] + s[0:-1]

def solve_all(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve_all("1234") = "4321"
    solve_all("1234?") = "1234?"
    solve_all("ab") = "Ba"
    solve_all("#a@C") = "c@a#"
    """
    if not s:
        return s
    if s[0] == s[-1] == '"':
        return s[1:-1]
    else:
        return s[1:] + s[0:-1]

def solve_all_no_question(s):
    """You are given a string s.
    if s[i] is a consonant, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve_all_no_question("1234") = "4321"
    solve_all_no_question("1234?") = "1234?"
    solve_all_no_question("ab") = "Ba"
    solve_all_no_question("#a@C") = "c@a#"
    """
    if not s:
        return s
    if s[0] == s[-1] == '"':
        return s[1:-1]
    else:
       