

def product_of_multiples(n):
    """Returns the product of all the multiples of 2 or 5 below n."""
    product = 1
    for i in range(2, n):
        if i % 2 == 0 or i % 5 == 0:
            product *= i
    return product

print(product_of_multiples(197))