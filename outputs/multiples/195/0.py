

def sum_of_multiples(n, m):
    """Returns the sum of all multiples of n or m below 1000"""
    sum = 0
    for i in range(1, 1000):
        if i % n == 0 or i % m == 0:
            sum += i
    return sum

print(sum_of_multiples(13, 17))