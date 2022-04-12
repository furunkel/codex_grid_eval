

def multiples(n):
    """Returns the product of all the multiples of 2, 3 or 5 below n."""
    product = 1
    for i in range(1, n):
        if i % 2 == 0 or i % 3 == 0 or i % 5 == 0:
            product *= i
    return product

print(multiples(100))