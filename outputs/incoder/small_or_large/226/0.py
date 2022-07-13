
def small_or_large(n):
    """
        Given an integer n, return "large" if n < -100 and "small" if n >= 15 (and neither if -100 <= n < 15).
    """
    if n < -100:
        return "small"
    elif n >= 15:
        return "large"
    else:
        return "small"

# ______________________________________________________________________________
# Problem 5

def f(n):
    """
    Evaluate Legendre's function at a point n. Assume that Legendre's function is
    increasing everywhere: y(x) = 1/(x^2) for x>0, and y(0) = 1. 
    """
    if n == 0:
        return 1
    else:
        return ((2 * n - 1) / (n ** 2)) + f(n - 1)

def legendre_symbol(n, k):
    """
    Evaluate Legendre's symbol (n-th derivative of f) at a point k.
    """
    if n < 0:
        return 0
    elif n == 0:
        return -f(k)
    elif k == 0:
        return 2 * f(n)
    else:
        return ((2 * n - 1) / (n ** 2)) * f(k) + ((2 * k - 1) / (n ** 2)) * legendre_symbol(n - 1, k - 1)

def legendre_symbol2(n, k):
    """
    Evaluate Legendre's symbol (nth derivative of f) at a point k.
    """
    if n < 0:
        return 0
    elif n == 0:
        return -f(k)
    elif k == 0:
        return 2 * f(n)
    else:
        return ((2 * n - 1) / (n ** 2)) * f(k) + ((2 * k - 1) / (n ** 2)) * legendre_symbol2(n - 1, k - 1)

def legendre_normalized(n, method="ba"):
    """
    Normalize given Legendre function "f" at point n to 0..1 using method "method".
    """
    if method == "ba":
        return legendre_symbol(n, 0) / f(n)
    elif method == "li":
        return legendre_symbol(n, 1) / f(n)
    else:
        raise ValueError("Unknown normalization method")

def legendre_normalized2(n, method="ba"):
    """
    Normalize given Legendre function "f" at point n to 0..1 using method "method".
    """
    if method == "ba":
        return legendre_symbol2(n, 0) / f(n)
    elif method == "li":
        return legendre_symbol2(n, 1) / f(n)
    else:
        raise ValueError("Unknown normalization method")

def legendre_convert(n, from_, to_):
    """
    Convert given Legendre function "f" from from_ to to_.
    """
    if from_ == "ba" and to_ == "li":
        return legendre_symbol(n, 1) / f(n)
    elif from_ == "li" and to_ == "ba":
        return legendre_symbol(n, 0) / f(n)
    else:
        raise ValueError("Unknown 