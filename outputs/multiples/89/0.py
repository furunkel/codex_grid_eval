

def multiples(n):
    """Returns the product of all the multiples of 5, 7 or 9 below n."""
    product = 1
    for i in range(1, n):
        if i % 5 == 0 or i % 7 == 0 or i % 9 == 0:
            product *= i
    return product

print(multiples(197))