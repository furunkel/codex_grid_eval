def solve(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve("1234") = "4321"
    solve("1234?") = "1234?"
    solve("ab") = "bA"
    solve("#a@C") = "C@A#"
    """
    if not s:
        return s
    if len(s) == 1:
        return s
    if s[0] == s[-1]:
        return s
    if s[0] == s[len(s) - 1]:
        return s
    return s[1:] + s[:1]


def solve_with_vowel(s):
    """You are given a string s.
    if s[i] is a vowel, reverse its case from lower to upper or vise versa, 
    otherwise keep it as it is.
    If the string contains no question marks, reverse the string.
    The function should return the resulted string.
    Examples
    solve_with_vowel("ab") = "ab"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab?") = "ab?"
    solve_with_vowel("ab