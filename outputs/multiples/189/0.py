

def multiples(n):
    """Returns the product of all the multiples of 13 or 17 below n."""
    product = 1
    for i in range(1, n):
        if i % 13 == 0 or i % 17 == 0:
            product *= i
    return product

print(multiples(200))