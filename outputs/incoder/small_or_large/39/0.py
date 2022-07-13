
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 2 and "large" if n >= 2000 (and neither if 2 <= n < 2000).
    """
    if n < 2:
        return "small"
    elif n >= 2000:
        return "large"
    else:
        return "small"

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
    else:
        return ((3*n+2)*f(n-1) - n*(3*n-1)) / f(n-2) - (n**3 - n)/3

def legendre_symbol(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p)

def legendre_symbol2(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-1)

def legendre_symbol3(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-2) - (2*n**2 - n)/(2*n-1)

def legendre_symbol4(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-3)

def legendre_symbol5(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-4)

def legendre_symbol6(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-5)

def legendre_symbol7(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-6)

def legendre_symbol8(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-7)

def legendre_symbol9(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/fact(p-8)

def legendre_symbol10(n, p):
    """
    Evaluate Legendre's constant C for given n and p.
    """
    return (-1)**p*n*f(n)/