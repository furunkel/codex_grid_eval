

def sum_of_multiples(n, m):
    """Find the sum of all the multiples of n or m below 124."""
    sum = 0
    for i in range(124):
        if i % n == 0 or i % m == 0:
            sum += i
    return sum

print(sum_of_multiples(13, 17))