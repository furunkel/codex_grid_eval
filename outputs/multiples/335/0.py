

def multiples(n):
    """Returns the product of all the multiples of 2 or 9 below n."""
    product = 1
    for i in range(2, n):
        if i % 2 == 0 or i % 9 == 0:
            product *= i
    return product

print(multiples(1000))