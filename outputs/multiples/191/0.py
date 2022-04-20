

def multiples(x,y,z):
    """x is the first multiple, y is the second multiple, z is the upper limit"""
    total = 0
    for i in range(z):
        if i % x == 0 or i % y == 0:
            total += i
    return total

print(multiples(13,17,500))