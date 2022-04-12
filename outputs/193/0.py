

def multiples(x,y,z):
    """Finds the product of all the multiples of x or y below z."""
    product = 1
    for i in range(1,z):
        if i % x == 0 or i % y == 0:
            product *= i
    return product

print(multiples(13,17,600))