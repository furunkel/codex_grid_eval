
def bit_diff(a, b):
    """
    Returns whether the two numbers differ at exactly 4 bit positions.
    """
    return bin(a^b)[-4:] == "100"

# ______________________________________________________________________________
# Simple Tasks
# ______________________________________________________________________________

def id(x):
    return x

def inc(x):
    return x + 1

def dec(x):
    return x - 1

def double(x):
    return x * 2

def halve(x):
    return x / 2

def plus(a, b):
    return a + b

def times(a, b):
    return a * b

def divides(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    return a % b

def lt(a, b):
    return a < b

def le(a, b):
    return a <= b

def eq(a, b):
    return a == b

def neq(a, b):
    return a != b

def ge(a, b):
    return a >= b

def gt(a, b):
    return a > b

def bit_or(a, b):
    return a | b

def bit_and(a, b):
    return a & b

def bit_xor(a, b):
    return a ^ b

def bit_shl(a, b):
    return a << b

def bit_shr(a, b):
    return a >> b

def bit_xor(a, b):
    return a ^ b

def list_append(a, b):
    a.append(b)
    return a

def list_length(a):
    return len(a)

def list_index(a, x):
    i = a.index(x)
    if i == -1: return None
    return i

def list_insert(a, i, x):
    a.insert(i, x)
    return a

def list_remove(a, i):
    a.pop(i)
    return a

def list_reverse(a):
    a.reverse()
    return a

def list_concat(a, b):
    return a + b

def list_contains(a, b):
    return b in a

def range_contains(a, b):
    return b in a # a.find(b) != -1

def list_sum(a):
    return sum(a)

def list_sort(a):
    a.sort()
    return a

def list_copy(a):
    return a[:]

def list_concat(a, b):
    return a + b

def list_contains(a, b):
    return b in a

def list_sum(a):
    return sum(a)

def list_sort(a):
    a.sort()
    return a

def list_copy(a):
    return a[:]

def list_concat(a, b):
    return a + b

def list_contains(a, b):
    return b in a

def list_sum(a):
    return sum(a)

def list_sort(a):
    a.sort()
    return a

def list_copy(a):
    return a[:]

def list_concat(a, b):
    return a + b

def list_contains(a, b):
    return b in 