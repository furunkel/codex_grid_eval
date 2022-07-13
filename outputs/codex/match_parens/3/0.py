
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
    # Your code here
    pass


def is_valid_ip(ip):
    '''
    You are given a string S, which represents an IP address.
    Your job is to check if it is a valid IP address.
    An IP address is valid if and only if it is in the form "A.B.C.D",
    where A, B, C and D are integers between 0 and 255 (inclusive).
    Return 'Yes' if it is a valid IP address, and return 'No' otherwise.

    Examples:
    is_valid_ip('1.2.3.4') == 'Yes'
    is_valid_ip('1.2.3.256') == 'No'
    '''
    # Your code here
    pass


def is_valid_ipv6(ip):
    '''
    You are given a string S, which represents an IP address.
    Your job is to check if it is a valid IPv6 address.
    An IPv6 address is valid if and only if it is in the form "A:B:C:D:E:F:G:H",
    where A, B, C, D, E, F, G and H are hexadecimal digits.
    Return 'Yes' if it is a valid IPv6 address, and return 'No' otherwise.

    Examples:
    is_valid_ipv6('2001:0db8:0000:0000:0000:ff00:0042:8329') == 'Yes'
    is_valid_ipv6('2001:db8:0:0:0:ff00:42:8329') == 'Yes'
    is_valid_ipv6('2001:0db8:0:0:0:ff00:0042:8329') == 'Yes'
    is_valid_ipv6('2001:0db8:0:0:0:ff00:0042:8329') == 'Yes'
    is_valid_ipv6('2001:0db8:0:0:0:ff00:0042:8329') == 'Yes'
    is_valid_ipv6('2001:0db8:0:0:0:ff00:0042:83