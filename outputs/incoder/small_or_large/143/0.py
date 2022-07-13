
def small_or_large(n):
    """
        Given an integer n, return "small" if n < 1000 and "house" if n >= 2000 (and neither if 1000 <= n < 2000).
    """
    if n < 1000:
        return "small"
    elif n >= 2000:
        return "house"
    else:
        return "small"
</cell>
<cell>
small_or_large(1000)
</cell>
<cell>
small_or_large(2000)
</cell>
<cell>
small_or_large(3000)
</cell>
<text>
Exercise 4
Write a function that takes an integer n and returns the number of digits in n (not counting leading zeroes).


</text>
<cell>
def digits(n):
    """
        Given an integer n, return the number of digits in n (not counting leading zeroes).
    """
    return len(str(n))
</cell>
<cell>
digits(1000)
</cell>
<cell>
digits(2000)
</cell>
<cell>
digits(3000)
</cell>
<text>
Exercise 5
Write a function that takes an integer n and returns the number of digits in n that are not zero (not counting leading zeroes).


</text>
<cell>
def digits_not_zero(n):
    """
        Given an integer n, return the number of digits in n that are not zero (not counting leading zeroes).
    """
    return len(str(n))-len(str(n))%2
</cell>
<cell>
digits_not_zero(1000)
</cell>
<cell>
digits_not_zero(2000)
</cell>
<cell>
digits_not_zero(3000)
</cell>
<text>
Exercise 6
Write a function that takes an integer n and returns the number of digits in n that are evenly divisible by 3 (not counting leading zeroes).


</text>
<cell>
def digits_even_divisible_by_3(n):
    """
        Given an integer n, return the number of digits in n that are evenly divisible by 3 (not counting leading zeroes).
    """
    return len(str(n))-len(str(n))%2
</cell>
<cell>
digits_even_divisible_by_3(1000)
</cell>
<cell>
digits_even_divisible_by_3(2000)
</cell>
<cell>
digits_even_divisible_by_3(3000)
</cell>
<text>
Exercise 7
Write a function that takes an integer n and returns the number of digits in n that are evenly divisible by 5 (not counting leading zeroes).


</text>
<cell>
def digits_even_divisible_by_5