
def fizz_buzz(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz(3298)
    212
    """
    if n % 7 == 0 or n % 11 == 0:
        return n
    else:
        return fizz_buzz(n//7) + fizz_buzz(n//11) + n%7 + n%11
</cell>
<cell>
def fizz_buzz_iterative(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz_iterative(3298)
    212
    """
    count = 0
    while n > 0:
        if n % 7 == 0 or n % 11 == 0:
            count += 1
        n //= 7
        n //= 11
    return count
</cell>
<cell>
def fizz_buzz_memoized(n:int):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz_memoized(3298)
    212
    """
    memo = {}
    def fizz_buzz(n):
        if n in memo:
            return memo[n]
        if n % 7 == 0 or n % 11 == 0:
            memo[n] = n
            return n
        else:
            memo[n] = fizz_buzz(n//7) + fizz_buzz(n//11) + n%7 + n%11
            return memo[n]
    return fizz_buzz(n)
</cell>
<cell>
def fizz_buzz_memoized_iterative(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz_memoized_iterative(3298)
    212
    """
    memo = {}
    count = 0
    while n > 0:
        if n in memo:
            count += 1
        n //= 7
        n //= 11
        memo[n] = count
    return memo[n]
</cell>
<cell>
def fizz_buzz_memoized_iterative_memoized(n):
    """Return the number of times the digit 7 appears in integers less than n which are divisible by 7 or 11.
    >>> fizz_buzz_memoized_iterative_memoized(3298)
    212
    """
    memo = {}
    count = 0
    def fizz_buzz(n):
        if n in memo:
            return memo[n]
        if n % 7 == 0 or n % 11 == 0:
            memo[n] = n
            return n
        else:
            memo[n] = fizz_buzz(n//7) + fizz_