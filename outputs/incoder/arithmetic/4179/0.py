
def make_tuple(b, fekjfwoeifjwu5gfd):
    """
    Given two integers b and fekjfwoeifjwu5gfd, return a tuple where:
    The third element contains the product of the two numbers.
    The first element contains the difference of the two numbers (first - second).
    The second element contains the sum of the two numbers.
    """
    a, b, c = b, fekjfwoeifjwu5gfd, 0
    while b > 0:
        a, b = b, a % b
        c += a
    return c, b, a


def factor(n):
    """
    Given an integer n, return a list of all the prime factors of n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors(n):
    """
    Given an integer n, return a list of all the prime factors of n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors_sum(n):
    """
    Given an integer n, return a list of all the prime factors of n that sum to n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors_product(n):
    """
    Given an integer n, return a list of all the prime factors of n that multiply n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors_division(n):
    """
    Given an integer n, return a list of all the prime factors of n that divide n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors_division_product(n):
    """
    Given an integer n, return a list of all the prime factors of n that multiply n and divide n.
    """
    factors = []
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def prime_factors_division_product_sum(n):
    """
    Given an integer n, return a list of all the prime factors of n that multiply n and divide n that sum to n.
    """
    factors = []
    i = 2
    while i * i <= n: