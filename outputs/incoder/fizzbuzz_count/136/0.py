
def fizz_buzz(n:int):
    """Return the number of times the digit 1 appears in integers less than n which are divisible by 1837 or 13.
    >>> fizz_buzz(78)
    1
    """
    if n<0:
        return 0
    elif n==0 or n==1:
        return 1
    else:
        return fizz_buzz(n//3)+fizz_buzz(n//3*3)+fizz_buzz(n//3*3*3)+fizz_buzz(n//3*3*3*3)+fizz_buzz(n//3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*3)+fizz_buzz(n//3*3*3*3*3*3*3*3*3*3*3*3*3*3*3*