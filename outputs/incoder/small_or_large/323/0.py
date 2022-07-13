
def small_or_large(n):
    """
        Given an integer n, return "mouse" if n < -100 and "large" if n >= 2000 (and neither if -100 <= n < 2000).
    """
    if n < 0:
        return "mouse"
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
        return ((3*n+2)//4)*f(n-1) + f(n-2)

def legendre_symbol(n, x):
    """
    Evaluate Legendre's constant Cn for given n and x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2*x
    else:
        return ((3*n+2)//4)*legendre_symbol(n-1, x) + legendre_symbol(n-2, x)

def legendre_symbol_inverse(n, x):
    """
    Evaluate inverse Legendre's constant Cn for given n and x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return ((3*n+2)//4)*legendre_symbol_inverse(n-1, x) - legendre_symbol_inverse(n-2, x)

def legendre_normalized(n, x):
    """
    Evaluate Legendre's normalized constant Cn for given n and x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return 2*x
    else:
        return ((3*n+2)//4)*legendre_normalized(n-1, x) + legendre_normalized(n-2, x)

def legendre_normalize_inverse(n, x):
    """
    Evaluate inverse Legendre's normalized constant Cn for given n and x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return ((3*n+2)//4)*legendre_normalize_inverse(n-1, x) - legendre_normalize_inverse(n-2, x)

def legendre_roots(n):
    """
    Return a list of Legendre roots for integer n.
    """
    if n == 0:
        return [0]
    elif n == 1:
        return [2]
    else:
        xs = [legendre_roots(n-1)[0]]
        for i in range(1, n):
            xs.append(2*xs[i-1] + xs[i])
        return xs

def legendre_eval(n, x):
    """
    Evaluate Legendre's polynomial for given n and x.
    """
    if n == 0:
        return 0
    elif n == 1:
        return x
    else:
        return legendre_eval(n-1, x) + legendre_eval(n-2, x)

def legendre_eval_derivative(n, x, dx):
    """
    Evaluate Legendre's polynomial for given n and x by differentiating 