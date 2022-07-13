
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 2 bit positions.
    """
    return bin(a^b)[2:].count("1")==2

def bit_diffs(a, b):
    """
    Returns a generator of bit differences between the two numbers.
    """
    return ((i, bit_diff(a, b)) for i in range(31))

def bit_diffs_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return sum(1 for _ in bit_diffs(a, b))

def bit_diffs_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diff(a, b) for a, b in bit_diffs(a, b))

def bit_diffs_product(a, b):
    """
    Returns the product of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)*bit_diffs_count(a, b)

def bit_diffs_quotient(a, b):
    """
    Returns the quotient of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)/bit_diffs_count(a, b)

def bit_diffs_remainder(a, b):
    """
    Returns the remainder of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b) % bit_diffs_count(a, b)

def bit_diffs_quotient_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/bit_diffs_count(a, b)

def bit_diffs_quotient_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)/bit_diffs_count(a, b)

def bit_diffs_quotient_product(a, b):
    """
    Returns the product of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)*bit_diffs_quotient_count(a, b)

def bit_diffs_quotient_quotient(a, b):
    """
    Returns the quotient of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)/bit_diffs_quotient_count(a, b)

def bit_diffs_quotient_remainder(a, b):
    """
    Returns the remainder of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b) % bit_diffs_quotient_count(a, b)

def bit_diffs_quotient_quotient_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_quotient_count(a, b)/bit_diffs_quotient_count(a, b)

def bit_diffs_quotient_quotient_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return bit_diffs_sum(a, b)/bit_diffs_quotient_count(a, b)

def 