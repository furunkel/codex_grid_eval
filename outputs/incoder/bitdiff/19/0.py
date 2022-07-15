
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 29 bit positions.
    """
    return bin(a^b)[-29:] == '0'*29

def bit_diffs(a, b):
    """
    Returns a generator of bit differences between the two numbers.
    """
    return zip(range(len(a)), bit_diff(a, b))

def bit_diffs_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return sum(1 for _ in bit_diffs(a, b))

def bit_diffs_ratio(a, b):
    """
    Returns the ratio of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diffs_ratio(a, b))

def bit_diffs_ratio_sum_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum_diff(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diffs_ratio(a, b))/len(a)

def bit_diffs_ratio_sum_diff_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum_diff_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diffs_ratio(a, b))/len(a)

def bit_diffs_ratio_sum_diff_sum_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum_diff_sum_diff(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diffs_ratio(a, b))/len(a)

def bit_diffs_ratio_sum_diff_sum_diff_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum_diff_sum_diff_sum(a, b):
    """
    Returns the sum of bit differences between the two numbers.
    """
    return sum(bit_diffs_ratio(a, b))/len(a)

def bit_diffs_ratio_sum_diff_sum_diff_sum_count(a, b):
    """
    Returns the number of bit differences between the two numbers.
    """
    return bit_diffs_count(a, b)/len(a)

def bit_diffs_ratio_sum_diff_sum_diff_sum_diff(a, b):
