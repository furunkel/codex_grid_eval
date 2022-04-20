

def multiples(n):
    return [x for x in range(n) if x % 2 == 0 or x % 9 == 0]

def product(n):
    return reduce(lambda x, y: x * y, multiples(n))

print product(1000)