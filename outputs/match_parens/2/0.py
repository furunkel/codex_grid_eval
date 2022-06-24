
def match_brackets(lst):
    '''
    You are given a list of two strings, both strings consist of open
    brackets '[' or close brackets ']' only.
    Your job is to check if it is possible to concatenate the two strings in
    some order, that the resulting string will be good.
    A string S is considered to be good if and only if all brackets in S
    are balanced. For example: the string '[[]][]' is good, while the string
    '[]]' is not.
    Return 'Yes' if there's a way to make a good string, and return 'No' otherwise.

    Examples:
    match_parens(['[][', ']']) == 'Yes'
    match_parens([']', ']']) == 'No'
    '''
    # Your code here
    pass


def is_valid_ip(ip):
    '''
    You are given a string S, which represents an IP address.
    Your job is to check if it is a valid IP address.
    An IP address is valid if and only if it satisfies the following conditions:
    1. It contains exactly 4 parts.
    2. Each part is between 0 and 255.
    3. Each part consists of digits only.
    4. No part has leading zeros.
    Return 'Yes' if it is a valid IP address, and return 'No' otherwise.

    Examples:
    is_valid_ip('1.2.3.4') == 'Yes'
    is_valid_ip('1.2.3.4.5') == 'No'
    is_valid_ip('123.45.67.89') == 'Yes'
    is_valid_ip('123.456.78.90') == 'No'
    is_valid_ip('123.045.067.089') == 'No'
    '''
    # Your code here
    pass


def is_valid_ipv6(ip):
    '''
    You are given a string S, which represents an IPv6 address.
    Your job is to check if it is a valid IPv6 address.
    An IPv6 address is valid if and only if it satisfies the following conditions:
    1. It contains exactly 8 parts.
    2. Each part is between 0 and FFFF.
    3. Each part consists of hexadecimal digits only.
    4. No part has leading zeros.
    Return 'Yes' if it is a valid IPv6 address, and return 'No' otherwise.

    Examples:
    is_valid_ipv6('2001:0db8:0000:0000:0000:ff00:0042:8329') == 'Yes'
    is_valid_ipv6('2001:db8:0:0:0:ff00:42:8329') == 'Yes'
    is_valid_ipv6('2001:0db8:0:0:0:ff00:0042:8329') == 'No'
    is_valid_ipv6('