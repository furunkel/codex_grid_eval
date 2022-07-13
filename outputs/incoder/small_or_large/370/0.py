
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "small" if n >= 15 (and neither if -100 <= n < 15).
    """
    if n < -100:
        return "mouse"
    elif n >= 15:
        return "small"
    else:
        return "large"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
    Evaluate Legendre's constant C for given n.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2
    elif n == 2:
        return 5
    else:
        return ((3*n+2)//2)*(3*n+1)

def legendre_symbol(n, x):
    """
    Compute the Legendre symbol (Cn) for x
    """
    if x < 0 or x >= n:
        raise ValueError("x must be in [0, n[")
    if n <= 0:
        return 0
    if x == 0 or x == 1:
        return 1
    return f(n)*(x*legendre_symbol(n-1, x-1)+f(n-1))

def legendre_symbol_inverse(n, x):
    """
    Compute the inverse Legendre symbol (Cn) for x
    """
    if x < 0 or x >= n:
        raise ValueError("x must be in [0, n[")
    if n <= 0:
        return 0
    if x == 0 or x == 1:
        return 1
    return f(n)*legendre_symbol(n-1, x)

def legendre_normalized(n, x, k):
    """
    Normalize x^k for given n and x.
    """
    if x < 0 or x >= n:
        raise ValueError("x must be in [0, n[")
    if n <= 0:
        return 0
    if x == 0 or x == 1:
        return 1
    return f(n)/(legendre_symbol(n-1, x)*legendre_symbol_inverse(n-1, x))

def legendre_symbols(n, n_max):
    """
    Return a list of the Legendre symbols "S_n" for a geometric sequence of "n" terms
    """
    result = []
    if n_max == 0:
        return result
    elif n_max == 1:
        result.append(1)
    elif n_max == 2:
        result.append(2)
    else:
        for n in range(n_max):
            result.append(legendre_symbol(n, 0))
            result.append(legendre_symbol(n, 1))
    return result

def legendre_roots(n, n_max):
    """
    Return a list of the roots of the Legendre symbols "S_n" for a geometric sequence of "n" terms
    """
    result = []
    if n_max == 0:
        return result
    elif n_max == 1:
        return [-1, 1]
    elif n_max == 2:
        return [-1, 1, -1]
    else:
        for n in range(n_max):
            result.append(legendre_symbol_inverse(n, 0))
            result.append(legendre_symbol_inverse(n, 1))
            result.append(legendre_symbol_inverse(n, 2))
        return result

def legendre_to_quadratic(n, n_max):
    """
    Convert Legendre 